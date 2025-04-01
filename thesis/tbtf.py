# tbtf.py: Core functions for TBTF strategy

# Import Libraries
import numpy as np
import pandas as pd

import statsmodels.api as sm
from scipy import stats
from scipy.stats import skew, kurtosis

# graphics
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# 6. Plot return distribution: TBTF vs. Market
# -----------------------------------------

def plot_benchmark_comparison(tbtf_returns, benchmark_df, period_label='pre-2010'):
    aligned_index = tbtf_returns.index

    if not isinstance(benchmark_df.index, pd.DatetimeIndex):
        if 'date' in benchmark_df.columns:
            benchmark_df = benchmark_df.set_index('date')
        else:
            raise KeyError("benchmark_df must have a datetime index or a 'date' column")

    for col in benchmark_df.columns:
        benchmark_series = benchmark_df[col].reindex(aligned_index)

        fig, axs = plt.subplots(1, 2, figsize=(12, 5))

        # 1. Return Distribution
        axs[0].hist(benchmark_series.dropna(), bins=40, alpha=0.6, label=col, density=True, color='gray')
        axs[0].hist(tbtf_returns.dropna(), bins=40, alpha=0.6, label='TBTF', density=True, color='steelblue')
        axs[0].axvline(tbtf_returns.mean(), color='blue', linestyle='--', label='TBTF Mean')
        axs[0].axvline(benchmark_series.mean(), color='black', linestyle='--', label=f'{col} Mean')
        axs[0].set_title(f'{period_label}: Return Distribution\nTBTF vs. {col}')
        axs[0].set_xlabel('Monthly Return')
        axs[0].legend()
        axs[0].grid(True)

        # 2. Price Level
        tb = (1 + tbtf_returns).cumprod()
        bm = (1 + benchmark_series).cumprod()
        axs[1].plot(tb.index, tb.values, label='TBTF', linewidth=2)
        axs[1].plot(bm.index, bm.values, label=col, linewidth=2, linestyle='--')
        axs[1].set_title(f'{period_label}: Price Level\nTBTF vs. {col}')
        axs[1].set_ylabel('Cumulative Value (Base = 1)')
        axs[1].legend()
        axs[1].grid(True)

        plt.tight_layout()
        plt.show()

def plot_return_distribution(tbtf_returns, market_returns, period_label="post-2010"):
    # 인덱스 통일
    tbtf_returns.index = pd.to_datetime(tbtf_returns.index)
    market_returns.index = pd.to_datetime(market_returns.index)

    # benchmark를 TBTF 기준에 맞춰 reindex
    market_aligned = market_returns.reindex(tbtf_returns.index)

    plt.figure(figsize=(8, 5))

    # 커널 밀도 추정 그래프 (scott)
    sns.kdeplot(tbtf_returns, bw_method='silverman', fill=True, label="TBTF", color='navy', linewidth=2)
    sns.kdeplot(market_returns, bw_method='silverman', fill=True, label="Market", color='gray', linewidth=2)

    # 통계값 계산
    tbtf_mean = tbtf_returns.mean()
    tbtf_std = tbtf_returns.std()
    market_mean = market_returns.mean()
    market_std = market_returns.std()

    # 수직선: 평균 및 ±1표준편차
    plt.axvline(tbtf_mean, color='navy', linestyle='--', linewidth=1.5, label='TBTF Mean')
    plt.axvline(tbtf_mean + tbtf_std, color='navy', linestyle='-', linewidth=1, label='TBTF ±1 STD')
    plt.axvline(tbtf_mean - tbtf_std, color='navy', linestyle='-', linewidth=1)

    plt.axvline(market_mean, color='red', linestyle='--', linewidth=1.5, label='Market Mean')
    plt.axvline(market_mean + market_std, color='red', linestyle='-', linewidth=1, label='Market ±1 STD')
    plt.axvline(market_mean - market_std, color='red', linestyle='-', linewidth=1)

    # 서식
    plt.title(f"Monthly Return Distribution ({period_label})")
    plt.xlabel("Monthly Return")
    plt.ylabel("Density")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 6. Plot normalized price level
