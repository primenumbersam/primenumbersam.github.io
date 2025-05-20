---
title: 기본 용어 정리
---

## 대수 용어

### 다항식 (Polynomial)

- 항 (Term, nomial) : 숫자나 문자의 곱으로 이루어진 식. 덧셈 기호로 구분됩니다. 예: $3x$, $-5xy^2$
- 다항식 (Poly-nomial) : 여러 항으로 이루어진 식
- *상수항 (constant term)*: 아는 숫자만 있는 항 (예: 7)
- *변수항 (unknown term)*: 모르는 숫자 (문자로 표현)가 포함된 항 (예: $3x$, $-2x^2$)
- *계수 (Coefficient)*: 변수항의 아는 숫자 부분
- *차수 (Degree)*: 변수항의 지수. **다항식의 차수**는 최고차항의 차수
- *동류항*: 차수가 같은 항들

$$2x^2 + 3x - 5 \quad \text{(최고차항: $2x^2$, 차수: 2)}$$

### 등식 (Equality)

두 수나 식이 항상 같음을 나타내는 수학 문장입니다. 등호 기호 `=`를 사용합니다.

- 예: $3 + 2 = 5$, $f(x) = y$

### 항등식 (Identity)

변수의 값과 관계없이 항상 참인 등식입니다. 수학 체계의 기초 문법으로 자주 등장합니다.

- 예: $a^2 - b^2 = (a - b)(a + b)$, $e^{i\pi} + 1 = 0$

### 부등식 (Inequality)

양변이 같지 않은 관계를 나타내는 문장입니다. 부등호 $\ne$, $<$, $\le$, $>$, $\ge$ 등을 사용합니다.

- 예: $1 < 2$, $\sqrt{x^2} \ge x$

### 방정식 (Equation)

연산자들 (operators)의 식 (formula)을 이용해서, 아는 계수 (상수, known coefficients)와 모르는 변수 (미지수, unknown variable)의 관계를 등호 (=)로 표현한 등식

- 1차 방정식: $\displaystyle \frac{x - 4}{3} = \frac{2x - 12}{4}$
- 2차 방정식: $x^2 - 2x + 1 = 0$

### 함수 (Function)

정적 해석 (동양식): 서로 다른 개체들 간의 동시적 관계를 표현합니다.
동적 해석 (서양식): 하나의 입력값에 대해 하나의 출력값을 정해주는 규칙입니다.

- 표기: $f: X \to Y$
- 정의역 (domain): $X$ (입력값들의 집합)
- 공역 (codomain): $Y$ (가능한 출력값들의 집합)
- 치역 (range): 실제로 출력되는 값들의 집합 $\subseteq Y$
- 역함수 $f^{-1}: Y \to X$는 $f$가 일대일 대응일 때 존재합니다.
- 일대일 대응 관계 (bijective, 1-1)는 아니지만, surjection (onto) 인 예시: $f(x) = x^2, \quad f: \mathbb{R} \to \mathbb{R}_{\ge 0}$
- 중요: 쓸모 없는 기계? 어떠한 입력값에도 대응되지 않는 출력값을 출력하는 기계. 객관적으로 관측 가능한 독립변수 집합에서 종속변수 집합 (e.g. 예측값)을 해석할 수 없는 기계


## 집합과 논리 (Set and Logic)

### 집합

- 원소들의 모임
- 예: $A = \{1, 2, 3\}$

### 포함 관계

- 원소 포함: $x \in A$
- 부분집합: $A \subseteq B$

### 논리 기호

- AND (그리고): $\land$
- OR (또는): $\lor$
- NOT (아니다): $\lnot$
- 조건: $P \Rightarrow Q$ ("P이면 Q이다")


## 직교좌표계 (Cartesian Coordinate System)

-   x 축 : 가로방향 수직선
-   y 축 : x축에 수직인 세로방향 수직선
-   위치좌표 : 순서쌍 (x,y)
    -   원점 : x축 직선과 y축 직선이 만나는 점 (0,0)
-   사분면 : 시계반대방향

- **x축**: 가로 방향 수직선
- **y축**: 세로 방향 수직선 (x축과 y축은 서로 **수직 (직각)** 관계)
- **원점**: $(0, 0)$
- **점의 좌표 표현**: $(x, y)$
- **사분면 (quadrant)**: 원점 $(0, 0)$을 중심으로 **시계반대 방향**으로 제1~4사분면

```{python}
import matplotlib.pyplot as plt

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.text(1, 1, 'I')
plt.text(-1, 1, 'II')
plt.text(-1, -1, 'III')
plt.text(1, -1, 'IV')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal')
plt.show()
```
