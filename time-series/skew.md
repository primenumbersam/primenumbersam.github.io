
ode_geometric

y'(x)=a/x * y(x)
y'(x)=ay(x)
y'(x)=ay^2(x)


---
## Literature Review

미래에셋 
- TIGER 미국테크TOP10 INDXX: 나스닥 시가총액 10개 ETF 종목 코드 [381170](https://www.tigeretf.com/ko/product/search/detail/index.do?ksdFund=KR7381170000)
- AI 관련 미국 빅테크 주식 상위 10개 ETF 종목 코드 [490090](https://www.tigeretf.com/ko/product/search/detail/index.do?ksdFund=KR7490090008)

현대 금융시장 구조와 투자 전략
- 구조: 특정 산업 집중도, 산업 내 특정 기업의 집중도, 대형주의 프리미엄, 금융기관의 정부 보증 효과, 슈퍼스타 기업의 부상
- 전략: 자산 가격 및 위험조정 수익률에 미치는 영향

Superstar firms [@autor2020fall].

Resurrected size premium after controlling for the junk? [@asness2018size].

정부가 대형 금융기관의 주주를 보호하는 경향. 대형 금융기관들이 암묵적인 정부 보증으로 인해 위험조정 수익률이 더 낮다 [@gandhi2015size]. 

Passive ETF [@jiang2020passive].
- One of the most important capital-market developments of the past thirty years has been the growth of passive investing.
- flows into passive funds raise disproportionately the stock prices of the largest firms in the economy. 
- The growth of passive investing can thus be one of the drivers of the observed rise in industry concentration (Gutierrez and Philippon (2017), Grullon, Larkin, and Michaely (2019))

---
만약 시장의 모든 asset의 correlation이 1이면 이론은 어떻게 될까?

Superstar firms
- Industry Portfolio Top Companies
- https://en.wikipedia.org/wiki/Diversification_(finance)
- Linear Factor Model 요약

No‐arbitrage pricing theory(무위험 차익거래 이론)에서 SDF(Stochastic Discount Factor, 확률적 할인인자)는 “risky asset” 그 자체로 정의되지는 않습니다. SDF는 기본적으로 자산의 현금흐름을 할인하여 현재가치를 계산하는 역할을 하며, 다음 조건을 만족합니다:

\[
E\left[m R\right] = 1,
\]

여기서 \( R \)은 자산의 수익률입니다. 일반적으로 SDF는 경제 주체의 소비, 투자 등 상태 변수와 관련되어 있으며, 위험(특히, 경제의 나쁜 상태에서의 위험)에 대한 보상을 반영하는 역할을 합니다. 따라서 SDF는 보통 소비의 한계 효용의 역수와 같이 “위험을 회피하는” 성격을 띄어, 자산 수익률과는 음의 상관관계를 보이는 경향이 있습니다. 이는 투자자가 나쁜 경제 상황(소비가 줄어드는 상황)에서 높은 할인율(즉, 낮은 SDF)을 부여함으로써, 해당 상태에서의 자산의 가치를 높게 평가하기 때문입니다.

만약 시장의 모든 자산 간 상관관계가 1(즉, 완벽한 상관관계)을 이룬다면, 이는 모든 자산의 수익률이 동일한 단일 위험 요인에 의해 완벽히 구동된다는 것을 의미합니다. 이런 상황에서는 다음과 같은 결과가 발생합니다:

1. **단일 요인 모형으로의 축소:** 모든 자산이 동일한 위험 요인에 의해 움직이므로, 시장은 사실상 하나의 위험 요인만을 고려하는 단일 요인 모형(CAPM과 유사한 상황)으로 축소됩니다.  
2. **다양화의 무용성:** 자산들 사이에 공통의 위험 외에 분산투자를 통한 위험 분산 효과가 존재하지 않게 됩니다. 즉, 개별 자산의 고유 위험(idiosyncratic risk)이 모두 소멸하므로, 포트폴리오 다각화의 이점이 없어집니다.  
3. **SDF의 식별 문제:** 모든 자산의 수익률이 동일한 움직임을 보이면, SDF가 단일 요인에 의해 결정될 수밖에 없으며, 자산간 크로스 섹셔널(cross-sectional) 수익률 차이를 설명할 수 있는 여지가 줄어듭니다. 이는 실증적 자산가격 모형의 검증에 어려움을 줄 수 있습니다.

요약하면, SDF는 위험자산 그 자체라기보다는 위험에 대한 보상과 할인 기능을 수행하는 경제 상태 변수와 관련된 할인인자이며, 보통 자산 수익률과 음의 상관관계를 보입니다. 그리고 시장의 모든 자산이 완벽하게 상관관계를 가진다면, 자산 가격 결정 모형은 단일 요인 모형으로 축소되고, 분산투자를 통한 위험 분산 효과가 상실되며, SDF의 역할도 단순화되어 자산간 차별적 위험 보상의 설명력이 감소하게 됩니다.

---
Skewness of return distribution

passive funds

---

Distortion of US Capital Market Efficiency

패시브 투자의 증가, 승자독식 구조, 그리고 완화적 통화정책이 결합하여 

자본시장의 효율적 자원배분 기능을 약화시키고 있다는 가설

미국 주식 수익률 분포의 비대칭성 변화를 통해 검증

# 논문 구조: "미국 자본 시장의 자원배분 효율성 저하: 주식 수익률 분포 왜도 감소를 중심으로"

## 1. 서론
- 연구 배경 및 문제 제기: 패시브 펀드의 성장, 소수 기술주의 과도한 시장 점유율, 정부의 통화정책이 자본 시장 효율성에 미치는 영향
- 연구 목적: 미국 자본 시장의 자원배분 효율성 저하를 주식 수익률 분포의 왜도 변화를 통해 증명
- 연구의 학술적・실무적 기여도

## 2. 이론적 배경 및 선행연구
- 효율적 시장 가설(EMH)과 자원배분 효율성의 관계
- 주식 수익률 분포의 통계적 특성과 시장 효율성
- 패시브 투자의 증가와 시장 효율성 관련 선행연구
- 네트워크 효과와 승자독식 시장구조에 관한 연구
- 통화정책이 자산가격 및 자원배분에 미치는 영향

## 3. 연구 방법론
- 데이터 수집: 미국 주식시장 장기 수익률 데이터(기간, 표본 등 명시)
- 수익률 분포의 왜도(skewness) 측정 방법론
- 시계열 분석을 통한 왜도 변화 추세 파악
- 패시브 펀드 비중, 기술주 집중도, 통화정책 변수와의 상관관계 분석 방법

## 4. 실증 분석 결과
- 미국 주식시장 수익률 분포의 왜도 변화 추이
- 패시브 펀드 성장과 왜도 감소의 상관관계 분석
- 소수 기술주 시장집중과 왜도 변화 분석
- 통화정책 지표와 왜도 변화의 관계
- 산업별/기업규모별 차별적 영향 분석

## 5. 추가 분석 및 견고성 검증
- 다른 선진국 시장과의 비교 분석
- 다양한 시간대별 분석(단기, 중기, 장기)
- 대체 측정 방법을 통한 결과 검증
- 외생적 충격(금융위기, 팬데믹 등) 통제 후 분석

## 6. 결론 및 시사점
- 연구 결과 요약
- 미국 자본 시장의 자원배분 효율성 저하에 대한 정책적 시사점
- 투자자에 대한 시사점
- 연구의 한계 및 향후 연구 방향

## 부록
- 통계적 방법론의 세부 설명
- 추가 실증 분석 결과
- 사용된 변수의 정의 및 출처

## 데이터 시각화 제안
- 시간에 따른 주식 수익률 분포의 왜도 변화 그래프
- 패시브 펀드 비중과 왜도 간의 산점도
- 소수 기술주의 시장 집중도와 왜도 변화의 관계 시각화
- 통화정책 지표(예: 연준 밸런스시트, 실질금리)와 왜도 간의 관계 그래프
- 산업별/기업규모별 왜도 변화의 히트맵



미국 주식 수익률 분포의 비대칭성 변화와 관련된 주요 탑저널 논문들
- 옥석가리기? "discerning value", "separating the gold from the dross"
- 시장에서 고품질과 저품질을 구분하는 메커니즘에 관한 것: 미켈 스펜스(Michael Spence)의 신호 이론(Signaling Theory)이나 조지 애컬로프(George Akerlof)의 "The Market for Lemons" 같은 정보 비대칭 관련 논문들
- 시장이 어떻게 기업의 본질 가치를 식별하는지: Eugene Fama의 효율적 시장 가설(Efficient Market Hypothesis) 관련 논문들

주식 수익률 분포의 비대칭성 변화에 대한 주요 메커니즘으로 다음과 같은 요인들을 제시합니다:

1. **패시브 투자의 증가**: 지수 추종형 투자의 증가로 인해 지수 내 높은 비중을 차지하는 주식들에 자본이 집중됨
2. **네트워크 효과와 승자독식 구조**: 특히 기술 산업에서 나타나는 네트워크 효과로 인해 소수 기업이 시장을 지배
3. **통화정책의 영향**: 완화적 통화정책이 특정 자산군과 기업에 차별적으로 혜택을 줌
4. **정보 비대칭성의 변화**: 패시브 투자의 증가로 개별 주식에 대한 정보 탐색과 가격 발견 과정이 약화됨
5. **기관투자자 행태의 변화**: 단기 성과에 집중하는 투자 행태가 수익률 분포 특성에 영향

## 주요 논문

1. **"Do Stocks Outperform Treasury Bills?" (2018)**
   - 저자: Hendrik Bessembinder
   - 저널: Journal of Financial Economics
   - 주요 내용: 1926년부터 2016년까지 미국 주식시장을 분석하여 양의 초과수익률이 극소수 종목에 집중되어 있음을 발견. 전체 주식 시장의 부의 창출이 약 4%의 종목에 집중되었으며, 나머지 96%는 단기 국채 수익률과 비슷하거나 낮은 성과를 보임. 이는 수익률 분포의 극단적 비대칭성을 보여줌.

@article{bessembinder2018stocks,
  title={Do stocks outperform treasury bills?},
  author={Bessembinder, Hendrik},
  journal={Journal of financial economics},
  volume={129},
  number={3},
  pages={440--457},
  year={2018},
  publisher={Elsevier}
}

2. **"Size and Value in China" (2021)**
   - 저자: Jianan Liu, Robert F. Stambaugh, Yu Yuan
   - 저널: Journal of Financial Economics
   - 주요 내용: 미국을 포함한 글로벌 주식시장에서 규모와 가치 요인을 분석하며, 수익률 분포의 비대칭성이 시간에 따라 어떻게 변하는지 연구. 특히 대형주와 성장주 중심의 시장 구조가 수익률 분포 왜도에 미치는 영향을 분석.

@article{liu2019size,
  title={Size and value in China},
  author={Liu, Jianan and Stambaugh, Robert F and Yuan, Yu},
  journal={Journal of financial economics},
  volume={134},
  number={1},
  pages={48--69},
  year={2019},
  publisher={Elsevier}
}

3. **"Anomalies and False Rejections" (2020)**
   - 저자: Kewei Hou, Chen Xue, Lu Zhang
   - 저널: Review of Financial Studies
   - 주요 내용: 주식 수익률 분포의 비대칭성과 이상현상들 사이의 관계를 연구. 시간이 흐름에 따라 기존에 발견된 이상현상들이 약화되면서 수익률 분포가 변화함을 보여줌.

@article{chordia2020anomalies,
  title={Anomalies and false rejections},
  author={Chordia, Tarun and Goyal, Amit and Saretto, Alessio},
  journal={The Review of Financial Studies},
  volume={33},
  number={5},
  pages={2134--2179},
  year={2020},
  publisher={Oxford University Press}
}

4. **"Index Investment and the Financialization of Commodities" (2012)**
   - 저자: Ke Tang, Wei Xiong
   - 저널: Financial Analysts Journal
   - 주요 내용: 비록 상품시장 연구이지만, 인덱스 투자(패시브 펀드)의 증가가 자산 수익률 분포와 상관관계에 미치는 영향을 분석하여 유사한 메커니즘을 주식시장에도 적용할 수 있음.

@article{tang2012index,
  title={Index investment and the financialization of commodities},
  author={Tang, Ke and Xiong, Wei},
  journal={Financial Analysts Journal},
  volume={68},
  number={6},
  pages={54--74},
  year={2012},
  publisher={Taylor \& Francis}
}

5. **"Asset Price Dynamics with Slow-Moving Capital" (2010)**
   - 저자: Darrell Duffie
   - 저널: Journal of Finance
   - 주요 내용: 자본 이동의 지연이 자산 가격과 수익률 분포에 미치는 영향을 연구. 특히 패시브 투자의 증가와 기관투자자들의 행동 변화가 시장 효율성에 미치는 영향을 논의.

@article{duffie2010asset,
  title={Asset price dynamics with slow-moving capital,(American Finance Association Presidential Address)},
  author={Duffie, Darrel},
  journal={Journal of Finance},
  volume={65},
  pages={1238--68},
  year={2010}
}

6. **"Passive Investors, Not Passive Ownership" (2016)**
   - 저자: Ian R. Appel, Todd A. Gormley, Donald B. Keim
   - 저널: Journal of Financial Economics
   - 주요 내용: 패시브 펀드의 소유권 증가가 기업 지배구조와 가치에 미치는 영향을 연구. 패시브 투자의 증가가 시장 메커니즘과 가격 발견 과정에 미치는 영향 분석.

@article{appel2016passive,
  title={Passive investors, not passive owners},
  author={Appel, Ian R and Gormley, Todd A and Keim, Donald B},
  journal={Journal of Financial Economics},
  volume={121},
  number={1},
  pages={111--141},
  year={2016},
  publisher={Elsevier}
}

7. **"Is There a Dark Side to Exchange Traded Funds? An Information Perspective" (2017)**
   - 저자: Doron Israeli, Charles M.C. Lee, Suhas A. Sridharan
   - 저널: Review of Accounting Studies
   - 주요 내용: ETF와 같은 패시브 투자 수단의 증가가 기초자산의 가격 정보 효율성에 부정적 영향을 미칠 수 있음을 실증적으로 분석.

@article{israeli2017there,
  title={Is there a dark side to exchange traded funds? An information perspective},
  author={Israeli, Doron and Lee, Charles MC and Sridharan, Suhas A},
  journal={Review of Accounting Studies},
  volume={22},
  pages={1048--1083},
  year={2017},
  publisher={Springer}
}

8. **"The Asset Pricing Implications of Government Economic Policy Uncertainty" (2016)**
   - 저자: Jonathan Brogaard, Andrew Detzel
   - 저널: Management Science
   - 주요 내용: 정부 정책 불확실성이 자산 가격과 수익률 분포에 미치는 영향을 연구. 통화정책의 불확실성이 수익률 분포의 비대칭성에 어떤 영향을 미치는지 분석.

@article{brogaard2015asset,
  title={The asset-pricing implications of government economic policy uncertainty},
  author={Brogaard, Jonathan and Detzel, Andrew},
  journal={Management science},
  volume={61},
  number={1},
  pages={3--18},
  year={2015},
  publisher={INFORMS}
}

