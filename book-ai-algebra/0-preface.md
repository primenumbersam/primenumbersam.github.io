---
title: Preface
---

## Prologue

Let us not fall into the error of personifying objects.
**People are subjects; mathematics is a tool.**

We do not learn mathematics because it speaks to us,
but because **it helps us express our own questions more beautifully and precisely**.

This book is not about solving someone else’s problems.
It is about discovering **how to express your own questions**—clearly, honestly, and elegantly—through the language of mathematics.

## Contents

> 수학의 자기 완결성? Nope. 수학의 효용성과 효율성.
> Global Flow: Basic Grammar, Unsupervised Learning, Supervised Learning
> Sub Flow: "Famous Problem -> Key Assumptions -> Python -> Interpretation".
> Approach: the practical, visualization-focused.

9 Optimization: Linear Programming
- Duality

1 Linear Equations: Linear Models in Economics and Engineering
- Systems of linear equations
- Applications of Linear systems
- Linear Models in Business, Science, and Engineering

2 Matrix Algebra : Computer Models in Aircraft Design
- The Leontief Input-Output Model
- Applications to Computer Graphics


3 Determinants: Random Paths and Distortion
- Properties of Determinants, Volume

8 Geometry of linear spaces
- The Platonic Solids
- Polytopes

6 Orthogonality and Least Squares : GPS Navigation
- Orthogonal Projection


4 Linear Spaces: Control Systems
The Geometry of Solution Spaces: Vector Spaces and Subspaces

- Rank-Nullity theorem
- Applications to **Difference** Equations
- Applications to Markov Chains

5 Eigenvectors
- Dynamic systems and Spotted Owls
- Applications to **Differential** equations

