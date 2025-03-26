---
title: hello
subtitle: world
author: gitSAM
date: '2025-03-19'
abstract: This study 
bibliography: references.bib
format:
  html:
    code-fold: true
    toc: true
    number-sections: true
jupyter: python3
---

- 철학과 함께하는 해석학
  - 대수학과 기하학을 해석하는 해석학 
  - 확률 최적화 이론 및 미적분을 사용하는 해석학 
  - LLM(대규모 언어 모델) 개발을 위한 해석학

```{python}

```

permno-tic-2021

https://www.ivo-welch.info/research/betas/header.html




먼저, 나같이 육하원칙에 맞춰서 투자전략을 생각하는게 '일반적'인가? 연구에서나 실무에서나 육하원칙에 맞춰서 간단하게 설명하는게 보통인가?

그리고, 다음 부분을 좀더 구체적으로 분석해서 위의 부분을 수정하자.
- Adjusted for survivorship bias and delisting bias: 먼저 일반적인 논문들에서는 어떻게 처리하는지? 설마 NaN을 remove하는 방식인가? 내가 생각한 방향은, listing에서 빠진 asset이나 listing으로 들어오는 asset을 하나의 external group으로 묶는 방식이었어. 예를 들어 listed asset을 decile로 나누었을때, external group은 11-th state이 되는 방식이었어. 이렇게 하면 transition matrix를 추적할 수 있을 것 같았어. 한편, delisted asset의 net return 은 -1 즉 gross return은 0으로 처리할 생각이었지. 
- Compare TBTF portfolio vs:
  - Pre-2010: 
    - DJIA, 
    - NDX,
    - 2 Fama-French Research Portfolios(Value-weighted size and prior earning momentum): ME 5 PRIOR 4, ME 4 PRIOR 3
  - Post-2010: 
    - DIA (ETF version of DJIA, State Street Corporation ETF. Fund inception: 1998/01/14), 
    - QQQ (ETF version of NDX. Nasdaq-100 ticker. the Invesco QQQ Trust. Fund inception: 1999/03/10), 
    - SPY (The SPDR S&P 500 ETF, Fund inception: 1993/01/22), 
    - VTI (Vanguard Total Stock Market ETF, Fund inception: 2001년 5월 24일), 
- Use Pre-2010 period to estimate weights, apply to Post-2010 and compare:
  - Use prior 4 year in Pre-2010 period: Use 1996-1999 period as in-sample. Then out-of-sample is 10 years 2000-2009
  - Same: Use 2010-2013 as in-sample. Then out-of-sample is 10 years 2014-2023
  - 일반적으로는 in-sample learning period가 out-of-sample testing period보다 훨씬 긴 것으로 알고 있는데, 이렇게 해서도 TBTF의 performance가 좋았다면 단지 운인가? 아니면 이러한 period도 나눠가면서 robustness check을 할까?
  

## 논문 제목 (제안)

**"Too Big to Transition? Capital Lock-In and Structural Dominance in Post-2010 US Equity Markets"**  
_Subtitle_: Evidence from CRSP on Capital Flow Persistence and Distributional Distortion


## 논문 개요 요약

**핵심 아이디어**:  
- 시가총액 기준 상위 그룹 (top 10, 20 등)은 자본을 지속적으로 lock-in하며, 그 그룹 내에서 자본이 순환하고 있음  
- TBTF 전략의 성과는 단순히 mean-return이 아니라, **transition asymmetry와 volatility trap**에 기인  
- 기존 AR(1)-based equilibrium 모형은 symmetric transition과 uniform stationary dist.를 암묵적으로 전제함 → 현실은 그 반대


## 전체 논문 구조 (이론적 기반 + 실증 구조 통합)

### **1. Introduction**

- 기존 자산시장 모형의 symmetric transition matrix assumption 소개
- 실제 주식시장에서는 **시가총액 기반 계층 구조**가 존재
- 이 논문은 **CRSP 데이터를 기반으로 자본의 lock-in 현상을 마르코프 전이 구조로 분석**하고자 함
- TBTF 전략은 단순히 리스크 조정 성과가 아니라, **자본의 구조적 편향(flow asymmetry)**에 기반함

---

### **2. Theoretical Motivation: Why Transition Structure Matters**

2. Theoretical Framework: Beyond Linear Risk-Reward (2–3 pages)

마르코프 체인 가정 적용.

2.1 implitic symmetry in Linear Models vs. asymmetry in real world
- Fama-French 3/5-factor 계열 선형모형들에 공통적인 white noise 가정. error term은 normal distribution. 누가 normal이라고 했는가?
- AR(1)에서 persistence parameter와 correlation coefficient의 관계: Tauchen-style 이산화 → symmetric, doubly stochastic → uniform stationary distribution
- 핵심 주장: 자본 시장은 계층적이며, risk-reward는 비선형적임.

