---
title: Finite-State Markov Chain Model
---

A **Markov chain** is a model for movement between discrete states.  
But this model only makes sense when the **Markov Property** holds — that is:

> (Memoryless) The future depends only on the present, not on the past.

Formally, for states $X_0, X_1, \dots, X_n$ in a discrete-time stochastic process:

$$\mathbb{P}(X_{n+1} = x \mid X_n = x_n, X_{n-1} = x_{n-1}, \dots, X_0 = x_0) = \mathbb{P}(X_{n+1} = x \mid X_n = x_n)$$

This assumption is **not universal**. It must be **justified by the nature of the system** being modeled.

> Markov property is not about the system itself, but about how you model information and relevance.


### When the Markov Property Fails

- **Human Learning Behavior**
  A student's future performance depends not just on their current grade, but also on how long and how intensely they studied in the past.  
  → Long-term memory → violates the Markov property.
- **Disease Progression**  
  In medical diagnosis, the probability of developing complications may depend on how long the patient has been ill — not just the current stage of disease.  
  → Duration-sensitive states → non-Markovian.
 - **Passive Investment Based on Long-Term History**
   An investor builds a portfolio by analyzing a firm’s **extended earnings history**, sector trends, and macroeconomic business cycles to predict future return. Decisions at time $t$ are conditioned on a long series of past financial states: $\mathbb{P}(\text{return}_{t+1} \mid \text{history}_{\leq t})$
   → **Past-dependent inference** violates the Markov property.

### When the Markov Property Holds (or approximately holds)

- **Active Investment Based on Present Signal**
  An investor makes decisions based on **current** financial signals, market sentiment, or recent events — such as a product launch or policy shift. In this case, the future expected return depends only on the current observable state: $\mathbb{P}(\text{return}_{t+1} \mid \text{state}_t)$
  → If the uncertainty horizon is short, and the system resets quickly, the process is **approximately Markovian**.
- **Inventory Replenishment Models**  
  If a warehouse is monitored daily, and decisions are made based on current stock levels only, then future inventory is conditionally independent of the past given the present.  
  → Well-controlled, memoryless policy → approximates a Markov chain.
- **Web Page Navigation (PageRank)**  
  The likelihood of a user jumping from one page to another depends only on the current page, not the full click history.  
  → Modeled as a Markov chain with transition matrix from current to next page.


Hence, before using a Markov model, we must ask:

> “Does the system _forget_ its past once the present is known?”

Only then can transition probabilities (e.g., $P(i \to j)$) fully describe the process.  
Once this assumption is accepted, we can begin to explore **structure** within the state space — and the first structural question is:

> “Which states communicate with each other?”

This leads us to our first concept: **Communicating States**.
