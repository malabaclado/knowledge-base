---
id: gemini_97aefc13564d5d4c
title: What is Value-at-Risk (VaR) and how to calculate it.
source: gemini
url: https://gemini.google.com/app/97aefc13564d5d4c
created: 2026-09-11T11:53:14+08:00
modified: 2026-09-11T11:53:14+08:00
tags:
  - ai-conversation
  - gemini
message_count: 8
---

> [!QUESTION] User
> I have a GARCH(1,1) model using Python's arch library. The model uses student's t distribution as the error distribution. How to calculate the value-at-risk using this model?

> [!NOTE] Gemini
> To calculate Value-at-Risk (VaR) from an `arch` GARCH(1,1) model with a Student’s $t$\-distribution, you need three components: the conditional mean forecast ($\hat{\mu}_{t+1}$), the conditional volatility forecast ($\hat{\sigma}_{t+1}$), and the standardized Student's $t$ quantile ($q_\alpha$).
> 
> Because the `arch` library standardizes the Student's $t$\-distribution to have unit variance ($\text{Var}(z_t) = 1$), you must use the standardized quantile rather than an unscaled `scipy.stats.t` quantile.
> 
> ### Implementation
> 
> Python
> 
> ```
> import numpy as np
> from arch import arch_model
> 
> # 1. Specify and fit the GARCH(1,1) model with Student's t innovations
> # returns: 1D array or pandas Series of returns (e.g., percentage returns)
> model = arch_model(returns, p=1, q=1, mean="Constant", dist="StudentsT")
> res = model.fit(disp="off")
> 
> # 2. Extract degrees of freedom (nu)
> nu = res.params["nu"]
> 
> # 3. Forecast 1-step-ahead conditional mean and variance
> forecasts = res.forecast(horizon=1)
> mu_forecast = forecasts.mean.iloc[-1, 0]
> sigma_forecast = np.sqrt(forecasts.variance.iloc[-1, 0])
> 
> # 4. Get the quantile for desired significance level (e.g., 95% or 99% VaR)
> alpha = 0.05  # 5% tail -> 95% VaR
> 
> # Option A: Directly using the fitted distribution from arch
> q_alpha = res.model.distribution.ppf(alpha, nu)
> 
> # Option B: Using scipy.stats (scaled for unit variance)
> # from scipy.stats import t
> # q_alpha = t.ppf(alpha, df=nu) * np.sqrt((nu - 2) / nu)
> 
> # 5. Calculate VaR
> # Expressed as a return threshold (negative number):
> var_return = mu_forecast + sigma_forecast * q_alpha
> 
> # Expressed as a positive loss percentage:
> var_loss = -var_return
> 
> print(f"Degrees of freedom (nu): {nu:.2f}")
> print(f"1-Day 95% VaR (Loss): {var_loss:.4f}")
> ```
> 
> ### In-Sample Dynamic VaR (Rolling Backtest)
> 
> If you need a continuous series of in-sample VaR estimates across your historical dataset:
> 
> Python
> 
> ```
> # In-sample fitted values
> cond_mean = res.conditional_volatility * 0 + res.params["mu"]  # or res.fitted_values
> cond_vol = res.conditional_volatility
> q_alpha = res.model.distribution.ppf(alpha, res.params["nu"])
> 
> # Daily in-sample VaR series (loss format)
> var_series = -(cond_mean + cond_vol * q_alpha)
> ```
> 
> ### Key Considerations
> 
> -   **Unit Variance Scaling:** A standard Student's $t$ variable has variance $\frac{\nu}{\nu - 2}$. The `arch` library divides the innovation by $\sqrt{\frac{\nu - 2}{\nu}}$ so that $\sigma_t^2$ represents the full conditional variance. Calling `res.model.distribution.ppf(alpha, nu)` handles this transformation automatically.
>     
> -   **Return Units:** If your return series is scaled by 100 (e.g., $1.5\%$ input as `1.5`), the resulting VaR is also in percentage points.
>     
> -   **Expected Shortfall (CVaR):** If you also need ES at level $\alpha$, integrate the standardized density tail:
>     
>     $$
>     \text{ES}_\alpha = -\left( \hat{\mu}_{t+1} + \hat{\sigma}_{t+1} \cdot \frac{1}{\alpha} \int_0^\alpha q_p \, dp \right)
>     $$
>     
> 
> Want me to show how to calculate Expected Shortfall (CVaR) or run a Kupiec backtest?
> 
> Yes

