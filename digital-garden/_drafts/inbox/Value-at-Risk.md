Value-at-risk (VaR) answers the question, **"What is the minimum amount I can expect to lose over a given time horizon, with a specified confidence level?"**

Example: A **1-day 95% VaR of $1,000** means there is a 95% chance your loss tomorrow will not exceed $1,000, and a 5% chance the loss will be $1,000 or worse.

# Parameters for calculating VaR
1. Time horizon (eg. 1 day, 10 days, 1 month)
2. Confidence level, denoted $1-\alpha$ (usually 85% or 99%)
3. Portfolio value - the total monetary position being evaluated

Mathematically, for a random loss variable $L$:
$$
\mathbb{P} (L \geq \text{VaR}_\alpha) = \alpha
$$

# How to calculate VaR

## Parametric method
Assumes returns follow an explicit parametric distribution

1. Calculate the daily mean and daily standard deviation from historical returns.
2. Find the critical standard normal value $Z_\alpha$ for a given $\alpha$.
3. Compute the cutoff return: $R_{VaR} = \mu + Z_\alpha \cdot \sigma$
4. Multiply the cutoff return by portfolio value
