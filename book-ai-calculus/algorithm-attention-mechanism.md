Attention Mechanism은 모든 현대 NLP 구조의 핵심이며, 특히 Scaled Dot-Product Attention은 LLM Transformer 구조의 근간.

## 핵심 개념: What is Attention?

- 목표: 배열 내에서 어떤 요소를 다른 요소에 비해 얼마나 집중할지(=중요도) 정량화.
    - 상대적 가중치 (relative weight).
    - 출력: 입력 배열의 각 구성요소에 대한 가중합(weighted sum)

## 기본 수학 표현 (Scaled Dot-Product Attention)

Attention 함수는 다음과 같이 정의됩니다:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

- $Q$: Query matrix ∈ $\mathbb{R}^{n \times d_k}$
- $K$: Key matrix ∈ $\mathbb{R}^{n \times d_k}$
- $V$: Value matrix ∈ $\mathbb{R}^{n \times d_v}$
- $n$: 토큰 수, $d_k$: key/query 차원, $d_v$: value 차원

**해석**: 
- Query가 Key와 얼마나 유사한지로 중요도 (가중치)를 계산
	- $\frac{QK^\top}{\sqrt{d_k}}$ = 정규화된 유사도 행렬 (scaled attention score). 
	- softmax는 유사도를 확률적 중요도로 변환
	- 변형 attention 함수들: softmax 외에 ReLU, sigmoid도 있음. 
- Value는 정보 그 자체이며, $V$에 가중치를 곱해 최종 output 산출

## 간단한 예시 (토큰 2개, 임베딩 차원 2인 경우)

**문장 예시**: `"The cat"`

- "The": 문장 구조상 중요한 단어는 아니며, 대부분의 경우 의미적 기여가 적음
- "cat": 핵심 명사로서 문맥상 중요한 정보

### Step 1: 입력 정의

Query, Key, Value 행렬:

- $Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ → Query: "The", "cat"
- $K = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ → Key: "The", "cat"
- $V = \begin{bmatrix} 1 & 2 \\ 9 & 8 \end{bmatrix}$ → Value: 정보 자체 ("The"는 약한 정보, "cat"은 강한 정보)

### Step 2: scaled attention score 계산

$QK^\top = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$

$\frac{QK^\top}{\sqrt{2}} = \begin{bmatrix} \frac{1}{\sqrt{2}} & 0 \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}$

### Step 3: Attention weight 계산 (행별 적용)

각 행에 **softmax** 적용 (단어별로 다른 단어에 대한 집중도 계산):

"The"의 attention weight:
$$\text{softmax}([0.707, 0]) = \left[\frac{e^{0.707}}{e^{0.707} + 1}, \frac{1}{e^{0.707} + 1}\right] ≈ [0.669, 0.331]$$

"cat"의 attention weight:
$$\text{softmax}([0.707, 0.707]) ≈ [0.5, 0.5]$$

### Step 4: Attention output (Weighted Sum) 계산

행렬 곱: $\text{Attention}(Q, K, V) = \text{softmax}\left( \cdots \right) V$

"The"의 attention output:

$$[0.669,0.331] \cdot \begin{bmatrix} 1 & 2 \\ 9 & 8 \end{bmatrix} = [0.669 \cdot 1 + 0.331 \cdot 9,\ 0.669 \cdot 2 + 0.331 \cdot 8] = [3.648,\ 4.316]$$

"cat"의 attention output:
$$[0.5,0.5] \cdot \begin{bmatrix} 1 & 2 \\ 9 & 8 \end{bmatrix} = [5.0, 5.0]$$

**해석**:

- "The"는 본래 정보량이 적지만, 문장 내에서 "cat"에 주목하여 **의미를 재구성**함
- "cat"은 자기 자신과 "The" 모두를 동일하게 고려하여, **중심 의미**로 정제된 표현을 생성함

## Self vs. Cross Attention

| 구분              | $Q$           | $K$         | $V$         | 설명 및 예시                         |
| --------------- | ------------- | ----------- | ----------- | ------------------------------- |
| Self-Attention  | 동일 입력         | 동일 입력       | 동일 입력       | Transformer encoder (입력 내 상호작용) |
| Cross-Attention | decoder에서 입력됨 | encoder의 출력 | encoder의 출력 | Encoder–Decoder 구조 (T5, BART 등) |