# -----------------------------------------
def plot_price_level(tbtf_returns, market_returns, start_date=None, end_date=None):
    # Step 1: Series 확인
    if not isinstance(tbtf_returns, pd.Series) or not isinstance(market_returns, pd.Series):
        raise ValueError("Both inputs must be pandas Series objects.")

    # Step 2: 인덱스를 datetime으로 통일
    tbtf_returns.index = pd.to_datetime(tbtf_returns.index)
    market_returns.index = pd.to_datetime(market_returns.index)

    # Step 3: 내부 정렬 및 교집합 기준 정렬
    tbtf_aligned, market_aligned = tbtf_returns.align(market_returns, join='inner')

    # Step 4: 병합
    df = pd.DataFrame({
        "TBTF": tbtf_aligned,
        "Market": market_aligned
    })

    # Step 5: Optional filtering by start_date / end_date
    if start_date:
        df = df[df.index >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df.index <= pd.to_datetime(end_date)]

    # Step 6: 누적 곱으로 price 계산
    price_df = (1 + df).cumprod()

    # Step 7: 시각화
    plt.figure(figsize=(9, 5))
    plt.plot(price_df.index, price_df["TBTF"], label="TBTF", color='navy', linewidth=2)
    plt.plot(price_df.index, price_df["Market"], label="Market", color='gray', linewidth=2)
    plt.title("Normalized Price Level Comparison")
    plt.xlabel("Date")
    plt.ylabel("Price Level (Normalized to 1)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 6. Generate performance table for multiple portfolios
# -----------------------------------------
def generate_performance_table(returns_dict, eta=3, p=0.01):
    rows = []
    for name, series in returns_dict.items():
        perf = evaluate_performance(series, eta=eta, p=p)
        row = {"Portfolio": name}
        row.update(perf)
        rows.append(row)
    return pd.DataFrame(rows).set_index("Portfolio")


#########################################################################################

def plot_quadratic_fit(df_in_sample, n=10, state=10, ax=None):
    """
    특정 in-sample에서 주어진 state, top-n 종목에 대한
    (rank, capshare) 산점도와 quadratic regression fitted line 시각화
    """
    all_obs = []

    for date, group in df_in_sample[df_in_sample['state'] == state].groupby('date'):
        group = group.sort_values('mktcap_lag', ascending=False).head(n).copy()
        if len(group) < n:
            continue

        group = group.sort_values('mktcap_lag')  # rank: 1 = smallest
        group['rank'] = np.arange(1, len(group) + 1)
        total_cap = group['mktcap_lag'].sum()
        group['capshare'] = group['mktcap_lag'] / total_cap

        all_obs.append(group[['rank', 'capshare']])

    if not all_obs:
        raise ValueError("No valid observations for fitting.")

    df_all = pd.concat(all_obs, ignore_index=True)
    df_all['rank_sq'] = df_all['rank'] ** 2

    # 회귀
    X = sm.add_constant(df_all[['rank', 'rank_sq']])
    y = df_all['capshare']
    model = sm.OLS(y, X).fit()

    # 추정 계수
    alpha, beta, gamma = model.params

    # Fitted curve
    rank_grid = np.linspace(df_all['rank'].min(), df_all['rank'].max(), 100)
    fitted_curve = alpha + beta * rank_grid + gamma * rank_grid**2

    # 시각화
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df_all['rank'], df_all['capshare'], alpha=0.4, label='Observed', color='steelblue')
    ax.plot(rank_grid, fitted_curve, color='darkgreen', linewidth=2.5, label='Quadratic Fit')
    ax.set_title(f"Quadratic Fit (state={state}, n={n})")
    ax.set_xlabel("Rank")
    ax.set_ylabel("Capital Share")
    ax.legend()
    ax.grid(True)

    return 

def plot_exponential_fit(df_in_sample, n=10, state=10, ax=None):
    """
    특정 in-sample에서 주어진 state, top-n 종목에 대한
    (rank, capshare) 산점도와 exponential regression fitted line 시각화
    """

    all_obs = []

    for date, group in df_in_sample[df_in_sample['state'] == state].groupby('date'):
        group = group.sort_values('mktcap_lag', ascending=False).head(n).copy()
        if len(group) < n:
            continue

        group = group.sort_values('mktcap_lag')  # 작은 순서대로 재정렬
        group['rank'] = np.arange(1, len(group) + 1)
        total_cap = group['mktcap_lag'].sum()
        group['capshare'] = group['mktcap_lag'] / total_cap

        all_obs.append(group[['rank', 'capshare']])

    if not all_obs:
        raise ValueError("No valid observations for fitting.")

    df_all = pd.concat(all_obs, ignore_index=True)
    df_all['log_capshare'] = np.log(df_all['capshare'])

    # 회귀
    X = sm.add_constant(df_all['rank'])
    y = df_all['log_capshare']
    model = sm.OLS(y, X).fit()

    # 추정 계수
    ln_alpha, beta = model.params
    alpha = np.exp(ln_alpha)

    # Fitted curve
    rank_grid = np.linspace(df_all['rank'].min(), df_all['rank'].max(), 100)
    fitted_curve = alpha * np.exp(beta * rank_grid)

    # 시각화
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df_all['rank'], df_all['capshare'], alpha=0.4, label='Observed', color='steelblue')
    ax.plot(rank_grid, fitted_curve, color='darkred', linewidth=2.5, label='Exponential Fit')
    ax.set_title(f"Exponential Fit (state={state}, n={n})")
    ax.set_xlabel("Rank")
    ax.set_ylabel("Capital Share")
    ax.legend()
    ax.grid(True)

    return 


#########################################################################################


# -----------------------------------------
# Helper functions
# -----------------------------------------

def check_state_counts(df, state=10):
    counts = df[df['state'] == state].groupby('date').size()
    print(counts.describe())
    # check_state_counts(crsp, state=10)

def get_rebalance_offset(rebalance_freq):
    """
    rebalance_freq가 문자열로 주어지고 'M'으로 끝나면,
    해당 숫자만큼의 MonthEnd offset으로 변환합니다.
    예: '12M' -> pd.offsets.MonthEnd(12)
    그렇지 않으면 그대로 반환합니다.
    """
    if isinstance(rebalance_freq, str) and rebalance_freq.endswith('M'):
        num = int(rebalance_freq[:-1])
        return pd.offsets.MonthEnd(num)
    return rebalance_freq