> [!QUESTION] User
> Summarize the formulas for VaR and CVaR for me

> [!NOTE] Gemini
> Value-at-Risk (VaR) measures the maximum expected loss at a given confidence level over a specific horizon, while Conditional Value-at-Risk (CVaR), also called Expected Shortfall (ES), measures the average loss exceeding VaR.
> 
> ### Core Theoretical Definitions
> 
> For continuous return $R$ and loss $L = -R$ with significance level $\alpha \in (0, 1)$ (e.g., $\alpha = 0.05$ for $95\%$ confidence):
> 
> -   **Value-at-Risk ($\text{VaR}_\alpha$):** The lower $\alpha$\-quantile of the return distribution (or upper $(1-\alpha)$\-quantile of loss):
>     
>     $$
>     \text{VaR}_\alpha = -F_R^{-1}(\alpha) = F_L^{-1}(1 - \alpha)
>     $$
>     
> -   **Conditional Value-at-Risk ($\text{CVaR}_\alpha$):** The expected loss given that the loss exceeds $\text{VaR}_\alpha$:
>     
>     $$
>     \text{CVaR}_\alpha = \mathbb{E}[L \mid L \ge \text{VaR}_\alpha] = -\frac{1}{\alpha} \int_0^\alpha F_R^{-1}(p) \, dp
>     $$
>     
> 
> ### Distributional Formulas (Loss Convention: Loss $\> 0$)
> 
> Let $\mu$ be the conditional mean, $\sigma$ the conditional volatility, and $z$ the standardized innovation.
> 
> | Distribution | VaRα​ Formula | CVaRα​ Formula |
> | --- | --- | --- |
> | Standard Normal Z∼N(0,1) | −(μ+σΦ−1(α)) | −μ+σ(αϕ(Φ−1(α))​) |
> | Standardized Student's t (Var=1) | −(μ+σqα,ν​) | −μ+σ(αgν​(qα,ν​)​(ν−1ν+qα,ν2​​)) |
> | Empirical / Historical | −Quantile(R,α) | −∣Ri​≤−VaRα​∣1​∑Ri​≤−VaRα​​Ri​ |
> 
> Where:
> 
> -   $\Phi^{-1}(\cdot)$ and $\phi(\cdot)$ are the standard normal quantile and PDF.
>     
> -   $\nu \> 2$ is the degrees of freedom parameter for the Student's $t$\-distribution.
>     
> -   $q_{\alpha, \nu}$ is the $\alpha$\-quantile of the standardized Student's $t$\-distribution:
>     
>     $$
>     q_{\alpha, \nu} = t_\nu^{-1}(\alpha) \cdot \sqrt{\frac{\nu - 2}{\nu}}
>     $$
>     
> -   $g_\nu(\cdot)$ is the standardized Student's $t$ probability density function:
>     
>     $$
>     g_\nu(x) = \sqrt{\frac{\nu}{\nu - 2}} \cdot \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\pi \nu} \, \Gamma\left(\frac{\nu}{2}\right)} \left( 1 + \frac{x^2}{\nu - 2} \right)^{-\frac{\nu + 1}{2}}
>     $$
>     
> 
> ### Key Theoretical Differences
> 
> -   **Coherence:** VaR is not a coherent risk measure because it violates the subadditivity axiom ($\text{VaR}(X + Y) \not\le \text{VaR}(X) + \text{VaR}(Y)$ under non-elliptical or heavy-tailed distributions). CVaR is always coherent.
>     
> -   **Tail Sensitivity:** VaR is completely blind to the magnitude of losses beyond the cutoff percentile. CVaR accounts for tail severity and kurtosis.

> [!QUESTION] User
> What is Value-at-Risk in finance and how is it computed, for a stock, for example?

