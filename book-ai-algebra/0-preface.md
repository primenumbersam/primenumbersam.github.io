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


10 Finite-State Markov Chains : Google's PageRank
- Steady-state vector
-   **Famous Problem:** Solving very large systems of linear equations that arise from complex models or massive datasets (e.g., in finite element methods or network analysis). (Direct methods like Gaussian Elimination can be too slow or memory-intensive).
-   **Key Assumptions:** Iterative methods approach the true solution Ax=b through successive approximations \[Strang 7.4\].
-   **Python Visualization:** Implementing a simple iterative method (e.g., Jacobi or Gauss-Seidel, or gradient descent for Ax=b). Visualizing the convergence of the solution vector over iterations.
-   **Interpretation Summary:** For very large problems, iterative methods provide a practical way to find approximate solutions to linear systems, essential in fields like numerical simulation and large-scale optimization (which underlies many machine learning algorithms).

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