def subtract_rf_from_df(df, ff3, date_col='date'):
    """
    df: 날짜와 수익률 데이터를 포함하는 DataFrame. 
        날짜 컬럼 이름은 기본적으로 'date'로 가정합니다.
    ff3: ff3 데이터프레임, 'date'와 'r_f' 컬럼을 포함해야 합니다.
    date_col: 날짜 컬럼의 이름 (기본값 'date').
    
    df의 모든 숫자형 수익률 컬럼(날짜 컬럼 제외)에서 ff3의 r_f 값을 해당 날짜에 맞게 차감합니다.
    """
    # 날짜 컬럼을 datetime으로 변환
    df[date_col] = pd.to_datetime(df[date_col])
    ff3['date'] = pd.to_datetime(ff3['date'])
    
    # ff3의 r_f 컬럼만 추출 후, 날짜 기준으로 병합
    merged = df.merge(ff3[[date_col, 'r_f']], on=date_col, how='left')
    
    # 날짜와 r_f를 제외한 모든 숫자형 컬럼에 대해 r_f를 차감
    numeric_cols = merged.select_dtypes(include='number').columns.tolist()
    # 만약 날짜 컬럼이 숫자형으로 인식될 경우, 제거
    if date_col in numeric_cols:
        numeric_cols.remove(date_col)
    if 'r_f' in numeric_cols:
        numeric_cols.remove('r_f')
        
    for col in numeric_cols:
        merged[col] = merged[col] - merged['r_f']
        
    # r_f 컬럼은 제거
    return merged.drop(columns='r_f')

#pre_index_excess  = subtract_rf_from_df(pre_index, ff3, date_col='date')
#post_index_excess = subtract_rf_from_df(post_index, ff3, date_col='date')
#post_ff_excess    = subtract_rf_from_df(post_ff, ff3, date_col='date')


# -----------------------------------------
# Split sample
# -----------------------------------------
def split_in_out_sample(df, in_end, in_sample_months=36, out_end=None):
    """
    주어진 in_end와 in_sample_months, 그리고 선택적으로 out_end를 이용해 
    in-sample과 out-of-sample 데이터를 분할합니다.
    
    Parameters:
      - df: 전체 데이터프레임 (반드시 'date' 컬럼이 있어야 함)
      - in_end: in-sample 종료일 (string 또는 datetime)
      - in_sample_months: in-sample 기간 (월 단위, default 36)
      - out_end: out-of-sample 종료일 (string 또는 datetime). None인 경우 in_end 이후 전체가 out-of-sample.
    
    Returns:
      - in_sample: [in_end - in_sample_months, in_end] 기간의 데이터프레임
      - out_sample: (in_end, out_end] 또는 in_end 이후 전체 데이터프레임
    """
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    in_end = pd.to_datetime(in_end)
    
    # in-sample 기간 계산
    in_start = in_end - pd.DateOffset(months=in_sample_months)
    in_sample = df[(df['date'] >= in_start) & (df['date'] <= in_end)].copy()
    
    # out-of-sample 기간 계산
    if out_end is not None:
        out_end = pd.to_datetime(out_end)
        out_sample = df[(df['date'] > in_end) & (df['date'] <= out_end)].copy()
    else:
        out_sample = df[df['date'] > in_end].copy()
    
    return in_sample, out_sample

# -----------------------------------------
# estimate_weights
# -----------------------------------------
def estimate_exponential_weights(df_in_sample, n=10, state=10):
    """
    Exponential model 기반으로 특정 state 내 상위 n개 종목의 rank → capshare 관계를 추정.
    
    Parameters:
    - df_in_sample: in-sample CRSP 데이터프레임
    - n: 각 시점에서 선택할 상위 종목 수
    - state: 분석 대상 percentile state (e.g., 10 = top 10%)

    Returns:
    - model_params: {'alpha': α, 'beta': β}
    - r_squared: 회귀 적합도
    """
    all_obs = []

    for date, group in df_in_sample[df_in_sample['state'] == state].groupby('date'):
        group = group.sort_values('mktcap_lag', ascending=False).head(n).copy()
        if len(group) < n:
            continue

        group = group.sort_values('mktcap_lag')  # 작은 순으로 정렬
        group['rank'] = np.arange(1, len(group) + 1)
        total_cap = group['mktcap_lag'].sum()
        group['capshare'] = group['mktcap_lag'] / total_cap
        group['log_capshare'] = np.log(group['capshare'])

        all_obs.append(group[['rank', 'log_capshare']])

    if not all_obs:
        raise ValueError("No valid observations for exponential regression.")

    df_all = pd.concat(all_obs, ignore_index=True)
    X = sm.add_constant(df_all['rank'])
    y = df_all['log_capshare']

    model = sm.OLS(y, X).fit()
    ln_alpha, beta = model.params
    alpha = np.exp(ln_alpha)

    return {'alpha': alpha, 'beta': beta}, model.rsquared

def estimate_quadratic_weights(df_in_sample, n=10, state=10):
    """
    Rolling in-sample 기간에 대해 top-n 종목에 대한 평균적인 
    (rank, capshare) 관계를 추정하여 quadratic weight 모델 생성
    """
    df = df_in_sample[df_in_sample['state'] == state].copy()

    # 각 날짜별로 상위 n개 선택
    top_n_list = []
    for date, group in df.groupby('date'):
        group = group.sort_values('mktcap_lag', ascending=False).head(n)
        if len(group) < n:
            continue
        group = group.sort_values('mktcap_lag')
        group['rank'] = np.arange(1, len(group) + 1)
        group['capshare'] = group['mktcap_lag'] / group['mktcap_lag'].sum()
        top_n_list.append(group[['permno', 'rank', 'capshare']])
    
    if not top_n_list:
        return None, None

    df_all = pd.concat(top_n_list)

    # 회귀 변수 생성
    df_all['rank_sq'] = df_all['rank'] ** 2
    X = sm.add_constant(df_all[['rank', 'rank_sq']])
    y = df_all['capshare']

    # 회귀 수행
    model = sm.OLS(y, X).fit()
    
    return model.params, model.rsquared

