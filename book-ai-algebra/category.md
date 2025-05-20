

Terminology and Notations

- Adjoint functor
- Hasse Diagram : Partially ordered set (poset)
- Commutative Diagram

## "Different expressions, same meaning."

Category theory is a language for comparing different forms of expression to identify structures that are essentially the same. It extends set theory through functional thinking and abstraction, focusing on **relationships and composition** rather than individual elements. For instance, rather than treating **equality** (`=`) as the central notion, category theory replaces it with a more flexible concept: **equivalence**.

* **Isomorphism** means two objects are completely identical in structure — there exists a one-to-one and onto functor with an inverse.
* **Equivalence** means two categories may look different, but their essential behavior is indistinguishable.

If a functor $F : \mathcal{C} \to \mathcal{D}$ is **full**, **faithful**, and **essentially surjective**, then $\mathcal{C} \simeq \mathcal{D}$. In other words, the two categories are **the same in meaning**, though different in appearance.

| Categorical Property   | Set-Theoretic Analogy                | Interpretation                                  |
| ---------------------- | ------------------------------------ | ----------------------------------------------- |
| Full                   | Surjective on morphisms              | Preserves **all relationships**                 |
| Faithful               | Injective on morphisms               | **Precisely distinguishes** relationships       |
| Essentially Surjective | Up to isomorphism, everything is hit | Captures the **existential meaning** of objects |


### Objects and Relationships

In category theory:

* **Objects** can be interpreted as **source** and **target**, often thought of as **nodes** in a diagram.
* **Morphisms** (or arrows) describe **relationships** between objects.
* A **functor** maps one category to another, preserving identity morphisms and composition of morphisms.
* A **category** is a collection of objects and morphisms satisfying associativity and identity laws.


### Equivalence of Categories

The statement “Two categories $\mathcal{C}$ and $\mathcal{D}$ are equivalent” means:

There exist two functors $F: \mathcal{C} \to \mathcal{D}, \quad G: \mathcal{D} \to \mathcal{C}$ such that $G F \cong \mathrm{id}_{\mathcal{C}}, \quad F G \cong \mathrm{id}_{\mathcal{D}}$

**Example:**
The category of finite-dimensional real vector spaces and the category of real vector spaces with a fixed basis are equivalent, even though one emphasizes linear maps and the other emphasizes coordinate representations.


### Dual of a Category

For any category $\mathcal{C}$, its **dual category** $\mathcal{C}^{\mathrm{op}}$ is defined by reversing the direction of **all** morphisms: Every morphism $f: A \to B$ in $\mathcal{C}$ becomes $f^{\mathrm{op}}: B \to A$ in $\mathcal{C}^{\mathrm{op}}$.

**Example:**
In the category **Pos** of partially ordered sets, the dual category corresponds to reversing the order. That is, $(P, \le)$ becomes $(P, \ge)$.

### Dually Equivalent Categories

The statement “Two categories $\mathcal{C}$ and $\mathcal{D}$ are dually equivalent” means

$$
\mathcal{C} \simeq \mathcal{D}^{\mathrm{op}}
\quad\text{or equivalently}\quad
\mathcal{C}^{\mathrm{op}} \simeq \mathcal{D}.
$$

**Example:**
The category of affine schemes **Aff** is dually equivalent to the category of commutative rings **CRing**:

$$
\mathbf{Aff} \simeq \mathbf{CRing}^{\mathrm{op}}.
$$

This reflects how **geometric** objects correspond contravariantly to **algebraic** objects — a core insight of algebraic geometry.


### Self-dual Category

Self-duality is a special case of dual equivalence:

$$
\text{self-duality} \;\subset\; \text{dual equivalence}.
$$

A category $\mathcal{C}$ is **self-dual** if it is equivalent to its own dual:

$$
\mathcal{C} \simeq \mathcal{C}^{\mathrm{op}}.
$$

**Example:**
The category **FdVectₙ** of finite-dimensional vector spaces over a field is self-dual, because every linear space is naturally isomorphic to its dual via the Riesz representation theorem. Another example is the category of Boolean algebras **Bool**, which is self-dual through negation and De Morgan’s laws.

