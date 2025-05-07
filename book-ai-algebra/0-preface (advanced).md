
> 주제: 선형 공간 안에 벡터 (방향성, 크기)들의 관계 (연산)

이런 걸 배울 수 있어요

- 행렬로 나타내고 그림으로 보는 선형 연립 방정식
- 데이터 테이블 (행렬)과 데이터 (벡터)
- 평행사변형과 선형공간
- 미분방정식에서 고유벡터의 의미 (축척)
- 선형회귀모형에서 수직이 아닌 방향
- 최적화이론의 목적함수와 정부호행렬
- 여러가지 행렬 분해법 활용
- 군과 선형사상

Introduction to Linear Algebra (6th edition): [Gilbert Strang](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/) in MIT OpenCourseWare (MIT OCW)
![[book-strang.png]]

### 커리큘럼

**선형연립방정식**에서 출발해 선형**공간과 고유값**으로 확장하고, 이어서 **내적공간·분해정리(SVD, QR)** 및 **최소제곱법**·**힐버트 공간** 등 특수한 응용을 다룬 뒤, 마지막으로 **군(群)과 추상구조** 등 일반화 된 개념을 소개하며 전체 학습을 마무리합니다.

### (선형연립방정식 해석) $X\boldsymbol{\beta} = \boldsymbol{y}$

- **행렬 표현과 행렬의 연산법칙**
- **Geometry of Linear Equations**:
    - **Gaussian Elimination (가우스 소거법), Row-reduced Echelon Form**
    - **Pivot (피봇), Pivot Column (피봇 열)**: 행렬의 랭크(rank)와 직결되며, 해의 개수 및 유·무결정성에 영향을 준다.
    - Rank–Nullity Theorem (계수-퇴화차수 정리)와 4개의 부분공간 (열공간(Column space), 행공간(Row space), 영공간(Null space), 왼쪽 영공간(Left null space))
- **치환 (Permutation)과 대칭행렬 (Symmetric matrix)**
    - **행렬식 (Determinant)이 결정하는 것**
        - 선형공간의 차원: **초등 행렬 (Elementary matrix)**
        - 특이행렬(singular matrix)? 선형변환이 “부피(volume)를 0으로 만든다”
        - 비특이행렬(non-singular matrix): **역행렬 (Inverse matrix)**이 존재
    - **LU factorization:** 정방행렬 𝐴를 두 개의 삼각행렬로 분해해서 선형계를 빨리 풀기
        - 필요 시 치환행렬(Permutation matrix)로 부분 피벗팅(Partial Pivoting)을 고려해 PA=LU 형태로 분해
        - **Cholesky decomposition**: 정방행렬이 양정부호인 경우는 더 빠르게.

### (선형공간의 구조와 분해) Structures of Linear space

- **선형 공간 (Linear space = Vector space)**
    - 집합이 선형적 연산 (즉, 덧셈과 스칼라곱)에 대해 닫혀 있음: 덧셈에 대한 가환군 (Abelian Group)에 크기 늘리기 연산자 (스칼라곱, scalar multiplication)을 추가한 공간
    - 선형 공간: 선형적 벡터 공간, 선형적 함수 공간
    - **선형결합 (Linear combination), 선형독립 (linear independence), 부분공간(subspace), 기저(basis), 차원(dimension)**
- **평행사변형에서의 대각선**: 고유벡터(Eigenvector)와 고유값 (Eigenvalue)
    - **케일리-해밀턴 정리 (Cayley-Hamilton Theorem)**: 행렬의 특성 방정식 (Characteristic equation)
    - **고윳값분해(Eigendecomposition), 행렬의 대각화 (Diagonalization)**
    - 선형미분방정식 (Linear Differential Equations)과 지수행렬 \exp(A t)
    - **마크코프체인 모형 (Markov-Chain model):** 전이행렬(transition matrix)에 의한 steady-state vector(정상분포)를 고유벡터로 해석
- **직사각형에서의 피타고라스 정리 (Pythagorean theorem): 수직 (perpendicularity)의 개념**
    - **내적 연산자 (Inner product operator)가 있는 내적 공간 (Inner Product Space)**
    - 내적에서 유도되는 거리(길이) 개념인 놈(Norm)
    - 직교여공간(Orthogonal complement): 해 공간과 여공간의 관계