# -----------------------------------------
# construct_tbtf
# -----------------------------------------
def construct_tbtf_exponential(crsp_df, target_state, top_n, params):
    # construct_tbtf는 날짜별로 실행되며 내부에서 weight 추정 포함
    """
    주어진 날짜의 crsp snapshot에서 target_state에 해당하는 자산들 중 
    상위 top_n 자산을 선택한 후, exponential weighting 방식을 적용하여 
    포트폴리오의 초과수익률 (ret_excess)의 가중 평균을 계산합니다.
    
    Parameters:
    - crsp_df: 특정 날짜의 CRSP snapshot (DataFrame). 
               필수 컬럼: 'permno', 'mktcap_lag', 'ret_excess', 'state'
    - target_state: 선택할 state 값 (예: 10, 즉 top decile)
    - top_n: 선택할 자산 수. (예: 10, 20 등)
    - params: in-sample에서 추정된 exponential model 파라미터 (dict), 
              반드시 key 'beta'를 포함. 
              (예: params = {'alpha': value, 'beta': beta_value})
    
    Process:
    1. crsp_df에서 target_state (예: state=10)인 자산들을 필터링.
    2. mktcap_lag 기준 내림차순 정렬 후, 상위 top_n 자산을 선택.
    3. 선택된 자산들을 mktcap_lag 기준 오름차순으로 재정렬하여, 
       rank를 1부터 top_n까지 할당 (즉, 1 = smallest, top_n = largest).
    4. Exponential weighting: 
          predicted_weight = exp(beta * group_rank)
       그리고 이들을 정규화하여 합이 1이 되도록 조정.
    5. 각 자산의 ret_excess에 가중치를 곱해 가중 평균 포트폴리오 수익률 계산.
    
    Returns:
    - portfolio_return: 해당 시점의 포트폴리오 초과수익률 (scalar)
    - selected_df: DataFrame with columns ['permno', 'group_rank', 'predicted_weight']
                     (각 자산별 weight 및 순위 정보를 포함)
    """
    df = crsp_df.copy()
    # target state에 해당하는 자산들만 필터링
    df = df[df['state'] == target_state].copy()
    
    # 전체 그룹에서 mktcap_lag 기준 내림차순 정렬하여 상위 top_n 자산 선택
    df_desc = df.sort_values('mktcap_lag', ascending=False).reset_index(drop=True)
    selected = df_desc.head(top_n).copy()
    
    # 그룹 내에서, 재정렬: 오름차순으로 정렬하여 1 = smallest, top_n = largest로 rank 부여
    selected = selected.sort_values('mktcap_lag', ascending=True).reset_index(drop=True)
    selected['group_rank'] = np.arange(1, len(selected) + 1)
    
    # Exponential weighting: weight = exp(beta * group_rank)
    beta = params['beta']  # in-sample 추정된 exponential parameter (로그 선형 회귀의 slope)
    selected['predicted_weight'] = np.exp(beta * selected['group_rank'])
    
    # 정규화: 합이 1이 되도록
    selected['predicted_weight'] /= selected['predicted_weight'].sum()
    
    # 포트폴리오 수익률 계산: 가중 평균 ret_excess
    portfolio_return = (selected['predicted_weight'] * selected['ret_excess']).sum()
    
    return portfolio_return, selected[['permno', 'group_rank', 'predicted_weight']]

