---
title: Time-Varying Cointegration in Economic Indicators and Structural Break Analysis 
subtitle: US data
---

## Preliminaries
- Spurious correlation vs. Cointegration: High linear correlation between two non-stationary time series may be spurious, unless the series are cointegrated, meaning they share a long-term equilibrium.
- In econometrics, cointegration is a statistical property describing a **long-term, stable relationship** between two or more time series variables, even if those variables themselves are individually non-stationary (i.e., they have trends). This means that despite their individual fluctuations, the variables move together in the long run, anchored by an underlying equilibrium relationship. If two or more time series are **individually** integrated of order 1 (I(1)), meaning they need one difference to become stationary, but there exists a **linear combination** of these series that is stationary (I(0)), then the series are **cointegrated**. In other words, despite each series following its own random walk, a specific weighted sum (a linear combination) of them is stable over time.
- 공적분 개념에서는 변수들이 **장기적으로** **안정적인** **선형 결합**을 보였으면, 장기적 균형관계를 형성하고 있다고 추론함. **보통 10년 이상**의 데이터에서, the absolute value of estimated correlation coefficient가 0.7 이상이면 **안정적** 균형관계가 있다고 해석함.
- Nelson & Plosser (1982) Findings: Many US macroeconomic time series (e.g., GDP, wages, employment) exhibit stochastic trends, implying that standard regression models using such data may yield misleading results without testing for cointegration.

## Overview

This study aims to analyze the persistent yet time-varying structural relationships among key economic indicators through **cointegration** analysis while **quantitatively tracking** how these relationships evolve over time. The research also seeks to **identify structural breaks** in these **long-run** relationships, providing insight into the impact of economic crises, policy shifts, and macroeconomic shocks. The findings may contribute to **long-term** investment strategy optimization, economic forecasting, and policy evaluation.

## Research Questions and Hypothesis

- Which economic indicators form a (statistically significant) **long-term** relationship?
  - Variables such as corporate investment, interest rates, money supply, inflation, and stock market values are expected to be cointegrated.
- How much these relationships changed over time?
  - The relationships are **time-varying**, meaning they strengthen, weaken, or disappear over different periods. But how much?
- How to relate these **quantitatively** detected structural breakpoints with **causal** and **qualitative** external macroeconomic shocks (e.g., policy shifts, recessions, financial crises)?
  - Cointegration breakdowns should coincide with major economic disruptions (e.g., 2008 financial crisis, 2020 COVID-19 pandemic).

## Key Considerations
- Selecting Relevant Economic Indicators:
  - Identifying the most widely used variables in investment and policy decision-making.
- Classifying Economic Indicators:
  - Granger causality tests determine whether leading indicators **predict** (not cause) coincident variables
  - Leading indicators (e.g., corporate investment), coincident indicators (e.g., stock market indices), lagging indicators (e.g., inflation).
- Determining the Integration Order and Standardizing Measurement Units:
  - All variables included in the cointegration analysis must be of the same integration order ($I(d)$).
  - If a variable is $I(2)$ while others are $I(1)$, transformation is necessary.
  - What if X is arithmetic series while Y is geometric series? Applying log transformations to Y and converting variables into returns for comparability.
- Testing methods for Cointegration:
  - Engle-Granger Test 
  - Johansen Cointegration Test
  - Alternative testing methods?
- Estimating methods to detect Multiple Structural Breakpoints Simultaneously: (assumptions and limitations)
  - Unlike parametric models, this study assumes a nonparametric linear relationship using data-driven methods.
  - Bai-Perron Structural Break Test:
  - Rolling Johansen Cointegration Test:
  - CUSUM & CUSUMSQ Tests: 
  - Quandt-Andrews Unknown Breakpoint Test: 
  - Sup-Wald Test: 

## Data Collection and Preprocessing
### Data Sources and Variables
- **Data period**: January 1990 – December 2024 (34 years)
- **Data frequency**: Monthly

| **Category**      | **Variable**                                  | **Source**            | **Observation Start** | **Frequency** |
|------------------|---------------------------------------------|----------------------|----------------------|--------------|
| **Equity**       | SPY (S&P 500 ETF)                          | Yahoo Finance       | 1993                 | Daily/Monthly |
| **Equity**       | NDX (NASDAQ 100)                           | Yahoo Finance       | 1985                 | Daily/Monthly |
| **Currency**     | DXY (Dollar Index)                         | FRED / Yahoo        | 1973                 | Daily/Monthly |
| **Short-term Bond** | Fed Rate (Federal Funds Rate)           | FRED                | 1954                 | Monthly |
| **Long-term Bond** | 10-Year Treasury Yield                   | FRED                | 1953                 | Monthly |
| **Money Supply** | M2 (Money Supply)                         | FRED                | 1959                 | Monthly |
| **Gold**         | Gold Price                                 | Yahoo Finance       | 1975                 | Daily/Monthly |
| **Inflation**    | CPI (Consumer Price Index)                | FRED                | 1947                 | Monthly |
| **Consumption**  | University of Michigan: Consumer Sentiment| FRED                | 1978                 | Monthly |
| **Investment**   | Real Gross Private Domestic Investment (GPDIC1) | FRED                | 1960                 | Quarterly |