- **직교기저 분해정리 (Spectral Theorem)**
    - 표준기저(Standard Basis)를 정규직교기저(Orthonormal Basis)로 만드는 과정
    - **QR decomposition**: 직사각형 행렬 𝐴를 직교(orthonormal) 행렬 𝑄와 상삼각행렬(upper triangular matrix) 𝑅로 분해
        - Gram-Schmidt Algorithm 을 활용하여 Q, R 추출
    - **SVD (Singular Value Decomposition)**: 직사각형 행렬 𝐴를 정규직교 정사각행렬들과 직사각 대각행렬로 분해.
- **선형회귀모형 (Linear regression model)에서 최소제곱법 (Least Squares method)**
    - **정규방정식(Normal equation)과 직교사영(Orthogonal Projection)**
- **힐버트 공간(Hilbert space)과 푸리에 급수(Fourier Series)**
    - 내적공간의 구조가 무한 차원으로 확장되는 예시
    - 기함수/짝함수 분해, 편의상 $[-\pi,\pi]$ 구간에서의 직교기저
- **Bilinear form as a local volume form**
    - **국소적 선형공간에서의 표준적 부피 형식 (Volume form)과 텐서 (Tensor)**
    - **Positive definite kernel (양의정부호 커널)**, **Dual space (쌍대공간)**, **Optimization problems (최적화 문제들)**
    - 편미분방정식(PDE), 미분기하학 등 고급 응용과도 연결

### (군과 구조 개념) Group and structures

- **대수적 공간 (Algebraic space)**: Space(공간) = Set(집합) + Structure(구조)
    - 직합(Direct Sum, $\oplus$): 두 개 이상의 선형 공간(또는 부분공간 subspace)을 하나의 더 큰 벡터 공간으로 묶는 연산.
    - 몫공간 (Quotient Space, $V/W$): 벡터 공간 V에서 부분공간 W를 나누어 새로운 공간을 정의하는 개념. 몫공간 V/W의 원소는 **여공간(coset) $v+W$** 로 표현됨. 예를 들어, $\mathbb{R}^3$에서 $W = \operatorname{Span} \{(1,0,0)\}$ 라고 하면, ,$\mathbb{R}^3 / W$는 **원점을 지나면서 x-축과 평행한 평면들의 공간**.
    - 벡터 공간을 나누는 서로 다른 방법: 직합과 몫공간
        - $U \oplus W$이면, $V/W \cong U$. 즉, 몫공간을 취하면 남은 부분이 원래 공간의 다른 부분과 동형이 됨.
- 대수적 군 (Group) : 공간의 분류
    - **정사각형, 직사각형, 마름모, 평행사변형:** 평행이동·회전·대칭 등 기하학적 변환을 “군” 관점에서 볼 수도 있음
    - **몫공간 (Quotient space)**,
    - **일반선형군 (General linear group, GL(n))**: 행렬 곱셈이 가능한 가역 정방행렬들의 집합. 역행렬이 존재하는 정방행렬들의 집합. 행렬식이 0이 아닌 모든 정방행렬
        - 선형공간 내 벡터들에 벡터 내적연산을 추가해도 벡터들이 속한 선형공간은 가환군이지만, 선형공간 내 행렬들에 행렬 곱셈을 추가하면 행렬들이 속한 선형공간은 비가환군(Non-Abelian Group, )
        - GL(n,R) (실수 계수 정방행렬의 군)
        - **유니터리 군 (Unitary group, U(n))**: 복소수 계수 n×n 행렬 중에서, $U'U=I$ 를 만족하는 (즉, 켤레전치가 역행렬) 유니터리 행렬(unitary matrix)의 집합. 행렬의 원소인 벡터의 길이(norm)와 각도(inner product)를 보존하는 변환. **회전, 반사 등**을 포함하는 복소수 변환들 (행렬군).
            - 실수 행렬 버전이 **직교군 (Orthogonal group, O(n))**,
- **구조 불변 변환 (Morphism)**:
    - “구조 불변”이란 특정 성질(길이·각도·부피·위상 등)을 그대로 보존하는 변환을 의미하며, 군과 범주의 핵심 개념이다.
    - 선형사상(Linear map)
    - 동형사상(Isomorphism, same)
    - 준동형사상(Homomorphism, similar)
    - Rank–Nullity Theorem as the first isomorphism theorem ([*Fundamental theorem on homomorphisms](https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms))* in Noether's isomorphism theorems