def construct_tbtf_quadratic(crsp_df, target_state, top_n, params):
    """
    주어진 날짜의 crsp snapshot에서 target_state (예: state=10)에 해당하는 자산들 중 
    상위 top_n 자산을 선택하고, in‐sample에서 추정된 quadratic 회귀 계수를 이용하여
    각 자산의 weight를 계산한 후, 포트폴리오 초과수익률(ret_excess)의 가중 평균을 구하는 함수.
    
    Parameters:
      - crsp_df: 특정 날짜의 CRSP snapshot (DataFrame)
                 필수 컬럼: 'permno', 'mktcap_lag', 'ret_excess', 'state'
      - target_state: 선택할 state 값 (예: 10, 즉 top decile)
      - top_n: 선택할 자산 수 (예: 10 또는 20 등)
      - params: in-sample에서 추정된 quadratic 모델의 계수 
                (dict with keys 'const', 'rank', 'rank_sq')
                
    Returns:
      - portfolio_return: 해당 날짜의 포트폴리오 초과수익률 (scalar)
      - selected_df: 각 자산별 정보를 담은 DataFrame (permno, group_rank, predicted_weight)
    
    Process:
      1. 전체 데이터에서 target_state에 해당하는 자산만 필터링.
      2. mktcap_lag 기준 내림차순으로 정렬하여 상위 top_n 종목 선택.
      3. 선택된 종목들을 mktcap_lag 기준 오름차순으로 재정렬하여, 
         1부터 top_n까지의 group_rank를 부여 (1 = smallest, top_n = largest).
      4. Quadratic 모형: weight = const + beta * group_rank + gamma * (group_rank)^2 로 계산.
      5. 음수 weight는 0으로 클리핑한 후, 전체 weight 합이 1이 되도록 정규화.
      6. 각 자산의 ret_excess에 weight를 곱해 가중 평균 포트폴리오 수익률 산출.
    """
    df = crsp_df.copy()
    # target_state에 해당하는 자산들만 필터링
    df = df[df['state'] == target_state].copy()
    
    # mktcap_lag 기준 내림차순으로 top_n 종목 선택
    df = df.sort_values('mktcap_lag', ascending=False).reset_index(drop=True)
    selected = df.head(top_n).copy()
    
    # 그룹 내에서 오름차순 정렬하여, 1 = smallest, top_n = largest로 rank 부여
    selected = selected.sort_values('mktcap_lag', ascending=True).reset_index(drop=True)
    selected['group_rank'] = np.arange(1, len(selected) + 1)

    # fallback 처리: params가 유효한 dict 또는 Series가 아닐 경우 fallback 값 사용
    try:
        const_ = params['const']
        beta = params['rank']
        gamma = params['rank_sq']
    except (IndexError, TypeError, KeyError):
        const_ = 0.07
        beta = 0
        gamma = 0.0015

    # Quadratic weighting: weight = const + beta * group_rank + gamma * group_rank^2
    selected['quad_weight'] = const_ + beta * selected['group_rank'] + gamma * (selected['group_rank'] ** 2)
    selected['quad_weight'] = selected['quad_weight'].clip(lower=0)
    
    # 정규화: sum(weight) = 1
    selected['predicted_weight'] = selected['quad_weight'] / selected['quad_weight'].sum()
    
    # 포트폴리오 초과수익률 계산: 가중 평균 ret_excess
    selected['weighted_ret'] = selected['predicted_weight'] * selected['ret_excess']
    portfolio_return = selected['weighted_ret'].sum()
    
    return portfolio_return, selected[['permno', 'group_rank', 'predicted_weight']]


# -----------------------------------------
# compute_return
# -----------------------------------------

def compute_return_tbtf(crsp, rebalance_dates, weighting_method='exponential', top_n=10, state=10, in_sample_months=36):
    """
    TBTF 전략의 out-of-sample 포트폴리오 수익률 계산 파이프라인.
    
    Parameters:
      - crsp: 전체 CRSP DataFrame (날짜, permno, mktcap, ret, mktcap_lag, ret_excess, state, state_lag 등 포함)
      - rebalance_dates: 리밸런싱 날짜 리스트 (datetime 형식, 오름차순)
      - weighting_method: 'exponential' 또는 'quadratic'
      - top_n: 각 리밸런싱 시점마다 선택할 자산 수
      - state: 대상 state (예: 10)
      - in_sample_months: in-sample 윈도우 (월 수)
    
    Returns:
      - returns_df: 각 리밸런싱 시점별 포트폴리오 초과수익률 시계열 DataFrame
      - weights_df: 각 리밸런싱 시점별 선택된 자산의 weight 정보 DataFrame
    """
    returns_list = []
    weights_list = []
    
    for i in range(len(rebalance_dates) - 1):
        current_date = rebalance_dates[i]
        next_date = rebalance_dates[i+1]
        
        # in-sample 데이터: current_date 이전 in_sample_months 기간
        in_start = current_date - pd.DateOffset(months=in_sample_months)
        in_sample = crsp[(crsp['date'] >= in_start) & (crsp['date'] <= current_date)].copy()
        
        # snapshot: 현재 리밸런싱 시점의 데이터 (target state만 필터링)
        snapshot = crsp[crsp['date'] == current_date].copy()
        snapshot_state = snapshot[snapshot['state'] == state].copy()
        
        # weighting method에 따라 파라미터 추정 및 포트폴리오 구성
        if weighting_method == 'exponential':
            # in-sample에서 exponential 모델 파라미터 추정
            params_exp, rsq_exp = estimate_exponential_weights(in_sample, n=top_n, state=state)
            # 현재 시점 snapshot에 대해 exponential weighting 적용
            port_ret, weight_detail = construct_tbtf_exponential(snapshot_state, target_state=state, top_n=top_n, params=params_exp)
        elif weighting_method == 'quadratic':
            # in-sample에서 quadratic 모델 파라미터 추정
            weight_table, params_quad = estimate_quadratic_weights(in_sample[in_sample['state'] == state], n=top_n)
            # 현재 시점 snapshot에 대해 quadratic weighting 적용
            port_ret, weight_detail = construct_tbtf_quadratic(snapshot_state, target_state=state, top_n=top_n, params=params_quad)
        else:
            raise ValueError("weighting_method must be 'exponential' or 'quadratic'")
        
        returns_list.append({'date': current_date, 'portfolio_return': port_ret})
        weight_detail = weight_detail.copy()
        weight_detail['date'] = current_date
        weights_list.append(weight_detail)
    
    returns_df = pd.DataFrame(returns_list).sort_values('date').reset_index(drop=True)
    weights_df = pd.concat(weights_list, ignore_index=True)
    return returns_df, weights_df