💡 **Adjustment for Quarterly Data**  
GPDIC1 (investment data) is originally **quarterly** and must be **converted to monthly frequency** using **linear interpolation**:

## Cointegration Testing

### Unit root tests
- a unit root should not be present in Each time-series. 
- For each testing method, examinine Model formula, assumption, limitations, Procedure, Decision criteria
  - Augmented Dickey-Fuller (ADF) Test
  - Phillips–Perron test (PP) 
  - ADF-GLS test procedure (ERS)
  - KPSS Test 

### Cointegration existence tests
- After ensuring that all series are $I(1)$, the multivariate time-series are cointegrated if a linear combination of variables is $I(0)$
- 만약 공적분이 존재하지 않으면, 단기적 autoregressive 관계 위주로 분석 (e.g., VAR Model). 
- For each testing method, examinine Model formula, assumption, limitations, Procedure, Decision criteria
  - Johansen Cointegration Test: Determines the number of cointegrating relationships (rank $r$).
  - Engle-Granger Cointegration Test: Used for pairwise relationships.
  - Alternative tests?

## Quantitative Structural Breakpoint Detection methods
- How can we simultaneously detect multiple structural breaks in cointegration relationships?
- For each testing method, examinine Model formula, assumption, limitations, Procedure, Decision criteria
  - Bai-Perron Structural Break Test: Detects multiple structural breakpoints in regression relationships.
  - Rolling Johansen Cointegration Test: Tracks how cointegration relationships evolve over time. Sudden jumps in p-values indicate cointegration breakdowns.
  - Quandt-Andrews Unknown Breakpoint Test: Checks for a single unknown structural break. Tests whether regression coefficients change at an unknown point.

## Qualitative analysis of the detected Structural Breakpoints
- Compare breakpoints of cointegration with macroeconomic events (e.g., 2008 financial crisis, COVID-19 pandemic).
- Provide empirical insights into how economic indicators interact over time.

Once breakpoints are identified, compare them to historical macroeconomic events.

Breakpoint Date	Potential Cause
2008-Q3	Global Financial Crisis
2011-Q3	European Debt Crisis
2020-Q1	COVID-19 Shock
2022-Q1	Inflation Surge & Interest Rate Hikes
Overlay detected structural breaks on historical policy decisions, crises, and market events.


---
### **Evaluation of the Proposed Research Flow**

Your proposed **flow is logically strong** and follows a **step-by-step approach** to analyzing **structural breaks in cointegration relationships**, considering different modeling techniques at each stage. This framework allows for **progressive refinement**, starting from **traditional econometric techniques** and advancing toward **more complex nonlinear models**. 

Below is a **logical breakdown** of your approach and its strengths:

---

## **1. Detecting Structural Breaks in Cointegration Under the Traditional Cointegration Framework**  
**Objective**: Use standard cointegration models to identify **long-term relationships** and apply structural breakpoint detection methods.  

### **Step 1: Cointegration Testing**
- Use **Johansen Cointegration Test** to check for **long-run equilibrium relationships** among economic indicators.
- Apply **Engle-Granger Cointegration Test** for **pairwise relationships**.

**Methods:**
- **Johansen Cointegration Test**: Identifies **how many** cointegrating relationships exist in a **multivariate system**.
- **Engle-Granger Cointegration Test**: Confirms whether a **specific variable pair** is cointegrated.
  
**Expected Output**:  
- A set of **cointegrated variable pairs or groups** that will be tested for **structural breaks**.

---

### **Step 2: Structural Break Detection in Cointegration Relationships**
Once cointegration is established, structural breakpoints are detected using standard break tests.

**Break Detection Methods:**
- **Bai-Perron Structural Break Test**: Identifies multiple structural shifts in **linear regression relationships**.
- **Quandt-Andrews Unknown Breakpoint Test**: Tests whether there is an **unknown break** at some point in the data.
- **Rolling Johansen Cointegration Test**: Tracks how **cointegration relationships evolve over time** and identifies shifts in equilibrium.
- **CUSUM & CUSUMSQ Tests**: Detects structural changes in **residual variance over time**.

**Expected Output**:  
- Identified **structural breakpoints** in the **traditional linear cointegration model**.

---

## **2. Detecting Structural Breaks in Fractional Cointegration Models**
**Objective**: Extend structural break analysis to a **fractional cointegration framework**, which allows for **long-memory relationships and non-integer integration orders**.

### **Step 1: Fractional Cointegration Testing**
- Apply **Geweke and Porter-Hudak (GPH) Test** to estimate the **fractional integration order ($d$) of each series**.
- Use **Robinson’s Fractional Cointegration Test** to determine if a **fractional cointegration relationship exists**.

**Methods:**
- **GPH Test**: Estimates the **memory parameter ($d$) to determine long-term persistence**.
- **Robinson Test**: Tests whether the **linear combination of cointegrated variables has a lower fractional integration order** than the original series.

**Expected Output**:  
- Confirmation that **fractional cointegration exists** and that the system follows a **long-memory adjustment process**.

---

