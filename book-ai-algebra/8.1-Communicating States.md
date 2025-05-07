
> “A state is not truly reachable unless it can reach back — **fairness** lies in **mutual** paths.”

## Relation

### Non-equivalence relation as a very common but unfair relation

> “Asymmetry reveals power, not understanding.”

In many social, economic, or logical structures, relations are:

- Not reflexive: I might not understand myself.
    
- Not symmetric: If I understand you, it doesn't mean you understand me.
    
- Not transitive: Even if I understand you, and you understand Sam, I may not understand Sam.
    

Such relations are directional, asymmetric, and often hierarchical, reflecting power, ignorance, or miscommunication — thus, structurally unfair.

---

### Equivalence relation as a very special but fair relation

>“True fairness begins when I understand you, and you understand me.”

In contrast, an equivalence relation ensures mutuality, balance, and internal coherence. It defines a structure where **all** members of a group communicate equally and symmetrically.

#### Logical example

- Reflexivity: I understand myself.
    
- Symmetry: If I understand you, you understand me.
    
- Transitivity: If I understand you, and you understand Sam, then I understand Sam.
    

#### Algebraic example: Congruence modulo 3

- Reflexive: 0 ≡ 0, 1 ≡ 1, 2 ≡ 2 mod 3
    
- Symmetric: 1 + 2 ≡ 0 ≡ 2 + 1 mod 3
    
- Transitive: If 0 ≡ 3 and 3 ≡ 6, then 0 ≡ 6 mod 3
    

Note: Group structure implies closure and invertibility under a binary operation, which yields equivalence relations on cosets or orbits — not necessarily between individual elements.  
Congruence modulo 3 partitions ℕ into equivalence classes (e.g. 0 ≡ 3 ≡ 6, 1 ≡ 4 ≡ 7, etc.).

---

## Communication in Markov Chains

>“Communication is not just connection, but mutual reachability across time.”

**Definition**: In **a finite-state Markov chain**, state $i$ **communicates** with state $j$ if there exists some $n \geq 0$ such that:

- $P^n(i, j) > 0$, and
    
- $P^m(j, i) > 0$ for some $m$
    

This communication relation satisfies:

- Reflexivity: Each state eventually returns to itself
    
- Symmetry: If $i$ can reach $j$ and $j$ can reach $i$
    
- Transitivity: If $i \leftrightarrow j$ and $j \leftrightarrow k$, then $i \leftrightarrow k$
    

Therefore, communication is an equivalence relation on the state space.  
The state space is partitioned into **communication classes** — mutually reachable subsets that determine long-term dynamics.

---

### Cross-sectional Fairness: Equivalence through Group Action

>“In an Abelian world, no action is dominant — every action is equally valid in every direction.”

In abstract algebra, group actions define structural fairness by letting group elements “act” on a set. If a group $G$ acts on a set $X$, we say:

$$x \sim y \quad \text{if there exists } g \in G \text{ such that } g \cdot x = y$$

This relation is:

- Reflexive ($e \cdot x = x$)
    
- Symmetric (if $g \cdot x = y$, then $g^{-1} \cdot y = x$)
    
- Transitive (composition of group actions)
    

In particular, Abelian groups (where $a + b = b + a$) such as $(\mathbb{Z}_n, +)$ reinforce this symmetry.

Each **orbit** under a group action forms a class of equivalent configurations — just as communication classes in Markov chains represent mutually reachable states.  Thus, **no element has a privileged direction of action over another** within each orbit — a kind of “structural justice” within class, even if there may be inequality across different orbits.

---

### Time-Sensitive Fairness: 조삼모사(朝三暮四)

>“To those with finite lives, timing reveals the meaning of fairness.”

In the fable _조삼모사_ (three in the morning, four in the evening), a monkey protests that receiving three chestnuts in the morning and four in the evening is not the same as four in the morning and three in the evening — despite the total being seven in both.

The monkey is often mocked as foolish, but in fact may be rational: For mortals with finite lives, time matters. Receiving earlier is better than later, because future utility is uncertain and discounted.

Just as in discounted utility models in economics or stochastic dominance in finance, the **timing** of allocation affects perceived fairness — even when totals are equal.

Hence:

- Fairness should be not only structural (symmetry, equivalence), but also temporal
    
- Even in Markov chains or stochastic systems, **when** transitions occur can matter as much as **whether** they occur
