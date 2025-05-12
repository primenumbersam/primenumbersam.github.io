---
title: What Matters in Linear Algebra
subtitle: Linearity, Duality, and Scale
---

This book is an introduction to linear algebra, and all the examples throughout the chapters are based on two fundamental assumptions: **linearity** and **small-scale variable structures**. Before delving into specific models, we clarify several foundational concepts that students often find confusing.

## Simple linear model?
Why are simple linear models studied more extensively than complex nonlinear models?

* **Parsimony**:
  Deep learning and large language models are typically considered black-box systems, where the internal mechanisms between input and output are difficult to interpret.
  In contrast, linear models offer transparent causal relationships between variables, making them especially effective for decision-making and policy evaluation tasks.

* **Computational tractability**:
  Numerical computation, whether by hand or machine, ultimately relies on local linear approximation.
  For example, as in digital displays where curves must be approximated by straight-line segments at high resolution, all nonlinear systems must be handled as locally linear for practical calculation.

* **Precision**:
  Linear models trade some degree of predictive accuracy for interpretability and structural clarity.
  In contrast, models such as deep learning and LLMs pursue accuracy at the cost of interpretability.
  This trade-off is closely related to the classical bias–variance dilemma.

## What is linearity?

Linearity assumes that the internal structure of a system lies on a linear space.
This does not merely refer to a "straight line," but to a vector space where addition and scalar multiplication are defined and behave predictably.

* In one dimension, this space can be visualized as a line segment.
* In two dimensions, a plane.
* In three or more dimensions, it is often represented by a polytope.

These geometric interpretations are intuitive and visual. More abstract algebraic properties of linearity will be discussed in later chapters, especially in those focusing on vector spaces and linear transformations.

## What is meant by a small-scale model?

A small-scale model refers to a system with a **limited number of variables to estimate**. Specifically:

* In the context of deep learning, this means the number of unknown parameters to learn across a network is relatively small.
* In control theory, the number of state variables already known through measurement or estimation is small, so the number of control variables to be determined is also small.
* In decision models, the number of known coefficients is small, hence the dimensionality of the decision space is reduced.

## What is duality?

In linear models, it is common to find problems that can be formulated and interpreted in two complementary ways. This structural feature is called **duality**.

* **Geometrically**, we find that rectangles and rhombuses are dual in the plane; in conic sections, ellipses and hyperbolas are dual shapes, with the parabola appearing as the critical boundary between them.

* **Algebraically**, duality refers to the structural symmetry between two seemingly distinct types of quantitative variables, as determined by the underlying relationships that govern the system.

Some representative dual pairs include:

* state variables vs. control variables
* estimated variables vs. estimating variables
* constants vs. variables

To interpret a system’s duality, we must ask a fundamental question:

What do we know with greater certainty?

For example:

* In **physics**, we can directly observe the position of an object, but velocity is derived from relative motion across time. Which is more fundamental?

* In **economics**, individual or sector-level income may be measurable, but relative value across sectors emerges only through interaction. Which tells us more about the system?

* In **philosophy**, the human body is physically perceptible, but the mind remains elusive. Which better defines human identity?

* In **biology**, both genetic inheritance (nature) and environmental influence (nurture) shape personality. Which exerts greater causal force?

These questions are not merely about data—they reflect our **philosophical orientation toward modeling the world**.
In this way, duality in linear algebra is not just a computational technique, but a foundational principle in how we understand, construct, and interpret models.
It helps us not only calculate, but also decide where to look and what to value in real-world systems.



이 책은 선형대수학의 입문서이므로, 모든 예제는 선형성과 소규모 변수 구조를 전제로 합니다. 본격적인 모형들을 소개하기에 앞서, 학생들이 자주 혼동하는 개념들을 먼저 정리합니다.

왜 복잡한 비선형 모형보다 단순한 선형 모형이 더 많이 연구되어 왔는가?

* 간결성 (parsimonious):
  딥러닝이나 대형 언어 모델은 구조적으로 블랙박스에 가까워, 입력과 출력 사이의 작동 메커니즘을 명확히 파악하기 어렵습니다.
  반면 선형 모형은 변수 간의 인과 구조가 투명하여, 의사결정이나 정책 평가와 같은 실제적 목적에 유리합니다.

* 계산 가능성 (computational tractability):
  컴퓨터에 의한 수치 계산은 결국 국소적 선형 근사(local linear approximation)를 필요로 합니다.
  예를 들어, 디지털 화면의 해상도처럼 모든 곡선은 충분히 작은 영역에서는 직선으로 근사되어야만 계산이 가능합니다.

