---
title: Food choice and Nutritional balance
subtitle: Determinacy of a Linear system
---

## Scientific Motivation

In order to survive, an organism must consume a set of **essential nutrients**.
Because no single food contains all the necessary nutrients in sufficient quantity, a **combination of foods** is required to maintain **homeostasis**.
This motivates the question:

> How can we combine available foods to satisfy minimum daily nutritional requirements?

The goal of this section is to **translate a biological constraint** into a **system of linear equations**, and to analyze the feasibility of different cases:

* exactly determined system
* overdetermined system
* underdetermined system

### What Is an Organism?

The term *organism* refers to a living system—often characterized by metabolic activity, internal regulation, and structural complexity.
From a **reductionist** perspective, however, an organism can be seen as a system composed mostly of just a few atomic elements:
**carbon (C), hydrogen (H), oxygen (O), and nitrogen (N).**
These are the backbone of what we classify as **organic molecules**, in contrast to **inorganic** substances, which are not primarily composed of C, H, O, or N.

That said, the line between “organic” and “inorganic” is not absolute—it is a **gray area**, defined not by nature itself, but through **human standardization** and consensus.

### What Is a Nutrient?

From the perspective of molecular chemistry, nutrients are molecules made of atoms bonded together—typically through covalent or ionic bonds.
Major categories of nutrients include:

* **Fat (fatty acids)**: carbon–hydrogen chains with a carboxylic group (COOH)
* **Carbohydrates**: molecules composed mainly of C, H, and O
* **Proteins**: nitrogen-containing compounds linked by peptide bonds
* **Minerals**: micronutrients not based on C–H–O–N, often including ions like Fe²⁺, Ca²⁺, Zn²⁺

We assume here that to sustain life, a person must consume **a fixed minimum amount (in grams)** of each nutrient per day—say, for example, one unit of **fat, carbohydrate, protein, and mineral**.


## Case 1: Exactly Determined System

Suppose a person can choose from exactly **4 foods**: Bread, Potato, Steak, and Salad.
Let each food contribute a known amount of each of the 4 nutrients per 100g.
If the daily nutritional requirement is known and fixed, the question becomes:

> Can we find exactly **one solution**—one fixed combination of food quantities—to meet the nutrient requirements?

This is a **square system**:

* 4 variables (food quantities)
* 4 equations (nutrient requirements)
  If the nutrient matrix is invertible, a **unique solution** exists.
  In this case, the person **must** eat precisely that fixed combination every day.


## Case 2: Overdetermined System

Now suppose an additional food is available—**Sandwich**.
There are now **5 food options**, but still only 4 nutrient constraints.

This leads to an **overdetermined system**:

* 5 variables
* 4 equations

Now there are **infinitely many possible food combinations** that can satisfy the nutritional goal.
The system may still have a solution if the extra food doesn't conflict with the requirements.
It is **flexible**, allowing for choice, taste, and substitution.


## Case 3: Underdetermined System

Suppose only **2 foods** are available—Bread and Potato.

Now we have:

* 2 variables
* 4 equations

This is an **underdetermined system**.
It is **impossible** to satisfy all nutrient constraints using only two foods, unless by some coincidence the two foods form a spanning set for the nutritional space.
In general, no combination of these two foods alone will meet the minimum nutrient requirements.


## Conclusion

This simple biological system illustrates the essence of **linear systems of equations**:

* Whether a solution exists depends on the **relationship between equations and unknowns**.
* Whether the solution is **unique** or **nonexistent** can often be deduced from matrix structure alone.

By modeling a nutritional constraint as a matrix equation, we move from **biology to algebra**, and gain insight into what is possible, impossible, or flexible in real-world systems.

## 2D Coordinate Geometry

To further simplify the discussion of the three types of linear systems introduced above, we visualize each case in a two-dimensional coordinate system.

* In the first plot (**Exactly Determined**), two lines intersect at a single point, representing a unique solution.
* In the second plot (**Overdetermined**), three lines may not all intersect at a single point, but may approximate a common intersection — a solution may exist, but only under specific consistency conditions.
* In the third plot (**Underdetermined**), only one line is present, representing infinitely many solutions along the line.

```{python}
import numpy as np
import matplotlib.pyplot as plt

# Setup figure
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
titles = ["Exactly Determined", "Overdetermined", "Underdetermined"]

# Case 1: Exactly determined (2 equations, 2 unknowns)
axs[0].set_title(titles[0])
x = np.linspace(0, 10, 200)
y1 = (6 - 2 * x) / 1  # 2x + y = 6
y2 = (8 - 1 * x) / 2  # x + 2y = 8
axs[0].plot(x, y1, label='2x + y = 6')
axs[0].plot(x, y2, label='x + 2y = 8')
axs[0].set_xlim(0, 5)
axs[0].set_ylim(0, 5)
axs[0].legend()
axs[0].grid(True)

# Case 2: Overdetermined (3 equations, 2 unknowns)
axs[1].set_title(titles[1])
y3 = (6 - 2 * x) / 1       # 2x + y = 6
y4 = (8 - 1 * x) / 2       # x + 2y = 8
y5 = (7 - 1 * x) / 1       # x + y = 7
axs[1].plot(x, y3, label='2x + y = 6')
axs[1].plot(x, y4, label='x + 2y = 8')
axs[1].plot(x, y5, label='x + y = 7')
axs[1].set_xlim(0, 5)
axs[1].set_ylim(0, 5)
axs[1].legend()
axs[1].grid(True)

# Case 3: Underdetermined (1 equation, 2 unknowns)
axs[2].set_title(titles[2])
y6 = (6 - 2 * x) / 1       # 2x + y = 6
axs[2].plot(x, y6, label='2x + y = 6')
axs[2].set_xlim(0, 5)
axs[2].set_ylim(0, 5)
axs[2].legend()
axs[2].grid(True)

# Final adjustments
for ax in axs:
    ax.set_xlabel('Bread (x)')
    ax.set_ylabel('Potato (y)')

plt.tight_layout()
plt.show()
```

