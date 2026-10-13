

# ARCH
An **ARCH** model (**A**utoregressive **C**onditional **H**eteroskedasticity) is a statistical model used in financial time series to predict **changing volatility** over time.

- **Autoregressive:** The current value is predicted using past values of the same series (specifically, past squared residuals/surprises).
- **Conditional:** The variance at time $t$ is non-static; it depends on (is conditional upon) information from previous days.
- **Heteroskedasticity:** A fancy econometrics term for **non-constant (changing) variance**. (Homoskedastic = constant variance; Heteroskedastic = changing variance).

In plain English, *conditional heteroskedasticity* means **"variance that changes over time based on recent events."**

Core intuition: An ARCH model captures this behavior by assuming that **today’s variance depends on how big yesterday’s surprises (shocks) were**.

ARCH models were created in the context of econometric and finance problems having to do with the amount that investments or stocks increase (or decrease) per time period, so there’s a tendency to describe them as models for that type of variable.

## Limitations
While groundbreaking, standard ARCH models have a key drawback:

- **Requires too many lags:** To capture long-lasting volatility spikes in financial markets, an ARCH model often needs a large number of parameters ($q$).
- **Symmetric response:** Basic ARCH treats positive shocks and negative shocks identically, even though market drops usually trigger higher volatility than market gains.


# GARCH

**GARCH** stands for **Generalized Autoregressive Conditional Heteroskedasticity**. Developed by Tim Bollerslev in 1986 as a direct extension of Robert Engle's ARCH model, GARCH is designed to model time-varying volatility with far greater efficiency.

The core difference is simple:
- **ARCH** predicts today's volatility using **past squared shocks** (market surprises).
- **GARCH** predicts today's volatility using **past squared shocks AND past predicted variance**.

In a standard $\text{GARCH}(p, q)$ model, $p$ represents the number of lagged variance terms, and $q$ represents the number of lagged squared shock terms.

The most popular version in quantitative finance is **$\text{GARCH}(1,1)$**:

$$\sigma_t^2 = \omega + \alpha_1 \epsilon_{t-1}^2 + \beta_1 \sigma_{t-1}^2$$

Here is what each component represents:
- **$\omega > 0$**: The baseline variance constant.
- **$\alpha_1 \epsilon_{t-1}^2$ (The ARCH term):** Yesterday's market shock. It measures how strongly volatility reacts to sudden news or large price jumps (**short-term reaction**).
- **$\beta_1 \sigma_{t-1}^2$ (The GARCH term):** Yesterday's forecasted variance. It carries forward past volatility momentum (**volatility persistence**).

# Check for Stationarity

Stationarity means the series has a constant mean, constant variance, and constant autocovariance over time.

### Statistical Tests
- **Augmented Dickey-Fuller (ADF) Test:**
    - **Null Hypothesis ($H_0$):** The series has a unit root (it is **non-stationary**).
    - **Alternative Hypothesis ($H_1$):** The series is stationary.
    - **Interpretation:** A $p\text{-value} < 0.05$ rejects $H_0$, indicating the series **is stationary**.
- **Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test:**
    - **Null Hypothesis ($H_0$):** The series **is stationary**.
    - **Interpretation:** Unlike ADF, a $p\text{-value} > 0.05$ means you fail to reject $H_0$ (confirming stationarity). Running ADF and KPSS together gives a robust double-check.
- **Phillips-Perron (PP) Test:**
    - Similar to ADF, but incorporates non-parametric corrections for serial correlation and heteroskedasticity in the error terms.

### Visual Diagnostics
- **Time Series Line Plot:** Looking for a constant mean around zero without long-term upward/downward trends.
- **Autocorrelation Function (ACF) Plot:** A non-stationary series shows ACF values decaying very slowly across many lags, whereas a stationary series cuts off or decays rapidly toward zero.


# Check for Conditional Heteroskedasticity (ARCH effects)

### Statistical Tests

- **Engle’s Lagrange Multiplier (LM) Test for ARCH Effects:**
    - **How it works:** Regresses the squared residuals $\hat{\epsilon}_t^2$ on $q$ lagged squared residuals ($\hat{\epsilon}_{t-1}^2, \dots, \hat{\epsilon}_{t-q}^2$) to test if past shocks predict current volatility.
    - **Null Hypothesis ($H_0$):** No ARCH effects (homoskedasticity; $a_1 = a_2 = \dots = a_q = 0$).
    - **Alternative Hypothesis ($H_1$):** ARCH effects are present (conditional heteroskedasticity).
    - **Interpretation:** A $p\text{-value} < 0.05$ rejects $H_0$, confirming that conditional heteroskedasticity exists and an ARCH/GARCH model is warranted.
- **Ljung-Box Test on Squared Residuals:**
    - **How it works:** Evaluates whether there is significant autocorrelation in the **squared returns/residuals** ($\epsilon_t^2$).
    - **Null Hypothesis ($H_0$):** The squared residuals are independently distributed (no autocorrelation/ARCH effects).
    - **Interpretation:** A $p\text{-value} < 0.05$ indicates significant autocorrelation in variance over time.

### Visual Diagnostics
- **Residual / Return Plot:** Look for **volatility clustering**—distinct high-volatility bands alternating with quiet, low-volatility bands.
- **ACF / PACF of Squared Returns ($\epsilon_t^2$):** While raw returns often show zero autocorrelation, the **squared returns** will show significant autocorrelations at multiple lags if conditional heteroskedasticity is present.

# Augmented Dickey-Fuller (ADF)

The Augmented Dickey-Fuller test is an extended version of the Dickey-Fuller test. It tests the null hypothesis that a unit root is present in a time series sample. The presence of a unit root means the series is non-stationary.

# Stationarity

Conditions for stationarity
1. Mean is constant
2. S.D. is constant
3. No seasonality

Remark on white noise:
- If a series is white noise, then it is stationary. (white noise mean = 0, a constant)
- If a series is stationary, it is not necessarily white noise (mean may not be zero).

Can we make a time series stationary? Possible. (as per the video reference below - via transformations)


Reference: [Time Series Talk : Stationarity](https://www.youtube.com/watch?v=oY-j2Wof51c&list=PLvcbYUQ5t0UHOLnBzl46_Q6QKtFgfMGc3&index=4)