> [!NOTE] Gemini
> Value-at-Risk (VaR) answers a specific risk question: **"What is the minimum amount I can expect to lose over a given time horizon, with a specified confidence level?"**
> 
> For instance, a **1-day 95% VaR of $1,000** means there is a 95% chance your loss tomorrow will not exceed $1,000, and a 5% chance the loss will be $1,000 or worse.
> 
> ### Core Components of VaR
> 
> To define VaR, three parameters must be specified:
> 
> -   **Time Horizon ($T$):** The holding period (e.g., 1 day, 10 days, 1 month).
>     
> -   **Confidence Level ($1 - \alpha$):** Commonly 95% or 99% ($\alpha = 0.05$ or $0.01$).
>     
> -   **Portfolio Value ($V$):** The total monetary position being evaluated.
>     
> 
> Mathematically, for a loss random variable $L$:
> 
> $$
> \mathbb{P}(L \ge \text{VaR}_\alpha) = \alpha
> $$
> 
> ### Concrete Example: 3 Ways to Calculate Stock VaR
> 
> Assume you own **$10,000** worth of a stock and want to calculate the **1-day 95% VaR** ($\alpha = 0.05$).
> 
> #### 1\. Parametric (Variance-Covariance) Method
> 
> Assumes returns follow an explicit parametric distribution (typically Normal or Student's $t$).
> 
> 1.  Calculate the daily mean ($\mu$) and daily standard deviation ($\sigma$) from historical returns.
>     
>     -   *Example:* $\mu = 0.05\%$, $\sigma = 1.8\%$.
>         
> 2.  Find the critical standard normal value $Z_\alpha$ for $\alpha = 0.05$:
>     
>     $$
>     Z_{0.05} \approx -1.645
>     $$
>     
> 3.  Compute the cutoff return:
>     
>     $$
>     R_{\text{VaR}} = \mu + Z_\alpha \cdot \sigma = 0.0005 - (1.645 \cdot 0.018) = -0.02911 \text{ (-2.91\%)}
>     $$
>     
> 4.  Multiply by portfolio value:
>     
>     \\text{VaR}_{\\\$} = V \\cdot \\vert{}R_{\\text{VaR}}\\vert{} = \\\$10,000 \\cdot 0.02911 = \\mathbf{\\\$291.10}
>     
> 
> *Pros:* Fast and analytical.
> 
> *Cons:* Underestimates extreme tail risk because actual stock returns exhibit skewness and fat tails (excess kurtosis).
> 
> #### 2\. Historical Simulation
> 
> Makes no distributional assumptions; uses the empirical distribution of past returns.
> 
> 1.  Collect the past $N$ daily returns (e.g., $N = 500$ trading days).
>     
> 2.  Sort the returns in ascending order (worst to best):
>     
>     $$
>     R_{(1)} \le R_{(2)} \le \dots \le R_{(500)}
>     $$
>     
> 3.  Pick the $(N \times \alpha)$\-th observation. For 500 days at $5\%$:
>     
>     $$
>     \text{Rank} = 500 \cdot 0.05 = 25\text{th worst day}
>     $$
>     
> 4.  If the 25th worst return is $-2.70\%$:
>     
>     \\text{VaR}_{\\\$} = \\\$10,000 \\cdot 0.027 = \\mathbf{\\\$270.00}
>     
> 
> *Pros:* Captures real market fat tails and non-linearities naturally.
> 
> *Cons:* Backward-looking; limited by history (cannot predict a crash worse than past observations).
> 
> #### 3\. Monte Carlo Simulation
> 
> Generates thousands of hypothetical future paths using a stochastic model (e.g., Geometric Brownian Motion or GARCH).
> 
> 1.  Define a process: $dS_t = \mu S_t dt + \sigma S_t dW_t$.
>     
> 2.  Simulate $M$ scenarios (e.g., $M = 10,000$) for the next trading day.
>     
> 3.  Calculate returns across all 10,000 trials and sort them.
>     
> 4.  Extract the 500th worst outcome (the 5th percentile) and scale by $V$.
>     
> 
> *Pros:* Highly flexible; accommodates non-linear instruments like options and path-dependent dynamics.
> 
> *Cons:* Computationally intensive; sensitive to model calibration and underlying assumptions.
> 
> ### Comparison of Methods
> 
> | Method | Best Used For | Primary Limitation |
> | --- | --- | --- |
> | Parametric | Liquid, linear portfolios needing real-time risk reporting | Fails to capture fat tails and structural market crashes |
> | Historical | Portfolios with extensive historical price data | Assumes the past represents future market dynamics |
> | Monte Carlo | Portfolios containing options, structured products, or path dependencies | High computational overhead; model risk |
> 
> ### Critical Limitations of VaR
> 
> -   **Blind to Extreme Tail Losses:** VaR only tells you the boundary of the worst 5%. It does not indicate whether the loss past that point is $300 or $3,000. (Expected Shortfall/CVaR is used to measure the expected loss given that VaR is breached).
>     
> -   **Non-Subadditive:** The VaR of a combined portfolio can theoretically be greater than the sum of the individual VaRs ($\text{VaR}(A + B) \> \text{VaR}(A) + \text{VaR}(B)$) under heavy-tailed distributions, violating coherence.

> [!QUESTION] User
> Now, what is expected shortfall? How does it relate to VaR? How to calculate it?

> [!NOTE] Gemini
> **Expected Shortfall (ES)**, also known as **Conditional Value-at-Risk (CVaR)**, is a risk measure that answers the question:
> 
> > *"If losses cross the Value-at-Risk threshold and things go wrong, how much should I expect to lose on average?"*
> 
> While VaR defines the boundary of the worst outcomes, Expected Shortfall quantifies the magnitude of the tail losses beyond that boundary.
> 
> ### How ES Relates to VaR
> 
> Expected Shortfall directly depends on VaR. If you set a $95\%$ confidence level ($\alpha = 0.05$):
> 
> -   **VaR** is the **cutoff point** separating the best $95\%$ of days from the worst $5\%$.
>     
> -   **ES** is the **expected value (mean)** of all the losses falling into that worst $5\%$ tail.
>     
> 
> ```
> Distribution of Portfolio P&L / Returns
>                     
>                      Tail (Worst α = 5%)
>                     |-------------------|
>          ES         |                   |
>     [Average Tail]  |   VaR (Cutoff)    |
>           ▼         |        ▼          |
>   ───────●──────────┼────────●──────────┼─────────────────────
>                     |                   |      Normal /
>                     |                   |    Profitable Days
>                     |                   |        (95%)
> ```
> 
> #### Why Regulators & Risk Managers Prefer ES Over VaR
> 
> 1.  **Subadditivity (Coherence):** VaR is mathematically non-subadditive. Combining two risky portfolios can occasionally produce a VaR greater than the sum of their individual VaRs ($\text{VaR}(X + Y) \> \text{VaR}(X) + \text{VaR}(Y)$). ES is a **coherent risk measure**; it always satisfies subadditivity, meaning diversification is consistently rewarded.
>     
> 2.  **Tail Risk Sensitivity:** Two assets can have the exact same 95% VaR (e.g., -\\\$100), but one might have a mild tail (losses cap at -\\\$110) while the other carries catastrophic tail risk (losses reaching -\\\$1,000, such as short out-of-the-money options). VaR treats them as identical; ES immediately captures the severity.
>     
> 3.  **Basel III / FRTB Standard:** Under the Basel Committee's Fundamental Review of the Trading Book (FRTB), banking regulators officially replaced 99% VaR with 97.5% Expected Shortfall for market risk capital requirements.
>     
> 
> ### How to Calculate Expected Shortfall
> 
> Mathematically, for loss variable $L$ and significance level $\alpha$:
> 
> $$
> \text{ES}_\alpha = \mathbb{E}[L \mid L \ge \text{VaR}_\alpha] = \frac{1}{\alpha} \int_0^\alpha \text{VaR}_p \, dp
> $$
> 
> Using the same **$10,000 portfolio** over a **1-day horizon** at **95% confidence ($\alpha = 0.05$)**:
> 
> #### 1\. Historical Method
> 
> Take past empirical returns, identify observations worse than the VaR cutoff, and average them.
> 
> 1.  Take $N = 500$ historical daily returns, sorted from worst to best: $R_{(1)} \le R_{(2)} \le \dots \le R_{(500)}$.
>     
> 2.  With $\alpha = 0.05$, the worst $5\%$ consists of the lowest $500 \times 0.05 = 25$ returns.
>     
> 3.  The 25th worst return is your **VaR**.
>     
> 4.  **ES** is the simple average of those first 25 returns:
>     
>     $$
>     \text{ES}_\alpha = -\frac{1}{25} \sum_{i=1}^{25} R_{(i)}
>     $$
>     
> 5.  If the average of those 25 worst daily returns is $-3.8\%$:
>     
>     \\text{ES}_{\\\$} = \\\$10,000 \\times 0.038 = \\mathbf{\\\$380.00}
>     
>     *(Compared to a VaR of, say, \\\$270)*.
>     
> 
> #### 2\. Parametric Method (Normal Distribution)
> 
> If daily returns follow $R \sim \mathcal{N}(\mu, \sigma)$, ES has an exact closed-form solution derived from the truncated normal distribution:
> 
> $$
> \text{ES}_\alpha = -\mu + \sigma \left( \frac{\phi(\Phi^{-1}(\alpha))}{\alpha} \right)
> $$
> 
> Where:
> 
> -   $\Phi^{-1}(\alpha)$ is the standard normal quantile (for $\alpha = 0.05$, $\Phi^{-1}(0.05) \approx -1.6449$).
>     
> -   $\phi(\cdot)$ is the standard normal probability density function (PDF):
>     
>     $$
>     \phi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
>     $$
>     
> -   For $\alpha = 0.05$: $\phi(-1.6449) \approx 0.1031$, so $\frac{\phi(\Phi^{-1}(0.05))}{0.05} \approx \frac{0.1031}{0.05} \approx 2.0627$.
>     
> 
> *Calculation:*
> 
> -   If $\mu = 0.05\%$ and $\sigma = 1.8\%$:
>     
>     $$
>     \text{ES}_{\text{return}} = -0.0005 + 0.018 \times 2.0627 = 0.0366 \text{ (3.66\% loss)}
>     $$
>     
>     \\text{ES}_{\\\$} = \\\$10,000 \\times 0.0366 = \\mathbf{\\\$366.29}
>     
> 
> #### 3\. Standardized Student's $t$ Distribution (GARCH Context)
> 
> When innovations follow a standardized Student's $t$ with degrees of freedom $\nu \> 2$:
> 
> $$
> \text{ES}_\alpha = -\mu + \sigma \left( \frac{g_\nu(q_{\alpha, \nu})}{\alpha} \left( \frac{\nu + q_{\alpha, \nu}^2}{\nu - 1} \right) \right)
> $$
> 
> Where $q_{\alpha, \nu}$ is the quantile of the scaled $t$\-distribution and $g_\nu(\cdot)$ is its density function.
> 
> ### Python Code: Calculating ES from Historical and GARCH Outputs
> 
> Python
> 
> ```
> import numpy as np
> from scipy import stats
> 
> # Sample daily percentage returns
> np.random.seed(42)
> returns = np.random.standard_t(df=5, size=1000) * 0.015 + 0.0005
> portfolio_value = 10000
> alpha = 0.05
> 
> # -------------------------------------------------------------
> # 1. Historical ES
> # -------------------------------------------------------------
> hist_var = -np.percentile(returns, alpha * 100)
> tail_losses = returns[returns <= -hist_var]
> hist_es = -tail_losses.mean()
> 
> print(f"Historical 95% VaR: ${portfolio_value * hist_var:.2f}")
> print(f"Historical 95% ES:  ${portfolio_value * hist_es:.2f}")
> 
> # -------------------------------------------------------------
> # 2. Parametric Normal ES
> # -------------------------------------------------------------
> mu = np.mean(returns)
> sigma = np.std(returns)
> 
> z_alpha = stats.norm.ppf(alpha)
> normal_var = -(mu + sigma * z_alpha)
> normal_es = -mu + sigma * (stats.norm.pdf(z_alpha) / alpha)
> 
> print(f"Normal 95% VaR:     ${portfolio_value * normal_var:.2f}")
> print(f"Normal 95% ES:      ${portfolio_value * normal_es:.2f}")
> ```
> 
> ### Summary Comparison
> 
> | Feature | Value-at-Risk (VaR) | Expected Shortfall (ES / CVaR) |
> | --- | --- | --- |
> | Question Answered | "Where does the tail start?" | "What is the average loss inside the tail?" |
> | Mathematical Property | Quantile (Percentile) | Conditional Expectation |
> | Subadditivity | No (diversification can artificially increase VaR) | Yes (always coherent) |
> | Information Used | Only the single threshold value | Entire distribution beyond the threshold |
> | Regulatory Preference | Basel II standard | Basel III / FRTB market risk standard |