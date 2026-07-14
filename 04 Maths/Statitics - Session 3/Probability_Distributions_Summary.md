# Session 3 – Descriptive Statistics: Summary Notes

## 1. Random Variables

- **Algebraic variable** (e.g., *x*): an unknown fixed value.
- **Random variable (RV)**: a set of possible values that result from a random experiment.
- **Two types of random variables:**
  - **Discrete RV** — takes a countable set of values (e.g., rolling a die: 1–6).
  - **Continuous RV** — takes any value within a range, often infinite (e.g., height of people).

---

## 2. Probability Distributions

A **probability distribution** lists all possible outcomes of a random variable along with their probabilities.

**Problem:** When outcomes are numerous (or infinite, like height), a table becomes impractical.

**Solution:** Use a **mathematical function** to model the relationship between outcome and probability. This is called a **Probability Distribution Function (PDF/PMF)**.

> Note: "Probability Distribution" and "Probability Distribution Function" are often used interchangeably.

### Types
- **Discrete distributions** → described by a **PMF** (Probability Mass Function)
- **Continuous distributions** → described by a **PDF** (Probability Density Function)

### Why Probability Distributions Matter
- They give insight into the **shape** of your data.
- If your data matches a known ("famous") distribution, you automatically know a lot about its behavior.

### Famous Distributions (examples)
| Discrete | Continuous |
|---|---|
| Bernoulli, Binomial, Poisson, Negative Binomial, Beta-Binomial, Categorical | Normal, Uniform, Exponential, Log-normal, Gamma, Beta, Chi-square, t-distribution, Weibull, Pareto, Cauchy |

### Parameters
- **Parameters** are numerical values that define a distribution's **shape, location, and scale**.
- Different distributions have different parameters (e.g., Normal: mean *μ* and standard deviation *σ*).
- Understanding parameters is essential for statistical analysis and inference.

---

## 3. Probability Mass Function (PMF) — for Discrete RVs

The PMF assigns a probability to each possible value of a discrete random variable.

**Rules a valid PMF must satisfy:**
1. Every probability ≥ 0 (non-negative)
2. Sum of all probabilities = 1

*Examples: Bernoulli distribution, Binomial distribution*

---

## 4. Cumulative Distribution Function (CDF)

The CDF, **F(x)**, gives the probability that a random variable X is **less than or equal to** a value x:

```
F(x) = P(X ≤ x)
```

- Works for both discrete (built from PMF) and continuous (built from PDF) variables.
- The CDF is always non-decreasing and ranges from 0 to 1.
- For continuous variables, the CDF is obtained by **integrating** the PDF.

---

## 5. Probability Density Function (PDF) — for Continuous RVs

- Describes the probability distribution of a **continuous** random variable.
- Unlike PMF, the **height of the curve is not itself a probability** — for continuous variables, P(X = a single exact value) = 0.
- **The area under the curve** between two points represents the probability that X falls in that range:

```
P(a ≤ X ≤ b) = ∫ f(x) dx   (from a to b)
```

- Total area under the entire curve = 1 (i.e., P(-∞ ≤ X ≤ ∞) = 1)

**Key questions this concept answers:**
1. Why "density" and not "probability"? → Because at any single point, probability is technically zero; density describes relative likelihood.
2. What does area under the curve represent? → Probability over an interval.
3. How to calculate probability? → Integrate the PDF over the interval of interest.

*Examples: Normal distribution, Log-normal distribution, Poisson distribution*

---

## 6. Density Estimation

**Density estimation** = estimating the underlying probability density function (PDF) of a random variable from a set of observed data points.

**Uses:** hypothesis testing, data analysis, data visualization, machine learning (modeling input data or event likelihoods).

### A. Parametric Density Estimation
- Assumes the data follows a **specific known distribution** (e.g., Normal, Exponential, Poisson).
- Simpler and faster, but only accurate if the assumption is correct.

### B. Non-Parametric Density Estimation
- Makes **no assumption** about the underlying distribution.
- Estimates the density directly from the data.
- More flexible — useful when the true distribution is unknown or complex.
- **Downside:** computationally intensive and typically needs more data for accuracy.
- Common technique: **Kernel Density Estimation (KDE)**

---

## 7. Kernel Density Estimation (KDE)

- KDE smooths out data points using a **kernel function** (e.g., Gaussian) placed at each data point.
- Summing/overlapping these small "bumps" creates a **continuous, smooth estimate** of the density function — an alternative to a blocky histogram.
- **Bandwidth** (a hyperparameter): controls how wide/narrow each kernel is.
  - Too small → overly "spiky," noisy curve
  - Too large → oversmoothed, loses detail
- Choosing the right bandwidth balances smoothness vs. accuracy.

---

## 8. PDF vs CDF — Visual Relationship

| Aspect | PDF | CDF |
|---|---|---|
| Represents | Relative density/likelihood at a point | Cumulative probability up to a point |
| Shape | Bell-shaped curve (for Normal) | S-shaped (sigmoid-like), increasing from 0 to 1 |
| Relationship | Area under PDF = value on CDF | CDF is the **integral** of the PDF; PDF is the **derivative** of the CDF |
| Example | P(X = 165 cm) → density value only | P(X ≤ 165 cm) → actual cumulative probability |

---

### Quick Recap
- **RV** = outcome of a random experiment → discrete or continuous
- **PMF** → probabilities for discrete RVs (must sum to 1)
- **PDF** → density function for continuous RVs (area under curve = probability)
- **CDF** → cumulative probability P(X ≤ x), obtained via integration of PDF
- **Density Estimation** → estimating PDF from data (parametric = assumes known distribution; non-parametric = no assumption, e.g., KDE)
- **KDE** → smooths data using kernels; bandwidth controls smoothness