* 정밀성 (precision):
  선형 모형은 예측의 정확도를 일정 부분 포기하는 대신, 구조적 정밀성과 해석 가능성을 얻습니다. 반면, 딥러닝이나 LLM은 정밀성을 포기하고 정확도를 높이려는 시도이며, 이는 결국 bias–variance tradeoff의 일종으로 해석할 수 있습니다.

선형성(linearity)이란?

시스템 내부의 구조가 선형 공간(linear space) 위에 있다고 가정하는 것입니다. 이때 '선형'이라는 말은 단순히 직선의 의미가 아니라, 덧셈과 스칼라 곱이 정의된 공간 구조를 의미합니다.

* 1차원에서는 선분,
* 2차원에서는 평면,
* 3차원 이상에서는 다면체(polytope)로 시각화할 수 있습니다.

이러한 기하학적 해석은 누구나 직관적으로 이해할 수 있으며, 보다 추상적인 대수적 선형성은 본문의 관련 단원에서 자세히 다루게 됩니다.

소규모 모형(small-scale model)이란?

여기서 말하는 '소규모'란 추정해야 할 변수의 개수가 작다는 뜻입니다. 구체적으로,

* 딥러닝 모델 관점에서는, 텍스트나 이미지의 연결 구조 내에서 학습해야 할 미지의 파라미터 수가 작다는 의미입니다.
* 제어이론 관점에서는, 이미 측정 혹은 추정을 통해 알려진 상태 변수(state variable)가 소수이므로, 이후 제어해야 할 변수(control variable)도 소수입니다.
* 의사결정 모형 관점에서는, 알려진 계수(coefficient)의 수가 적기 때문에, 최적화를 통해 찾아야 할 의사결정 변수(decision variable)도 적습니다.

듀얼리티(duality)란?

선형 모형에서는 하나의 문제를 두 가지 방식으로 바라보는 구조가 자주 등장합니다. 이를 듀얼리티라고 부릅니다.

* 기하학적으로는, 2차원 공간에서 직사각형과 마름모는 서로 듀얼입니다.
  원뿔 곡선(conic section)에서는 타원(ellipse)과 쌍곡선(hyperbola)이 서로 듀얼이며, 이 둘의 경계에서 포물선(parabola)이 등장합니다.

* 대수적으로는, 시스템의 구조를 규정하는 집합적 관계(collectively hidden structural relationship)에서 나타나는 시스템 구성요소들 사이의 이중성을 의미합니다.

예를 들어 다음과 같은 쌍들이 대표적입니다:

* 상태 변수(state variable) ↔ 제어 변수(control variable)
* 추정된 변수(estimated variable) ↔ 추정에 사용되는 변수(estimating variable)
* 상수(constants) ↔ 변수(variables)

이러한 시스템의 듀얼리티를 해석하려면, 우리는 반드시 다음 질문에 답해야 합니다.

우리는 이 시스템에서 어떤 정보를 더 확실히 알고 있다고 말할 수 있는가?

예시:

* 물리학:
  물체의 위치(location)는 관찰로 직접 알 수 있지만, 속도(velocity)는 여러 시점 간의 차이로 유도됩니다. 어느 쪽이 더 확실한 정보일까요?

* 경제학:
  개인이나 산업의 소득(income)은 주어진 데이터로 측정할 수 있지만, 상대적 가치(relative weight)는 시장 내 상호작용 속에서만 드러납니다. 무엇이 더 본질적인가요?

* 철학:
  육체(body)는 감각적으로 접근할 수 있지만, 정신(mind)은 간접적입니다. 인간을 규정하는 데 무엇이 더 핵심적인 속성일까요?

* 생물학:
  유전적 요소(nature)와 환경적 요소(nurture)는 모두 인간의 특성을 형성하지만, 어느 쪽이 결정적으로 작용하는지를 판단하는 것은 여전히 논쟁적입니다.

이러한 판단은 단지 데이터의 문제가 아니라, 우리가 세상을 어떻게 이해하고자 하는가에 대한 철학적 태도를 반영합니다.
선형대수학에서의 듀얼리티 개념은 단순한 계산 기술이 아니라, 모형을 해석하고 구조를 파악하는 방식의 선택입니다.
이는 학문뿐 아니라 실제적인 의사결정과 가치 판단에서도 중요한 원리가 됩니다.