def compute_return_pfo(crsp, rebalance_dates, weighting_method='vw', top_n=10):
    """
    전통적 방식의 포트폴리오 수익률 계산 함수.
    각 리밸런싱 시점마다, 전체 crsp 데이터에서 
    mktcap_lag 기준 상위 top_n 자산을 선택한 후,
    weighting_method에 따라 포트폴리오 초과수익률(ret_excess)의 가중 평균을 계산합니다.
    
    Parameters:
      - crsp: 전체 CRSP DataFrame (필수 컬럼: 'date', 'permno', 'mktcap_lag', 'ret_excess')
      - rebalance_dates: 리밸런싱 기준 날짜 리스트 (datetime 형식, 오름차순)
      - weighting_method: 'vw' (value-weighted) 또는 'ew' (equal-weighted)
      - top_n: 각 리밸런싱 시점에서 선택할 자산 수
      
    Returns:
      - returns_df: 각 리밸런싱 시점별 포트폴리오 초과수익률 시계열 DataFrame
      - weights_df: 각 리밸런싱 시점별 선택된 자산의 weight 정보 DataFrame 
                    (permno, weight, date)
    """
    returns_list = []
    weights_list = []
    
    for i in range(len(rebalance_dates) - 1):
        current_date = rebalance_dates[i]
        next_date = rebalance_dates[i+1]
        
        # 현재 리밸런싱 시점의 snapshot 추출
        snapshot = crsp[crsp['date'] == current_date].copy()
        
        # 전체 데이터에서 mktcap_lag 기준 내림차순 정렬하여 상위 top_n 자산 선택
        snapshot = snapshot.sort_values('mktcap_lag', ascending=False).reset_index(drop=True)
        selected = snapshot.head(top_n).copy()
        
        if weighting_method.lower() == 'vw':
            total_cap = selected['mktcap_lag'].sum()
            selected['weight'] = selected['mktcap_lag'] / total_cap
        elif weighting_method.lower() == 'ew':
            selected['weight'] = 1 / len(selected)
        else:
            raise ValueError("weighting_method must be 'vw' or 'ew'")
        
        # 계산: 포트폴리오 수익률 = 가중 평균 ret_excess (리스크 프리 제외된 수익률)
        selected['weighted_ret'] = selected['weight'] * selected['ret_excess']
        port_ret = selected['weighted_ret'].sum()
        
        returns_list.append({'date': current_date, 'portfolio_return': port_ret})
        selected['date'] = current_date
        weights_list.append(selected[['permno', 'weight', 'date']])
    
    returns_df = pd.DataFrame(returns_list).sort_values('date').reset_index(drop=True)
    weights_df = pd.concat(weights_list, ignore_index=True)
    return returns_df, weights_df

# -----------------------------------------
# compute_turnover
# -----------------------------------------

def compute_turnover(weights_df, rebalance_dates):
    """
    각 리밸런싱 시점별로 포트폴리오 weight 변화(turnover)를 계산하고,
    t 시점의 weight 정보를 기준으로, 
    최대 상승(positive diff) 및 최대 하락(negative diff) asset의 permno와 
    해당 자산의 group_rank (존재하는 경우)를 기록합니다.
    
    Parameters:
      - weights_df: 리밸런싱 시점별 자산별 weight 정보 DataFrame.
          필수 컬럼: 'date', 'permno'
          TBTF 전략인 경우: 'predicted_weight'와 'group_rank'가 포함되어 있음.
          전통적 방식의 경우: 'weight' 컬럼만 포함.
      - rebalance_dates: 리밸런싱 날짜 리스트 (datetime 형식, 오름차순)
      
    Returns:
      - turnover_df: 각 리밸런싱 시점(t+1)에 대해 아래의 순서로 기록:
          rebalance_date, turnover, max_diff, min_diff,
          max_diff_permno, min_diff_permno,
          max_diff_group_rank, min_diff_group_rank
    """
    turnover_records = []
    
    # 사용할 weight 컬럼 결정: predicted_weight가 있으면 사용, 없으면 weight
    col_name = 'predicted_weight' if 'predicted_weight' in weights_df.columns else 'weight'
    
    for i in range(len(rebalance_dates) - 1):
        date_t = rebalance_dates[i]
        date_tp1 = rebalance_dates[i+1]
        
        # t 시점의 weight 정보 (group_rank 포함 여부 확인)
        wt_t = weights_df[weights_df['date'] == date_t][['permno', col_name]]
        if 'group_rank' in weights_df.columns:
            wt_t = wt_t.merge(weights_df[weights_df['date'] == date_t][['permno', 'group_rank']], on='permno', how='left')
        else:
            wt_t['group_rank'] = np.nan
        wt_t = wt_t.set_index('permno')
        
        # t+1 시점의 weight 정보 (group_rank는 t 시점의 값을 사용)
        wt_tp1 = weights_df[weights_df['date'] == date_tp1][['permno', col_name]].set_index('permno')
        
        # 두 시점 모두에 대해 outer join: 없는 경우 0 처리
        all_permnos = wt_t.index.union(wt_tp1.index)
        wt_t = wt_t.reindex(all_permnos, fill_value=0)
        wt_tp1 = wt_tp1.reindex(all_permnos, fill_value=0)
        
        # weight 차이 계산: t+1 - t
        diff = wt_tp1[col_name] - wt_t[col_name]
        diff = diff.dropna()
        turnover = np.abs(diff).sum()
        
        # 최대 상승(positive diff) 및 최대 하락(negative diff)
        if not diff.empty:
            max_diff_value = diff.max()
            max_diff_permno = diff.idxmax()
            min_diff_value = diff.min()
            min_diff_permno = diff.idxmin()
        else:
            max_diff_value = min_diff_value = np.nan
            max_diff_permno = min_diff_permno = None
        
        # t 시점의 group_rank 정보 (존재하는 경우만)
        max_diff_group_rank = wt_t.loc[max_diff_permno, 'group_rank'] if (max_diff_permno is not None and not pd.isna(wt_t.loc[max_diff_permno, 'group_rank'])) else np.nan
        min_diff_group_rank = wt_t.loc[min_diff_permno, 'group_rank'] if (min_diff_permno is not None and not pd.isna(wt_t.loc[min_diff_permno, 'group_rank'])) else np.nan
        
        record = {
            'rebalance_date': date_tp1,
            'turnover': turnover,
            'max_diff': max_diff_value,
            'min_diff': min_diff_value,
            'max_diff_permno': max_diff_permno,
            'min_diff_permno': min_diff_permno,
            'max_diff_group_rank': max_diff_group_rank,
            'min_diff_group_rank': min_diff_group_rank
        }
        turnover_records.append(record)
    
    turnover_df = pd.DataFrame(turnover_records)[['rebalance_date', 'turnover', 'max_diff', 'min_diff',
                                                    'max_diff_permno', 'min_diff_permno',
                                                    'max_diff_group_rank', 'min_diff_group_rank']]
    return turnover_df


