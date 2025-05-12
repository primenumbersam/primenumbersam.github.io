
수학적 최적화를 '프로그래밍'이라고 부르는 것은 컴퓨터 프로그래밍과 직접적인 관련은 없지만, 수학적 최적화 문제를 해결하기 위한 체계적인 '계획' 또는 '절차'를 의미합니다. 특히, 2차 세계대전 이후 조지 단치그(George Dantzig)가 선형 계획법 (linear programming)을 개발하면서 프로그래밍이란 용어가 널리 사용되었습니다. 당시 미국 국방부에서 군사 작전, 훈련, 물자 수송 등의 계획을 수립하는 데 이 방법이 활용되었습니다.

### 기원: George Dantzig와 베를린 공수 작전 (The Berlin Airlift)

George Dantzig는 제2차 세계대전 직후 미 공군에서 근무하던 중 **선형계획법(Linear Programming)**을 개발하게 되었습니다. 이 개념이 탄생하게 된 역사적 계기 중 하나는 바로 **베를린 공수 작전(1948–1949)**이었습니다.

- 전쟁 이후 소련이 서베를린에 대한 **육로 봉쇄**를 단행하자, 미국과 영국을 비롯한 서방 연합군은 **항공편을 통해 식량과 연료, 생필품을 수송**하기로 결정합니다.
    
- 이 작전은 매일 수백 대의 항공기를 운용해야 했고, **제한된 비행기 수, 활주로, 연료, 조종사, 시간**이라는 여러 제약 조건 속에서 효율적으로 물자를 운반해야 하는 상황이었습니다.
    
- 당시 국방부에서 일하던 Dantzig는 **이 복잡한 자원 배분 문제를 수학적으로 최적화할 수 없을까**라는 요청을 받게 되었고, 이 문제를 **선형 함수의 최적화 문제로 수학적으로 형식화**하면서 선형계획법이 등장하게 된 것입니다.
    

### Key Application Areas of Linear Programming

|Domain|Examples|
|---|---|
|**Logistics and Transportation**|Vehicle routing, airline scheduling, supply chain optimization|
|**Operations Research**|Resource allocation, production planning, facility location|
|**Economics**|Leontief Input-Output Model, utility maximization, shadow pricing|
|**Finance**|Portfolio optimization (basic LP or LP-relaxed), risk minimization|
|**Energy Systems**|Grid optimization, power generation and dispatch|
|**Manufacturing**|Cutting stock problem, workforce scheduling, inventory management|
|**Telecommunications**|Bandwidth allocation, network flow optimization|
|**Military and Defense**|Mission planning, logistics under constraint|
|**Health and Medicine**|Optimal allocation of medical resources, treatment planning|
|**AI and ML (Modern)**|Linear SVMs, constrained learning problems, LP relaxations for ILPs|

### Core Idea of Linear Programming

**Goal**:  
Maximize or minimize a **linear objective function** (e.g., profit, cost, delivery volume)  
Subject to a system of **linear equality and inequality constraints** (e.g., capacity, time, resource limits)

Mathematically:

$$\text{maximize (or minimize) } \mathbf{c}^T \mathbf{x} \quad \text{subject to} \quad A \mathbf{x} \leq \mathbf{b},\quad \mathbf{x} \geq 0$$


