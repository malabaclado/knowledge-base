---
tags:
  - ai-note
---
Yes, it makes absolute sense to calculate both. In institutional risk management, running **Parametric VaR** and **Historical VaR** side-by-side is a standard practice known as **Model Validation** or **Cross-Checking**.

Because these two methodologies use completely different logical frameworks to estimate the "worst-case scenario," comparing their results tells a risk manager exactly where the hidden vulnerabilities in a portfolio lie.

---

## The Core Technical Difference

To understand why using both is valuable, you have to look at how they treat past data:

* **Parametric VaR (Variance-Covariance):** Takes historical data, distills it into simple statistical metrics (mean, standard deviation, and correlation), and fits them onto a smooth, clean mathematical curve (usually a Normal Distribution).
* **Historical VaR (Non-Parametric):** Completely ignores smooth mathematical assumptions. It takes the actual day-by-day historical returns of the past few years and lines them up from "best day" to "worst day," picking the exact historical cutoff point.

---

## When Are They BOTH Useful? (The "Stress Testing" Scenario)

Calculating both is incredibly useful when you need to diagnose the **structural health of a portfolio's diversification**.

### Scenario: The Hidden Correlation Shock

Imagine you manage a portfolio split evenly between US Tech stocks and Gold. Historically, when Tech drops, Gold rises (they are negatively correlated).

1. **What Parametric VaR Sees:** It looks at the mathematical correlation coefficient over the past 3 years. Because the statistical math says they move in opposite directions, the formula concludes they perfectly hedge each other. It spits out a very low, comfortable VaR dollar amount.
2. **What Historical VaR Sees:** It searches the actual timeline. It looks back to a major macro shock (like the 2020 pandemic crash or a severe liquidity crisis) where *everything* was panic-sold simultaneously. It flags that on those specific worst days, Tech and Gold both crashed together. It spits out a much higher, conservative VaR dollar amount.

### The Diagnostic Outcome:

* If **Parametric VaR = $2,000** but **Historical VaR = $4,500**, you have a massive warning sign. The huge gap tells you that while your portfolio looks perfectly safe and diversified on a smooth mathematical average, it contains severe **"fat-tail risk"**—meaning it is highly vulnerable to extreme, real-world market crashes where standard mathematical correlations completely break down.

---

## When is One Better Than the Other?

Each method has specific operational strengths and fatal weaknesses, making them ideal for different use cases.

### Choose Parametric VaR When...

* **Speed and Performance Matter:** Because it relies entirely on quick matrix algebra (multiplying weights by the covariance matrix), it calculates in microseconds. This makes it perfect for **on-demand "What-If" API endpoints** or real-time trading dashboards.
* **You are Analyzing Small Datasets:** If you only have a short history of data (e.g., a newly listed stock with only 150 days of history), the parametric model can still calculate a stable risk estimate.
* **The Fatal Flaw:** It assumes market returns are normally distributed (a perfect bell curve). In reality, stock markets experience extreme crashes far more often than a normal distribution predicts. It consistently **underestimates extreme tail risk**.

### Choose Historical VaR When...

* **Your Portfolio Contains Complex Derivatives:** If your portfolio contains options, futures, or complex structural products, their risk profiles change non-linearly as stock prices move. Parametric models completely choke on options math. Historical VaR handles them perfectly because it simply replays what the option actually did on those historical days.
* **You Want Absolute Real-World Truth:** It makes zero mathematical assumptions. If an interviewer asks you to defend your risk numbers, saying *"This is the exact dollar amount this asset mix lost during the market correction last year"* is incredibly grounded and unarguable.
* **The Fatal Flaw:** It assumes the future will be an exact replica of the past. If a market event occurs that has no historical precedent, Historical VaR is completely blind to it. It is also slow to calculate because it requires sorting and filtering massive arrays of data inside your script.

---

## Summary Checklist for Your API Design

If you include both in your portfolio project's payload, you can structure your system logic to provide immense value to an organization:

* Use **Parametric VaR** as the primary, lightning-fast trigger for your day-to-day user alerts and interactive "What-If" simulators.
* Use **Historical VaR** as a defensive safety buffer, running it alongside the parametric calculation to flag potential "tail-risk anomalies" whenever the historical loss projections violently overshoot the mathematical formula.