2.2 Irreducible vs. Reducible Capital Lock-In
- $P_{11} \gg P_{1j}$ (상위 10%의 잔류 확률 극대화). **Top-quantile 주식군의 상태는 absorbing state에 가까움**
- 이런 구조에서는 upward mobility는 rare, downward는 asymmetric한 조건부 확률을 가짐
- 현실 자본 시장은 lock-in 구조 현실은 상위 종목의 자본 흡수(absorbing state). 그리고 이는 자본흐름의 비가역적(irreversible) 구조를 암시.
- 수학적 정의: absorbing state의 조건과 비대칭 전이 행렬의 특성(증명은 부록 참조).

---

### **3. Empirical Design: Capital Transition and Distributional Asymmetry**

#### 3.1 Data

- CRSP universe (NYSE/Nasdaq/AMEX), monthly data 1996–2024
- 2010을 기준으로 pre-2010 14년과, post-2010 14년을 비교. 2010을 잠재적 structural break point로 가정함.
- 시가총액 기준으로 매년 **rank percentile (e.g., 0–10%, 10–20%, ...)** 그룹 설정
- 각 시점에서 **stock-level capital amount**는 시가총액으로 간주

#### 3.2 Quantile-Based Transition Matrix

- 매년 각 stock의 rank percentile을 기록하여 panel 생성
- 각 구간(예: 10% 단위) 간의 자본 흐름을 **금액(capital-weighted count)**으로 측정  
- transition matrix: $P_{ij} = \text{Pr}(q_t = i \rightarrow q_{t+1} = j)$  
- focus: 상위 10%에서의 $P_{11} \gg P_{1j}$ (for $j \ne 1$)

#### 3.3 Stochastic Dominance and Volatility Structure

- **Big stocks vs. Small stocks**:
  - 비슷한 평균 수익률 (mean)
  - 더 낮은 volatility → 2nd-order stochastic dominance
  - 수익률 분포의 **negative skewness** 차이 비교
  - asymmetry가 tail risk 회피를 초래하고 있음

---

### **4. Main Findings: Capital Lock-In and Transition Asymmetry**

#### 4.1 Transition Matrix Results

- top 10% group: diagonal entry (P11) 매우 높음, outflow 희박
- lower quantile 그룹: diagonal 작고, 상위 그룹으로의 이동은 낮은 확률

→ **Markov chain이 irreducible하지 않음**, absorbing-like behavior 존재

#### 4.2 Lock-In Duration and Membership Stability

- top-10에 진입한 주식의 평균 lock-in duration 계산  
- 중위권의 전이는 자주 발생하지만, 상위권의 composition은 거의 고정

#### 4.3 Distributional Shape Differences

- Big vs. Small stock return distributions:
  - Same mean
  - Higher variance, higher kurtosis in small stocks
  - Skewness 구조 비교

→ 수익률 분포만 보면 **비대칭적인 risk-return profile**이 존재

### Appendix

- 전체 10×10 transition matrix heatmap  
- lock-in duration histogram  
- skewness by quantile return plot  
- stochastic dominance plot  
- stationary distribution estimation

---

## 코드 템플릿 및 시각화 방향

- **transition matrix**: stock-level panel에서 매년 rank percentile 계산 후 group-by  
- **lock-in duration**: 상위 quantile 내 잔류 기간 카운팅  
- **capital-weighted flow**: 각 cell의 전이 확률이 아니라 자본총량 기준  
- **ridge plot**: quantile별 수익률 분포 시각화 (skewness, kurtosis 비교)

---

---

### **5. Theoretical Implications: Mispricing, Moat, and TBTF Strategy**

- TBTF 전략은 mean-variance로 설명되지 않음  
- 사실상 자본이 흡수되는 “모트(moat)” 현상에 기반  
- 구조적 misallocation, 계층 고착적 자본 배분 문제  
- 마치 사회 계층처럼 **시장 내 자본의 percentile lock-in 구조**가 형성됨

---

### **6. Conclusion**

- 시가총액 기반 자본 전이는 symmetric하지 않으며,  
- 현실 자본시장은 **mixture structure + transition asymmetry**가 본질임  
- TBTF 전략은 그 구조적 lock-in을 추적하는 것이며, “sadly optimal”한 선택임

---



필요하시면 이 구조에 따라 CRSP 패널 정리용 Python notebook 템플릿, 그리고 transition matrix + stationary distribution 시각화 도구도 도와드릴 수 있습니다. 이 구조는 금융시장의 "구조적 불균형"을 정량적으로 밝히는 논문으로서 **RFS, JFE, RED, 또는 AER의 경제/금융의 경계지점에 제출 가능**한 강한 기여를 가집니다.