title: Duality Lists
---

## Self-Duality in Category Theory

In category theory, if a category $\mathcal{C}$ is **self-dual**, then duality represents a **correspondence** between properties of $\mathcal{C}$ and properties of its opposite category $\mathcal{C}^{\mathrm{op}}$. This means that:

* If a statement is **true** in $\mathcal{C}$, then its **dual statement** is also true in $\mathcal{C}^{\mathrm{op}}$.
* Likewise, if a statement is **false** in $\mathcal{C}$, its dual must be false in $\mathcal{C}^{\mathrm{op}}$.
* In essence, duality asserts that truth is invariant under reversal of morphisms.


## Duality in Common Contexts

The concept of duality appears widely across disciplines, often pairing between opposites that reflect deeper structural truths.

### Philosophy

* **Mind–Body Dualism**: The mind and body are distinct yet interrelated, sometimes seen as non-reducible to each other. Duality here represents the tension between **mental** and **physical**, or **subject** and **object**.
* **Yin–Yang** (Chinese philosophy): A system of opposing but complementary forces that interdependently drive change and harmony.

### Mathematics

* **General notion**: A duality often maps one concept, theorem, or structure to another in a one-to-one, reversible way — often via an involution. If the dual of $A$ is $B$, then the dual of $B$ is $A$.

* **Examples**:

  * *Euclidean Geometry*: The conjugate hyperbola of a hyperbola shares its asymptotes but lies in opposite sectors of the plane.
  * *Projective Geometry*: The dual curve of a plane curve $C$ is the set of all lines tangent to $C$, forming a curve in the dual projective plane.
  * *Optimization Theory*:

    * Every optimization problem has a **primal** and a **dual** formulation.
    * **Weak duality**: The value of the dual is a lower bound on the primal.
    * **Strong duality**: Under convexity and constraint qualification, primal and dual values coincide.
    * The **duality gap** measures how far apart primal and dual solutions are.

### Physics

* **Complementarity Principle**: Introduced by Niels Bohr, this principle states that certain physical quantities — such as wave and particle descriptions — are mutually exclusive but jointly necessary for a full description.

* **Quantum Mechanics**:

  * **Wave–Particle Duality**
  * **Heisenberg Uncertainty Principle**

* **Electromagnetism**:

  * Duality arises from the symmetry between electric and magnetic fields, particularly under Lorentz transformations in special relativity.

  | Electric Concept| Magnetic Dual|
  | -------------------------------------- | -------------------------------------- |
  | Electric Field ($\mathbf{E}$)| Magnetic Field ($\mathbf{H}$)|
  | Electric Flux Density ($\mathbf{D}$) | Magnetic Flux Density ($\mathbf{B}$) |
  | Electric Potential| Magnetic Potential|
  | Gauss’s Law (Electric)| Gauss’s Law (Magnetic)|
  | Faraday’s Law| Ampère’s Law (with Maxwell correction) |

* **Control Theory**: **Controllability** and **Observability** are dual properties under state-space transformation.

### Electrical Engineering

Duality is applied by **interchanging voltage and current**, or series and parallel configurations. This produces structurally equivalent but functionally dual systems.

| Concept                       | Dual Concept                  |
| ----------------------------- | ----------------------------- |
| Voltage ($V$)| Current ($I$)|
| Voltage Division              | Current Division              |
| Series Circuit                | Parallel Circuit              |
| Resistance ($R$)            | Conductance ($G$)           |
| Capacitance ($C$)           | Inductance ($L$)            |
| Impedance ($Z$)             | Admittance ($Y$)            |
| Kirchhoff's Voltage Law (KVL) | Kirchhoff's Current Law (KCL) |

These relationships form the basis for modeling and analyzing **dual** networks in **linear** systems.