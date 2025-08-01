## Latent Dirichlet Allocation (LDA)


목적: NLP 에서의 probabilistic generative model

Generative Process

- 문서 $d$에 대해:
    1. 각 문서 $d$는 topic 분포 $\theta_d \sim \mathrm{Dir}(\alpha)$에서 샘플됨 (핵심가정)
    2. 각 topic $k$는 word 분포 $\phi_k \sim \mathrm{Dir}(\beta)$에서 샘플됨 (핵심가정)
    3. 문서 $d$의 각 단어 $w_{dn}$에 대해:
        - topic $z_{dn} \sim \mathrm{Multinomial}(\theta_d)$ 선택
        - word $w_{dn} \sim \mathrm{Multinomial}(\phi_{z_{dn}})$

이 모형은 관측된 단어들의 집합으로부터 문서별 topic 구성과 topic별 단어 분포를 역추정(infer)합니다.

**Dirichlet 이름 출처:**  
Dirichlet 분포는 독일의 수학자 Johann Peter Gustav Lejeune Dirichlet (1805–1859)의 이름을 따온 것입니다. 다만, LDA라는 전체 모델은 2003년 Blei, Ng, Jordan의 논문(NeurIPS 2003)에 의해 제안된 현대적 생성 모델입니다. Dirichlet은 단지 prior로 사용되는 distribution의 이름일 뿐입니다.

## Linear Discriminant Analysis (또는 Fisher's LDA)의 본질

Linear Discriminant Analysis는 

목적: supervised learning classification (e.g. Singular Value Decomposition)

방법: 기본적으로 클래스 간 분산(between-class scatter)을 최대화하고, 클래스 내 분산(within-class scatter)을 최소화하는 **linear projection**을 찾습니다.

**핵심 가정:**

- 각 클래스의 데이터는 **공통된 공분산 행렬을 갖는 Gaussian 분포**를 따른다.
- 이 경우, separating boundary는 선형 결정경계(linear decision boundary)가 됩니다.
    

**수학적 목적 함수:**

$\mathbf{w}^* = \arg\max_{\mathbf{w}} \frac{\mathbf{w}^\top S_B \mathbf{w}}{\mathbf{w}^\top S_W \mathbf{w}}$

- $S_B$: 클래스 평균 간 분산 행렬 (between-class scatter)
- $S_W$: 클래스 내부 분산 행렬 (within-class scatter)