### **Step 2: Structural Break Detection in Fractional Cointegration**
Since fractional cointegration **adjusts continuously rather than in discrete jumps**, traditional break detection methods may not fully capture changes. We use methods adapted to **fractional models**:

**Break Detection Methods for Fractional Cointegration:**
- **Rolling Estimates of the Fractional Differencing Parameter ($d$)**: Observes whether the integration order of residuals **shifts over time**, indicating a **gradual regime shift**.
- **Wavelet-based Break Detection**: Identifies breaks in **long-memory processes** by decomposing time-series data into **different frequency components**.
- **Rolling Hurst Exponent Analysis**: Measures whether the persistence of shocks **changes structurally over time**.

**Expected Output**:  
- Structural breaks specific to the **fractional cointegration model**.

---

## **3. Identifying Common Structural Breakpoints Across Both Models**
By comparing breakpoints detected in both **traditional and fractional cointegration models**, we can:
- Identify **common breakpoints** that appear under **both frameworks**, which are more likely to be **true structural shifts** rather than artifacts of a particular model.
- Distinguish between **discrete breaks (traditional) vs. gradual shifts (fractional)** to better understand the **nature of economic regime changes**.

---

## **4. Applying Threshold Cointegration to Common Structural Breakpoints**
**Objective**: If breakpoints from both models **align**, apply **threshold cointegration models** to estimate **adjustment speeds across different regimes**.

### **Step 1: Threshold Cointegration Testing**
- Define a **threshold level ($\gamma$)** based on identified breakpoints.
- Estimate **threshold-adjusted error correction models (ECM)**.

**Methods:**
- **Threshold Error Correction Model (TECM)**:  
  \[
  \Delta Y_t =
  \begin{cases}
  \alpha_1 (Y_{t-1} - \beta X_{t-1}) + \epsilon_t, & \text{if } |Y_{t-1} - \beta X_{t-1}| > \gamma \\
  \alpha_2 (Y_{t-1} - \beta X_{t-1}) + \epsilon_t, & \text{if } |Y_{t-1} - \beta X_{t-1}| \leq \gamma
  \end{cases}
  \]
- **Generalized Sup Wald Test**: Tests whether the **threshold level is statistically significant**.

**Expected Output**:
- Estimation of **adjustment speeds in different regimes** ($\alpha_1, \alpha_2$).
- Identification of **whether the reaction to deviations from equilibrium is asymmetric**.

### **Step 2: Interpretation and Limitations**
- **Interpretation**: How do different regimes influence **economic variable adjustments**? Are market corrections **faster in recessions vs. expansions**?
- **Limitations**:
  - Threshold selection is **data-driven**, which may introduce **bias**.
  - **Regime definitions may be arbitrary** if not supported by economic theory.

---

## **5. Applying Threshold Fractional Cointegration**
**Objective**: Extend the analysis by combining **fractional integration properties with threshold effects**.

### **Step 1: Estimating Threshold Fractional Cointegration**
- Identify whether **threshold effects exist in a fractional cointegration framework**.
- Apply **threshold effects to the fractional adjustment process**.

**Methods:**
- **Threshold Fractional Error Correction Model (TFECM)**:
  \[
  \Delta Y_t =
  \begin{cases}
  (1 - L)^{d_1} X_t + \epsilon_t, & \text{if } |X_t - \beta Y_t| > \gamma \\
  (1 - L)^{d_2} Y_t + \eta_t, & \text{otherwise}
  \end{cases}
  \]
- **Sup LM Test for Nonlinear Adjustment in Fractional Cointegration**: Tests whether the adjustment process follows a **threshold-dependent fractional correction**.

**Expected Output**:
- A **combination of fractional long-memory effects and regime-dependent adjustments**.
- A more **flexible model that accounts for both smooth and discrete shifts**.

### **Step 2: Interpretation and Limitations**
- **Interpretation**: Do economic relationships follow **a mix of gradual memory-driven corrections and threshold-based regime shifts**?
- **Limitations**:
  - **Computational complexity**: Requires **more sophisticated estimation methods**.
  - **Theoretical justification**: Harder to justify **why certain variables follow threshold-dependent fractional adjustments**.

---

## **Final Evaluation of the Research Flow**
✔ **Logical Coherence**: The flow starts with a **well-established method (traditional cointegration)** and progressively incorporates **more sophisticated models**, leading to a **highly flexible and robust framework**.  

✔ **Comprehensive Analysis**: By identifying breakpoints under **both traditional and fractional cointegration**, the study avoids biases associated with **single-method approaches**.  

✔ **Innovative**: The final application of **Threshold Fractional Cointegration** integrates **memory effects and regime shifts**, making it a **powerful tool for modeling real-world economic dynamics**.  

✔ **Challenges Addressed**:  
- **Accounts for nonlinearity** in long-term relationships.  
- **Handles heterogeneous integration orders**.  
- **Provides a systematic way to distinguish gradual shifts from abrupt structural breaks**.  

**Conclusion**: This flow provides **a novel and rigorous approach** to understanding long-term economic relationships while addressing major limitations in existing econometric models. It serves as a **comprehensive framework for studying structural changes in cointegration relationships**.