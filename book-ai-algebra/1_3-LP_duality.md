---
title: Duality
subtitle: Primal form vs. Dual form
---

## Duality

In a canonical linear programming problem, the primal (maximization) problem is associated with its dual (minimization) problem.

### Problem Statement

We revisit the same production planning problem from the previous section. This time, instead of maximizing profit directly by choosing production quantities, we ask a different question:

> What is the minimum **total** cost one would have to pay per unit of resource (machine hours and raw material) to cover the required profits per product?

This alternative formulation is called the **dual problem** of the original (primal) linear programming problem.

### Formulate the Dual Problem

Let  
$u$ = price per unit of machine time  
$v$ = price per unit of raw material

Objective:  
Minimize the total cost of resources:

$$W = 180u + 160v$$

Subject to (each product must be worth at least its profit):

$$\begin{cases} 3u + 2v \geq 50 & \text{(product A)} \\ 2u + 3v \geq 40 & \text{(product B)} \\ u \geq 0,\quad v \geq 0 & \text{(non-negativity)} \end{cases}$$

### Solve with Python and Interpret

Solution to the dual:

- $u = 14$
- $v = 4$
- Minimum total cost $W = 3160$


Interpretation:

- This result confirms the **duality theorem**: the maximum profit from the primal form equals the minimum resource cost in the dual form.
    
- The shadow prices (dual variables) represent the **marginal value** of each resource:
    - $u = 14$ means each additional unit of machine time increases potential profit by $14.
    - $v = 4$ means each additional kg of raw material increases potential profit by $4.
        
- These values are also known as **dual prices** or **shadow prices**, and they help in **resource pricing, sensitivity analysis**, and **economic interpretation**.
    

## The Duality Theorem

Let the **primal** linear program be:

**Maximize** $Z = \mathbf{c}^T \mathbf{x}$, Subject to $A \mathbf{x} \leq \mathbf{b}, \quad \mathbf{x} \geq 0$

Its **dual** is:

**Minimize** $W = \mathbf{b}^T \mathbf{y}$, Subject to $A^T \mathbf{y} \geq \mathbf{c}, \quad \mathbf{y} \geq 0$

Then the **Duality Theorem** states:

If either the primal or the dual problem has a solution, then so does the other, and the extremal values are equal:
$$\max_{\mathbf{x}} \{\mathbf{c}^T \mathbf{x} \mid A\mathbf{x} \leq \mathbf{b}, \ \mathbf{x} \geq 0 \} = \min_{\mathbf{y}} \{\mathbf{b}^T \mathbf{y} \mid A^T\mathbf{y} \geq \mathbf{c}, \ \mathbf{y} \geq 0 \}$$

**In our example**:

- Primal maximum profit $Z = 3160$
- Dual minimum cost $W = 3160$  
    → Duality theorem holds exactly.

## Complementary Slackness

| Primal Problem| Dual Problem|
| ----- | ----- |
| Maximize $Z = \mathbf{c}^T \mathbf{x}$  <br>Subject to: <br>$A \mathbf{x} \leq \mathbf{b}, \quad \mathbf{x} \geq 0$ | Minimize $W = \mathbf{b}^T \mathbf{y}$ <br>Subject to: <br>$A^T \mathbf{y} \geq \mathbf{c}, \quad \mathbf{y} \geq 0$ |

The Complementary Slackness conditions are **necessary and sufficient** for optimality **when** both the primal and dual problems have feasible solutions. These conditions can be stated as follows:

* For each **primal constraint**:
  $y_i \cdot \left(b_i - (A \mathbf{x})_i\right) = 0$
  That is, if the dual variable $y_i > 0$, then the corresponding primal constraint must be **binding** (i.e., holds with equality).

* For each **dual constraint**:
  $x_j \cdot \left((A^T \mathbf{y})_j - c_j\right) = 0$
  That is, if the primal variable $x_j > 0$, then the corresponding dual constraint must also be **binding**.

In plain terms:

> If a **dual constraint is slack**, then the corresponding **primal variable is zero**.
> If a **primal constraint is slack**, then the corresponding **dual variable is zero**.

**In our example**:

- Both constraints in the primal are binding (i.e., satisfied as equalities)
  → Hence, the corresponding dual variables $u$ and $v$ must be **strictly positive**.
- Both primal variables $x$ and $y$ are strictly positive
  → Thus, both dual constraints are also binding.
- Therefore, **the Complementary Slackness conditions are fully satisfied**.