# -----------------------------------------
# Evaluate performance of a return series
# -----------------------------------------
def evaluate_performance(returns, eta=3, p=0.01, periods_per_year=12):
    """
    주어진 초과수익률(returns) 시계열에 대해 다양한 성과 지표를 계산합니다.
    returns는 이미 risk-free rate이 차감된 초과수익률(ret_excess) 시계열이라고 가정합니다.
    
    Parameters:
      - returns: pandas Series 또는 numpy array 형태의 초과수익률
      - eta: CRRA 계수 (default: 3)
      - p: Omega ratio 계산 시 기준 수익률 threshold (default: 0.01)
      - periods_per_year: 연간 관측 기간 수 (예: 월간이면 12, 6M이면 2, 연간이면 1)
      
    Returns:
      - metrics: dict 형태로 각 성과 지표를 반환
    """
    def ann_return(r):
        return (1 + r).prod()**(periods_per_year / len(r)) - 1

    def ann_vol(r):
        return r.std() * np.sqrt(periods_per_year)

    def sharpe(r):
        return r.mean() / r.std() * np.sqrt(periods_per_year)

    def sortino(r):
        downside = r[r < 0]
        # 만약 downside의 표준편차가 0인 경우, 평균이 양수면 무한대로 처리
        if downside.std() > 0:
            return r.mean() / downside.std() * np.sqrt(periods_per_year)
        else:
            return np.inf if r.mean() > 0 else 0

    def omega(r):
        gains = r[r > p] - p
        losses = p - r[r < p]
        return gains.sum() / losses.sum() if losses.sum() > 0 else np.nan

    def max_dd(r):
        cum = (1 + r).cumprod()
        dd = (cum - cum.cummax()) / cum.cummax()
        return dd.min()

    def calmar(r):
        a = ann_return(r)
        m = max_dd(r)
        return a / abs(m) if m < 0 else np.nan

    def expected_crra(r):
        x = 1 + r
        if eta == 1:
            return np.log(x).mean()
        else:
            return ((x**(1 - eta) - 1) / (1 - eta)).mean()

    def fisher_skew(r):
        return skew(r, bias=False)

    def pearson_skew(r):
        mu, med, std = r.mean(), r.median(), r.std()
        return 3 * (mu - med) / std if std > 0 else np.nan

    def ex_kurt(r):
        return kurtosis(r, fisher=True, bias=False)

    metrics = {
        'Annualized Return': ann_return(returns),
        'Annualized Volatility': ann_vol(returns),
        'Sharpe Ratio': sharpe(returns),
        'Sortino Ratio': sortino(returns),
        'Omega Ratio': omega(returns),
        'Max Drawdown': max_dd(returns),
        'Calmar Ratio': calmar(returns),
        'Expected CRRA': expected_crra(returns),
        'Fisher Skewness': fisher_skew(returns),
        'Pearson Skewness': pearson_skew(returns),
        'Excess Kurtosis': ex_kurt(returns),
    }
    return metrics

# 예시 사용:
# 만약 재조정 주기가 '6M'이면, periods_per_year=2, '12M'이면 1, '1M'이면 12 등을 전달.
# 예: monthly returns 시, evaluate_performance(returns, periods_per_year=12)



# -----------------------------------------
# backtest_pipeline
# -----------------------------------------