-   **Famous Problem:** Analyzing the long-term behavior of a system or process, like population distribution changes or Markov chains. (Eigenvectors show stable states).
-   **Key Assumptions:** The matrix A represents the transition or transformation rules of the system. Eigenvectors represent directions that are only scaled by the transformation.
-   **Python Visualization:** Visualizing eigenvectors (direction) and eigenvalues (magnitude of scaling) for a 2x2 matrix. Simulating the step-by-step application of a transition matrix (e.g., Lay's Markov chain example) and showing convergence to the eigenvector.
-   **Interpretation Summary:** Eigenvectors reveal the fundamental directions or components of a linear transformation, and eigenvalues tell us the factor by which variance is scaled in those directions. This is key to understanding PCA.


10 Finite-State Markov Chains : **Google's PageRank**
- Steady-state vector
-   **Famous Problem:** Solving very large systems of linear equations that arise from complex models or massive datasets (e.g., in finite element methods or network analysis). (Direct methods like Gaussian Elimination can be too slow or memory-intensive).
-   **Key Assumptions:** Iterative methods approach the true solution Ax=b through successive approximations [[Strang 7.4]].
-   **Python Visualization:** Implementing a simple iterative method (e.g., Jacobi or Gauss-Seidel, or gradient descent for Ax=b). Visualizing the convergence of the solution vector over iterations.
-   **Interpretation Summary:** For very large problems, iterative methods provide a practical way to find approximate solutions to linear systems, essential in fields like numerical simulation and large-scale optimization (which underlies many machine learning algorithms).

- **구글 페이지랭크**는 개념은 **스탠포드 대학**에서 연구되었으며, 구글의 창립자인 **래리 페이지**와 **세르게이 브린**이 개발하였다. 구글의 탄생 배경이 되는 중요한 개념이다.
- 페이지랭크는 웹 페이지의 **인기도**를 측정하는 알고리즘으로, 웹 페이지 간의 **링크 구조**를 기반으로 한다. 페이지랭크는 웹 페이지의 **상대적 중요성**을 평가하기 위해 사용되며, 이는 검색 엔진의 **효율성**을 높이는 데 기여한다.
- 첫 번째 웹페이지의 **파워 인덱스**는 해당 페이지가 **인용된 전체 갯수**로 정리할 수 있다.
- 파워 인덱스는 웹 페이지의 **인용 횟수**를 기반으로 하며, 이는 페이지의 **신뢰성**을 나타낸다.
- 각 웹 페이지는 다른 페이지들로부터 **인용**을 받을 수 있으며, 이 인용의 수가 많을수록 파워 인덱스는 **높아진다**.
- 파워 인덱스는 웹 페이지의 **상대적 위치**를 결정하는 데 중요한 역할을 한다.
- 페이지랭크는 **행렬** 형태로 표현할 수 있다.
- 각 웹 페이지의 인용 관계를 나타내는 **행렬**을 구성하여, 이를 통해 파워 인덱스를 계산한다.
- 이 행렬은 **대칭 행렬**로, 각 페이지 간의 인용 관계를 명확히 나타낸다.
- 행렬의 **고유값**을 통해 각 페이지의 파워 인덱스를 도출할 수 있다.
- 대칭 행렬은 **방향성이 없는 네트워크**를 나타낸다.
- 방향성이 있는 경우, **디렉티드 네트워크**로 표현된다.
- 이러한 행렬은 각 노드 간의 **관계를 명확히** 나타내는 데 기여한다.
- 행렬의 **구조**는 네트워크의 **특성을 이해**하는 데 중요한 요소이다.


7 Symmetric matrices and Quadratic Forms : Multichannel Image Processing
- SVD

-   **Famous Problem:** Analyzing the spread and correlation within a dataset, represented by the covariance matrix.
-   **Key Assumptions:** The covariance matrix is symmetric and (often) positive semidefinite or positive definite. Its eigenvectors point in directions of maximum variance (principal components).
-   **Python Visualization:** Calculating the covariance matrix for a 2D/3D dataset using `numpy.cov`. Visualizing the data scatter plot. Overlaying the eigenvectors of the covariance matrix scaled by the eigenvalues to show the principal axes of variance (linking back to Unit 2.1/2.2).
-   **Interpretation Summary:** The covariance matrix summarizes feature relationships. Positive definiteness is a key property related to variance and optimization objectives. Eigenanalysis of the covariance matrix reveals the principal components.

Dimensionality Reduction & Data Compression: Singular Value Decomposition (SVD)
- Famous Problem: Image compression or reducing the dimensionality of a dataset while retaining most information (Principal Component Analysis).
- Key Assumptions: Any matrix can be decomposed into a product of three matrices (U, Σ, V^T). The singular values in Σ capture the "importance" of each dimension.
- Python Visualization: Performing SVD on a simple data matrix or grayscale image using numpy.linalg.svd. Showing the singular values. Reconstructing the matrix/image using only the top k singular values and vectors, visualizing the compressed result. Illustrating the four fundamental subspaces using SVD.
- Interpretation Summary: SVD provides a powerful way to understand a matrix's structure, identify its rank, find orthogonal bases for the fundamental subspaces, and approximate the matrix with lower rank, directly enabling techniques like PCA for dimensionality reduction.






### **Applied Linear Algebra: Practical Modules**

- 9 Linear Programming **Optimization and Linear Programming**  
      Linear inequality problems in economics, resource allocation, and engineering  
      • Duality and economic interpretation
    
- 8 **Geometric Structures of Linear Spaces**  
      Visualizing algebra through Platonic solids and polytopes  
      • Foundations of convexity and feasibility
    
- 1 **Linear Equations**  
      Economic input-output analysis and physical system simulations  
      • Business, Science, and Engineering applications
    
- 2 **Matrix Algebra in Computation and Graphics**  
      How matrices govern structural transformations  
      • Leontief Model and Computer-Aided Design
    
- 3 **Determinants and Volume-Based Intuition**  
      Orientation, distortion, and random paths in multi-dimensional spaces  
      • From row operations to volume calculation
    
- 4 **Linear Spaces**  
      Abstract structure behind control systems and recursive dynamics  
      • Rank-Nullity Theorem  
      • **Difference** equations and Markov chains
    
- 5 **Eigenvectors in Dynamical Systems**  
      Growth, decay, and stability in nature and engineering  
      • **Differential** equations and population models
    
- 10 **Finite-State Markov Chains and PageRank**  
      How Google ranks the internet using steady-state vectors
    
- 6 **Orthogonality and Least Squares**  
      From projections to GPS: minimizing errors in systems
    
- 7 **Symmetric Matrices and Quadratic Forms**  
      Multichannel image processing and data compression  
      • Singular Value Decomposition (SVD)
    
---

Mathematical Modelling

Objective: **Explain** the complex real-world system and **Predict** the future behavior of the system.

Process:
- **State** the Problem
	- **Clarify** the problem (5W1H): problem? why (objective)? who (observer)? where (area)? what (system)? when (dynamics)? how (criteria)? 
	- **Simplify** the problem: simplify the problem enough to make it mathematically tractable, by making critical assumptions and by naming and identifying the variables.
- **Formulate** the problem: express the problem in a systematic way.
- **Solve** the formulated problem : derive the mathematical conclusion
- **Interpret** the solved problem : derive the meaningful conclusion
- **Test** the conclusion by making a prediction