def backtest_pipeline(crsp, in_end, out_end, in_sample_months, rebalance_freq,
                       weighting_method, top_n, state, eta, p):
    """
    전체 백테스트 파이프라인 함수.
    
    Parameters:
      - crsp: 전체 CRSP DataFrame. 필수 컬럼: 
              'date', 'permno', 'mktcap', 'ret', 'mktcap_lag', 'ret_excess', 'state', 'state_lag'
      - in_end: in-sample 기간의 마지막 날짜 (string, e.g., '2010-12-31')
      - out_end: out-of-sample 기간의 마지막 날짜 (string, e.g., '2015-12-31')
      - in_sample_months: in-sample 윈도우 (월 수, 예: 36)
      - rebalance_freq: 리밸런싱 주기 (string, e.g., '1M', '3M', '6M', '12M')
      - weighting_method: 'exponential', 'quadratic', 'value', 'equal'
      - top_n: 각 리밸런싱 시점마다 선택할 자산 수
      - state: TBTF 방식에 사용될 target state (예: 10). 전통적 방식에서는 무시됨.
      - eta: performance 평가에 사용할 CRRA 계수
      - p: Omega ratio 계산을 위한 threshold
      
    Returns:
      A dictionary with:
        - 'returns': DataFrame, 각 리밸런싱 시점별 포트폴리오 초과수익률
        - 'weights': DataFrame, 각 리밸런싱 시점별 자산별 weight 정보
        - 'performance': dict, 전체 포트폴리오 수익률에 대한 성과 지표 (evaluate_performance 결과)
        - 'turnover': DataFrame, 각 리밸런싱 시점별 turnover 정보
        - 'rebalance_dates': 리밸런싱 날짜 리스트 used
    """
    import pandas as pd
    import numpy as np

    print("[START] backtest_pipeline 호출됨")

    # 1. 기간 정의
    in_sample_start = pd.to_datetime(in_end) - pd.DateOffset(months=in_sample_months)
    in_sample = crsp[(crsp['date'] >= in_sample_start) & (crsp['date'] <= pd.to_datetime(out_end))]
    out_sample = crsp[(crsp['date'] > pd.to_datetime(in_end)) & (crsp['date'] <= pd.to_datetime(out_end))]

    print(f"[INFO] In-sample: {in_sample['date'].min()} to {in_sample['date'].max()}")
    print(f"[INFO] Out-of-sample: {out_sample['date'].min()} to {out_sample['date'].max()}")

    # 2. 리밸런싱 날짜 생성
    try:
        rebalance_dates = pd.date_range(
            start=pd.to_datetime(in_end) + pd.offsets.Day(1),
            end=pd.to_datetime(out_end),
            freq=get_rebalance_offset(rebalance_freq)
        )
    except Exception as e:
        print(f"[ERROR] rebalance_dates 생성 실패: {e}")
        raise

    # print(f"[INFO] Rebalance dates ({len(rebalance_dates)}): {rebalance_dates[:5].tolist()}...")

    returns_list = []
    weights_list = []

    for i in range(len(rebalance_dates) - 1):
        current_date = rebalance_dates[i]
        
        # print(f"[LOOP] current_date = {current_date.date()}")

        snapshot = out_sample[out_sample['date'] == current_date].copy()

        if weighting_method.lower() in ['exponential', 'quadratic']:
            snapshot_state = snapshot[snapshot['state'] == state].copy()

            in_window_start = current_date - pd.DateOffset(months=in_sample_months)
            current_in_sample = in_sample[(in_sample['date'] >= in_window_start) & (in_sample['date'] <= current_date)]
            current_in_sample_state = current_in_sample[current_in_sample['state'] == state].copy()

            # print(f"\t[snapshot_state] {len(snapshot_state)} rows | [in_sample_state] {len(current_in_sample_state)} rows")

            if snapshot_state.empty or current_in_sample_state.empty:
                print(f"\t[SKIP] {current_date.date()} - insufficient data")
                continue

            if weighting_method.lower() == 'exponential':
                params, rsq = estimate_exponential_weights(current_in_sample_state, n=top_n, state=state)
                port_ret, weight_detail = construct_tbtf_exponential(snapshot_state, target_state=state, top_n=top_n, params=params)
            else:
                weight_table, params_quad = estimate_quadratic_weights(current_in_sample_state, n=top_n)
                port_ret, weight_detail = construct_tbtf_quadratic(snapshot_state, target_state=state, top_n=top_n, params=params_quad)

        elif weighting_method.lower() in ['value', 'equal']:
            snapshot = snapshot.sort_values('mktcap_lag', ascending=False).reset_index(drop=True)
            selected = snapshot.head(top_n).copy()

            if len(selected) < top_n:
                print(f"\t[SKIP] {current_date.date()} - fewer than top_n stocks")
                continue

            if weighting_method.lower() == 'value':
                total_cap = selected['mktcap_lag'].sum()
                selected['weight'] = selected['mktcap_lag'] / total_cap
            else:
                selected['weight'] = 1 / len(selected)

            selected['weighted_ret'] = selected['ret_excess'] * selected['weight']
            port_ret = selected['weighted_ret'].sum()
            weight_detail = selected[['permno', 'weight']].rename(columns={'weight': 'predicted_weight'})
            weight_detail['group_rank'] = np.nan

        else:
            raise ValueError("Unsupported weighting_method")

        returns_list.append({'date': current_date, 'portfolio_return': port_ret})
        weight_detail['date'] = current_date
        weights_list.append(weight_detail)

    returns_df = pd.DataFrame(returns_list).sort_values('date').reset_index(drop=True)
    weights_df = pd.concat(weights_list, ignore_index=True)

    freq_upper = rebalance_freq.upper()
    num_months = int(''.join(filter(str.isdigit, freq_upper)))
    periods_per_year = int(12 / num_months)
    performance = evaluate_performance(returns_df['portfolio_return'], eta=eta, p=p, periods_per_year=periods_per_year)
    turnover = compute_turnover(weights_df, rebalance_dates)

    print(f"[DONE] Total returns recorded: {len(returns_df)}")
    return {
        'returns': returns_df,
        'weights': weights_df,
        'performance': performance,
        'turnover': turnover,
        'rebalance_dates': rebalance_dates
    }


