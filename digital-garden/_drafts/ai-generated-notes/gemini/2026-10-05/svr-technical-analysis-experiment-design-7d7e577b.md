---
id: gemini_7d7e577bd6a17dc6
title: SVR Technical Analysis Experiment Design
source: gemini
url: "https://gemini.google.com/app/7d7e577bd6a17dc6"
created: "2026-10-05T10:46:02+08:00"
modified: "2026-10-05T10:46:02+08:00"
tags:
  - ai-conversation
  - gemini
message_count: 8
---

> [!QUESTION] User
> You are a data scientist. Given this research problem, how would you conduct this experiment?
> Problem: Can technical analysis (TA) indicators derived from historical closing prices serve as effective input features for Support Vector Regression (SVR) to predict equity prices?

> [!NOTE] Gemini
> To evaluate whether technical indicators derived from closing prices provide predictive power for Support Vector Regression (SVR), you need an experimental design that avoids lookahead bias, respects market non-stationarity, and evaluates economic relevance beyond simple statistical error.
> 
> ### 1\. Problem Formulation & Target Variable
> 
> Directly predicting nominal future prices ($P_{t+k}$) with SVR often produces a deceptively low Mean Squared Error (MSE) simply because $P_t$ is a non-stationary random walk with drift; the model essentially learns $P_{t+k} \approx P_t$ with a 1-step lag.
> 
> -   **Target ($y_t$):** Formulate the target as **$k$\-step forward log returns** or percentage change:
>     
>     $$
>     y_t = \ln\left(\frac{P_{t+k}}{P_t}\right)
>     $$
>     
>     Common choices: $k=1$ (next-day return) or $k=5$ (weekly return).
>     
> -   **Alternative Formulation:** Directional classification (SVC) or triple-barrier labeling if trade execution logic is desired.
>     
> 
> ### 2\. Feature Engineering & Preprocessing
> 
> Derive technical indicators across distinct analytical categories to avoid collinear momentum indicators dominating the feature space:
> 
> | Indicator Category | Examples | Purpose |
> | --- | --- | --- |
> | Trend / Moving Averages | EMA/SMA ratios (SMA20​Pt​​), MACD signal difference | Captures baseline directional momentum |
> | Momentum / Oscillators | RSI (14-day), Stochastic Oscillator (%K, %D) | Quantifies overbought/oversold boundaries |
> | Volatility | Normalized ATR (Pt​ATR14​​), Bollinger Bands %B | Captures dispersion and regime width |
> | Volume / Price-Volume | On-Balance Volume (OBV) slope, VWAP spread | Validates price moves against liquidity |
> 
> #### Crucial Preprocessing Rules
> 
> -   **Stationarity:** Never feed raw nominal indicators (e.g., raw Moving Averages or raw prices) into SVR. Transform them into dimensionless ratios or differentials (e.g., $(P_t - \text{SMA}_n) / \text{SMA}_n$).
>     
> -   **Scaling:** SVR relies on distance metrics in feature space (typically via an RBF kernel). Scale all features to $[0, 1]$ or normalize with robust z-scores ($Z = \frac{X - \text{median}}{\text{IQR}}$) fitted **strictly on the training split** to prevent data leakage.
>     
> -   **Collinearity Reduction:** Use PCA or hierarchical clustering on the feature correlation matrix to prune redundant indicators.
>     
> 
> ### 3\. Data Splitting & Cross-Validation
> 
> Standard $k$\-fold cross-validation is invalid here due to temporal autocorrelation and lookahead bias.
> 
> -   **Split Strategy:** Use a **Rolling-Window (Walk-Forward) Validation** or **Expanding Window with an Embargo/Purge buffer**.
>     
>     -   *Purging:* Remove training labels whose forward return windows overlap with the test set evaluation start.
>         
>     -   *Window Setup:* Train on $T$ months $\rightarrow$ validate/tune on next $M$ months $\rightarrow$ evaluate out-of-sample on next $N$ months $\rightarrow$ roll forward.
>         
> -   **Asset Universe:** Select liquid equities (e.g., S&P 500 constituents) across diverse market regimes (e.g., 2018–2024 to capture bull, bear, and high-volatility sideways environments).
>     
> 
> ### 4\. Baseline Benchmarks & Model Configuration
> 
> An ML model's performance is meaningless in finance without comparing it against simpler structural baselines:
> 
> 1.  **Baselines:**
>     
>     -   *Naive Persistence Model:* $\hat{y}_{t+k} = 0$ (random walk benchmark).
>         
>     -   *Linear Auto-Regressive (ARIMA/Ridge):* Evaluates whether non-linear kernels add value over linear combinations.
>         
>     -   *Buy-and-Hold:* Passive index benchmark.
>         
> 2.  **SVR Configurations:**
>     
>     -   Kernels: Test **RBF** ($K(x, x') = \exp(-\gamma \vert{}\vert{}x - x'\vert{}\vert{}^2)$) vs. **Linear** and **Polynomial**.
>         
>     -   Hyperparameter Tuning: Grid/Bayesian search over $C$ (regularization penalty), $\epsilon$ (insensitivity margin), and $\gamma$ (kernel coefficient), optimized strictly on the inner cross-validation folds.
>         
> 
> ### 5\. Evaluation Protocol
> 
> Evaluate both **statistical predictive accuracy** and **economic/financial utility**:
> 
> #### A. Statistical Metrics
> 
> -   **RMSE / MAE:** Computed against the forward returns $y_t$.
>     
> -   **Mean Directional Accuracy (MDA):**
>     
>     $$
>     \text{MDA} = \frac{1}{N} \sum_{t=1}^N \mathbf{1}_{\text{sign}(y_t) == \text{sign}(\hat{y}_t)}
>     $$
>     
>     *(MDA significantly $\> 50\%$ indicates exploitable directional edge).*
>     
> -   **Information Coefficient (IC):** Spearman rank correlation between predicted returns and realized returns across assets per time step.
>     
> 
> #### B. Financial Backtest
> 
> -   **Strategy Simulation:** Long positions when $\hat{y}_t \> \delta$, Short/Cash when $\hat{y}_t \< -\delta$ (where $\delta$ is a volatility-adjusted threshold).
>     
> -   **Friction Constraints:** Apply realistic transaction costs (e.g., 5–10 bps per trade + slippage).
>     
> -   **Metrics:** Sharpe Ratio, Maximum Drawdown (MDD), Sortino Ratio, and Annualized Alpha relative to benchmark.
>     
> 
> ### 6\. Hypotheses & Validation Criteria
> 
> -   **Null Hypothesis ($H_0$):** Technical indicators fed into SVR yield an out-of-sample directional accuracy no better than a random walk ($\text{MDA} \le 50\%$) and fail to achieve a statistically significant positive Sharpe ratio after transaction costs.
>     
> -   **Alternative Hypothesis ($H_1$):** Non-linear feature interactions mapped by SVR kernels yield an information coefficient $\text{IC} \> 0.03$ and generate risk-adjusted returns exceeding the passive buy-and-hold benchmark under equivalent risk limits.
>     
> 
> Want to see the Python code for the walk-forward SVR pipeline?
> 
> Yes

> [!QUESTION] User
> Which technical indicators will you use as features and why? How do you pick them?

> [!NOTE] Gemini
> To make technical indicators viable for Support Vector Regression (SVR), every feature must satisfy three mathematical constraints:
> 
> 1.  **Strict Stationarity:** Indicators cannot drift with the price level (e.g., raw Moving Averages violate this; ratio transforms fix it).
>     
> 2.  **Orthogonality:** Indicators must represent distinct structural market properties (trend, momentum, volatility, volume) rather than collinear variations of the same formula.
>     
> 3.  **Bounded or Normal Distributions:** SVR optimization relies on inner products and Euclidean distance metrics ($\vert{}\vert{}x_i - x_j\vert{}\vert{}$); unconstrained, heavy-tailed features distort the margin and dominate kernel space.
>     
> 
> ### 1\. Selected Feature Set & Mathematical Formulations
> 
> | Dimension | Indicator | Mathematical Transformation | Hypothesis & Justification |
> | --- | --- | --- | --- |
> | Trend / Level | SMA Ratio | Xtrend​=SMAn​(P)t​Pt​​−1 (n∈{20,50}) | Normalizes moving averages around zero; measures price displacement relative to the dynamic baseline. |
> | Trend Direction | Normalized MACD | Xmacd​=ATR14,t​MACDt​−Signalt​​ | Scaling the histogram by Average True Range (ATR) ensures cross-asset and inter-temporal comparability without dollar dependence. |
> | Momentum | Wilder's RSI | Xrsi​=50RSI14,t​−50​ | Naturally bounded in [0,100]; centered to [−1,1] to align with SVR hyperplanes. Quantifies overbought/oversold exhaustion. |
> | Momentum | Stochastic %K | Xstoch​=H14​−L14​Pt​−L14​​ | Locates closing price relative to recent high-low range. Distinguishes consolidation from breakout acceleration. |
> | Volatility | Normalized ATR | Xnatr​=Pt​ATR14,t​​ | Expresses absolute range as a percentage. Controls for regimes where high volatility dilutes signal-to-noise ratio. |
> | Dispersion | Bollinger %B | X%B​=Uppert​−Lowert​Pt​−Lowert​​ | Standardizes price against local standard deviations (2σ), directly signaling local mean-reverting zones. |
> | Volume-Price | OBV Slope | Xobv​=SMA5​(Volume)t​OBVt​−OBVt−5​​ | Raw OBV is non-stationary and trends indefinitely. Normalizing the 5-day slope by average volume isolates liquidity divergence. |
> 
> ### 2\. Systematic Selection & Pruning Pipeline
> 
> Instead of guessing indicator parameters or throwing hundreds of indicators into the model, execute a 4-stage filter:
> 
> ```
> [Candidate Pool: 30+ Raw TAs] 
>    │
>    ▼
> 1. Stationarity Gate (ADF Test, p < 0.01)
>    │
>    ▼
> 2. Collinearity Pruning (Hierarchical Clustering / VIF < 5)
>    │
>    ▼
> 3. Information-Theoretic Ranking (Mutual Information / mRMR)
>    │
>    ▼
> 4. Out-of-Sample SVR Validation (Cross-Validated IC / MDA)
> ```
> 
> #### Step 1: Stationarity Verification
> 
> Run the **Augmented Dickey-Fuller (ADF)** test on every candidate feature:
> 
> -   Reject any feature with $p \ge 0.01$ (fails unit root test).
>     
> -   If a metric fails, apply logarithmic differencing or ratio transforms until stationarity is achieved.
>     
> 
> #### Step 2: Multicollinearity Removal
> 
> Many indicators measure the exact same underlying signal (e.g., RSI, Stochastic %K, and Williams %R exhibit pairwise correlations $\rho \> 0.85$). Multicollinearity expands the parameter space needlessly and destabilizes SVR support vectors.
> 
> -   **Hierarchical Clustered Feature Selection:** Compute Spearman rank correlation distance matrix $D = 1 - \vert{}\rho\vert{}$.
>     
> -   Form clusters using Ward's linkage.
>     
> -   Retain only the single highest-signal representative per cluster or compute the first principal component (PCA) within each cluster.
>     
> -   Confirm that **Variance Inflation Factor (VIF)** across retained features satisfies $\text{VIF} \< 5$.
>     
> 
> #### Step 3: Information-Theoretic Ranking (mRMR)
> 
> Use **Minimum Redundancy Maximum Relevance (mRMR)** to balance explanatory power against redundancy:
> 
> $$
> \max_{S} \left[ \frac{1}{\vert{}S\vert{}} \sum_{f_i \in S} I(f_i; y) - \frac{1}{\vert{}S\vert{}^2} \sum_{f_i, f_j \in S} I(f_i; f_j) \right]
> $$
> 
> where $I(X; Y)$ is **Mutual Information**. Unlike Pearson correlation, mutual information detects non-linear relationships, which directly benefits non-linear kernels like RBF ($e^{-\gamma \vert{}\vert{}x - x'\vert{}\vert{}^2}$).
> 
> #### Step 4: Time-Series Feature Attribution (SHAP / PFI)
> 
> Evaluate out-of-sample contributions across rolling folds using **Permutation Feature Importance (PFI)**:
> 
> 1.  Train SVR on fold $k$.
>     
> 2.  Permute feature $f_j$ strictly within the validation window.
>     
> 3.  If permuting $f_j$ does not decrease the validation Mean Directional Accuracy (MDA) or Information Coefficient (IC), prune $f_j$ permanently.
>     
> 
> ### 3\. SVR-Specific Considerations
> 
> -   **Lookback Windows:** Avoid fixing a single window (e.g., only 14 days). Test multi-scale resolutions (fast: 5-day, medium: 20-day, slow: 60-day) to capture interactions between short-term momentum and long-term trends.
>     
> -   **Outlier Clipping:** Financial returns exhibit leptokurtosis (fat tails). Clip transformed features at 3 standard deviations (or 1st/99th percentiles) before applying `StandardScaler` to prevent extreme market shocks from collapsing the $\epsilon$\-tube.

> [!QUESTION] User
> Consider making this research in a Jupyter Notebook, write a skeletal outline of the project, consider the ML lifecycle in your organization.

**Gemini:**

Here is an end-to-end skeletal outline for structuring this research in a production-oriented Jupyter Notebook, mapped against the standard enterprise ML lifecycle:

# Research Project: Predictive Edge of Technical Indicators in Equity Pricing via Support Vector Regression (SVR)

```
notebooks/
│
├── 00_environment_and_reproducibility.ipynb
├── 01_data_ingestion_and_universe_definition.ipynb
├── 02_feature_engineering_and_stationarity_gates.ipynb
├── 03_exploratory_data_analysis_and_collinearity.ipynb
├── 04_walk_forward_cross_validation_setup.ipynb
├── 05_model_training_and_hyperparameter_tuning.ipynb
├── 06_statistical_evaluation_and_feature_attribution.ipynb
├── 07_financial_backtest_and_economic_feasibility.ipynb
└── 08_production_handoff_and_governance.ipynb
```

*(Alternatively, run as a single consolidated notebook with the markdown headers below for rapid prototyping.)*

## 1\. Problem Formulation & Reproducibility Setup

*ML Lifecycle Phase: Business Understanding & Project Scoping*

-   **1.1 Research Objective & Hypotheses**
    
    -   Formalize $H_0$ (Technical analysis signals mapped through non-linear SVR do not surpass a random walk after transaction costs) vs. $H_1$.
        
    -   Target definition: 1-day and 5-day forward log returns ($y_t = \ln(P_{t+k} / P_t)$).
        
-   **1.2 Environment & Dependencies**
    
    -   Lock seeds (`numpy`, `random`, `torch`/`scikit-learn`).
        
    -   Log execution metadata: Python runtime, dependency lockfiles (`requirements.txt` / `poetry.lock`), hardware flags (CPU cores, BLAS threads).
        
-   **1.3 Enterprise Experiment Tracking Initialization**
    
    -   Initialize tracking client (e.g., MLflow, Weights & Biases, or internal tracking registry).
        
    -   Set baseline tags: `project_name`, `git_commit_sha`, `data_version`, `model_class: SVR`.
        

## 2\. Data Ingestion & Universe Selection

*ML Lifecycle Phase: Data Engineering & Governance*

-   **2.1 Universe Filtering & Survivorship Bias Mitigation**
    
    -   Define asset selection criteria (e.g., historical constituents of liquid indices like S&P 500 or ETF proxies like SPY/QQQ over a 2015–2025 window).
        
    -   Address corporate actions: split-adjusted and dividend-adjusted closing prices.
        
-   **2.2 Data Quality & Integrity Checks**
    
    -   Missing value profiling (halt trading days, trading halts, zero-volume anomalies).
        
    -   Data leakage guard: verify timestamps correspond to market close (e.g., 16:00 EST) and targets only reference subsequent intervals.
        
-   **2.3 Data Versioning Artifacts**
    
    -   Serialize immutable raw snapshots to object storage (DVC / S3 / parquet registry) with schema hashing.
        

## 3\. Feature Engineering & Mathematical Transformations

*ML Lifecycle Phase: Feature Store / Data Prep*

-   **3.1 Technical Indicator Construction (Dimensionally Grouped)**
    
    -   *Trend:* SMA/EMA log ratios ($\ln(P_t / \text{SMA}_n)$), Normalized MACD histogram ($\text{MACD}_t / \text{ATR}_{14, t}$).
        
    -   *Momentum:* Scaled Wilder’s RSI ($(\text{RSI}_{14} - 50) / 50$), Stochastic Oscillator (%K, %D).
        
    -   *Volatility / Range:* Normalized ATR ($\text{ATR}_{14} / P_t$), Bollinger %B.
        
    -   *Volume-Price:* Normalized OBV delta ($\Delta \text{OBV}_5 / \text{SMA}_5(\text{Vol})$).
        
-   **3.2 Stationarity Testing (Statistical Gate 1)**
    
    -   Run Augmented Dickey-Fuller (ADF) & KPSS tests across all candidate series.
        
    -   Automatically drop/re-difference any feature failing stationarity ($p \ge 0.01$).
        
-   **3.3 Outlier Handling & Transformation**
    
    -   Leptokurtic tail containment: winsorize/clip extreme values at 1st and 99th percentiles based on training window statistics.
        

## 4\. Feature Selection & Collinearity Reduction

*ML Lifecycle Phase: Exploratory Data Analysis & Dimensionality Optimization*

-   **4.1 Pairwise & Cluster Analysis**
    
    -   Compute Spearman rank correlation matrix across indicators.
        
    -   Hierarchical agglomerative clustering (Ward’s linkage) on correlation distance matrix ($D = 1 - \vert{}\rho\vert{}$).
        
-   **4.2 Multicollinearity Filtering**
    
    -   Variance Inflation Factor (VIF) evaluation (target: $\text{VIF} \< 5$).
        
    -   Redundant feature pruning: retain the single highest mutual information representative per cluster.
        
-   **4.3 Information-Theoretic Ranking**
    
    -   Minimum Redundancy Maximum Relevance (mRMR) ranking using non-linear mutual information against the target variable.
        

## 5\. Walk-Forward Validation & Pipeline Assembly

*ML Lifecycle Phase: Validation Framework Architecture*

-   **5.1 Temporal Split Engine**
    
    -   Construct rolling-window / expanding-window time-series CV.
        
    -   Enforce **Purging** (remove overlap between train label forward horizons and test window start) and **Embargo** (post-event buffer to prevent residual autoregression leakage).
        
-   **5.2 Scikit-Learn Pipeline Serialization**
    
    -   Build an atomic `Pipeline`:
        
        -   Step 1: `RobustScaler` / `StandardScaler` (fitted **only** on training fold).
            
        -   Step 2: `SelectKBest` / feature mask from Step 4.
            
        -   Step 3: `SVR()` estimator.
            

## 6\. Model Training & Hyperparameter Optimization

*ML Lifecycle Phase: Modeling & Experimentation*

-   **6.1 Baseline Models**
    
    -   Baseline 1: Naive Martingale / Random Walk ($\hat{y}_{t+k} = 0$).
        
    -   Baseline 2: ElasticNet / Ridge Regression (evaluates linear benchmark).
        
-   **6.2 SVR Hyperparameter Search**
    
    -   Search space:
        
        -   Regularization parameter: $C \in [10^{-2}, 10^3]$
            
        -   Tube insensitivity: $\epsilon \in [10^{-4}, 10^{-1}]$
            
        -   Kernel coefficient: $\gamma \in [\text{'scale'}, \text{'auto'}, 10^{-3}, 10^0]$
            
        -   Kernels: `rbf`, `linear`, `poly` (degree 2)
            
    -   Tuning algorithm: Bayesian Optimization (`optuna` / `scikit-optimize`) within inner temporal CV folds.
        
-   **6.3 Artifact Logging**
    
    -   Log best parameter configs, convergence curves, and fit execution runtimes to MLflow.
        

## 7\. Statistical & Financial Evaluation

*ML Lifecycle Phase: Model Validation & Risk Review*

-   **7.1 Statistical Performance Metrics**
    
    -   Directional metrics: Mean Directional Accuracy (MDA) + binomial test for statistical significance against $p=0.50$.
        
    -   Correlation metrics: Information Coefficient (Spearman rank IC) and Information Ratio of IC (ICIR).
        
    -   Error metrics: RMSE, MAE compared against baseline models.
        
-   **7.2 Economic & Strategy Backtesting**
    
    -   Signal-to-execution mapping: Long/Short/Cash rules driven by predicted forward return thresholds ($\hat{y}_t \gtrless \pm \delta$).
        
    -   Execution friction modeling: Transaction costs (e.g., 5–10 bps), borrow costs for shorts, slippage buffer.
        
    -   Portfolio analytics: Annualized Sharpe, Sortino, Calmar Ratio, Maximum Drawdown (MDD), Turn-over rate.
        
-   **7.3 Model Interpretability & Attribution**
    
    -   Permutation Feature Importance (PFI) evaluated strictly on test slices.
        
    -   SHAP kernel analysis on support vector subsets to diagnose non-linear feature interactions.
        

## 8\. Governance, Packaging & Production Readiness

*ML Lifecycle Phase: Deployment Readiness & Model Governance*

-   **8.1 Model Card & Research Sign-Off**
    
    -   Document assumptions, intended regime conditions, and known failure modes (e.g., sudden macro volatility shifts).
        
-   **8.2 Pipeline Export**
    
    -   Export frozen inference pipeline using ONNX or serialized Joblib container.
        
-   **8.3 Production Drift & Monitoring Plan**
    
    -   Define monitoring specifications: Population Stability Index (PSI) for indicator distribution drift, rolling 30-day IC degradation triggers, and retrain schedules.
        

Want to dive into the code implementation for the Purged Walk-Forward CV and SVR Pipeline in Section 5?

Yes

> [!QUESTION] User
> Now, suppose you finished your experiment, how would you present it to a recruiter other than a Jupyter notebook? Brainstorm ideas that includes something like a dashboard, or a streamlit app.

> [!NOTE] Gemini
> Recruiters and hiring managers rarely open raw `.ipynb` files. A recruiter reviews a portfolio in 30 to 60 seconds, while a technical lead checks for architecture, engineering rigor, and validation hygiene.
> 
> Here are four formats to showcase this experiment across the spectrum of interactivity, engineering depth, and storytelling:
> 
> ### 1\. Interactive Web Application (Streamlit / FastHTML / Gradio)
> 
> An interactive app bridges research and production by letting the reviewer test your models on unseen data in real time.
> 
> **Core Architecture & Views:**
> 
> -   **Tab 1: Executive Overview & The "Verdict"**
>     
>     -   Top-level KPIs: Out-of-sample Information Coefficient (IC), Directional Accuracy (MDA vs. 50% benchmark), Annualized Sharpe Ratio after transaction costs, and Maximum Drawdown.
>         
>     -   Direct takeaway: A concise summary of whether non-linear kernels (RBF SVR) actually captured alpha beyond linear models (Ridge/ElasticNet) or the random-walk baseline.
>         
> -   **Tab 2: Walk-Forward Backtester Sandbox**
>     
>     -   Interactive sliders: Let the reviewer adjust execution parameters (e.g., transaction costs from 0 to 25 bps, prediction hurdle threshold $\delta$, trading horizon $k=1$ vs $k=5$).
>         
>     -   Dynamic equity curves: SVR strategy vs. S&P 500 Buy-and-Hold vs. Naive Momentum baseline, with an interactive drawdown underwater chart.
>         
> -   **Tab 3: Feature Attribution & Interpretability**
>     
>     -   Interactive SHAP summary plots and Permutation Feature Importance (PFI).
>         
>     -   A regime dropdown (e.g., "2020 COVID Crash", "2022 Fed Tightening Cycle", "2024–2025 Tech Rally") showing which indicators (e.g., Normalized ATR vs. RSI vs. SMA Ratio) dominated during specific market conditions.
>         
> -   **Tab 4: Data Hygiene & Leakage Guard**
>     
>     -   A visual diagram of your **Purged & Embargoed Walk-Forward Engine** demonstrating that you accounted for forward-return overlaps and lookahead bias.
>         
> 
> ### 2\. Standalone Production Architecture Demo (FastAPI + Lightweight Frontend)
> 
> If you are targeting quantitative engineering or machine learning engineering (MLE) roles, packaging the model as an operational microservice proves full-stack ML proficiency.
> 
> -   **Components:**
>     
>     -   **Backend:** A containerized FastAPI service exposing inference endpoints:
>         
>         -   `POST /predict/returns`: Ingests latest OHLCV data, calculates stationary technical features, runs inference through a serialized pipeline, and outputs predicted return + confidence margin ($\epsilon$\-tube bounds).
>             
>         -   `GET /health/drift`: Computes Population Stability Index (PSI) or feature drift metrics on incoming data.
>             
>     -   **Interactive Docs:** Live Swagger/OpenAPI docs (`/docs`) where reviewers can execute test API payloads directly in the browser.
>         
>     -   **Packaging:** Hosted live via a free-tier platform (e.g., Render, Fly.io, or Railway) with a linked Dockerfile in the GitHub repository.
>         
> 
> ### 3\. A 60-Second Video Walkthrough (Loom / Screen Recording)
> 
> Technical recruiters often prefer a 90-second video over clicking through a deployment.
> 
> -   **Format (90-second cadence):**
>     
>     -   **0:00–0:15 (The Hook & Thesis):** "Can non-linear SVR extract alpha from technical indicators? Here is what happened over 10 years of out-of-sample walk-forward testing."
>         
>     -   **0:15–0:45 (Engineering Integrity):** Show the live Streamlit dashboard, pointing specifically to the purged walk-forward cross-validation and transaction cost simulation to prove you avoided standard backtest overfitting traps.
>         
>     -   **0:45–1:15 (Key Discovery):** Highlight the SHAP attribution and the Sharpe ratio curve after 10 bps slippage.
>         
>     -   **1:15–1:30 (Tech Stack & Links):** Mention the clean codebase, automated unit tests, and CI/CD pipeline, directing them to the live app and repo links.
>         
> 
> ### 4\. Technical Case Study / Visual Post-Mortem
> 
> Publishing an executive case study (hosted on a personal engineering blog, GitHub Pages, or a polished Substack/Medium article) positions you as a thoughtful researcher who communicates technical outcomes effectively.
> 
> -   **Key Sections to Feature:**
>     
>     -   **The "What Went Wrong" Section:** Machine learning in finance is noisy. Discussing why raw moving averages caused lookahead/non-stationarity failure and how you solved it with ratio transforms demonstrates domain maturity far more than claiming a 90% accuracy rate.
>         
>     -   **Visual Diff Tables:** Direct comparisons of Baseline Linear Model vs. Linear SVR vs. RBF SVR vs. Random Walk.
>         
>     -   **Reproducibility Badge:** Link to a 1-click binder or Google Colab environment and automated GitHub Actions workflow passing unit tests for the data transformation pipeline.
>         
> 
> ### Suggested Portfolio Presentation Matrix
> 
> | Recruiter Persona | Primary Deliverable | What They Look For |
> | --- | --- | --- |
> | HR / Non-Technical Recruiter | 90-second Loom Video + Streamlit App Overview | Clear metrics, clean presentation, concise communication of business/financial impact. |
> | Quant Researcher / Senior Data Scientist | Streamlit Backtest Sandbox + Written Case Study | Methodological rigor, handling of non-stationarity, out-of-sample IC, realistic transaction friction. |
> | Machine Learning Engineer / Tech Lead | FastAPI API Docs + Dockerfile + Clean GitHub Repo | Clean code structure, typing (pydantic), vectorized operations, CI/CD pipeline, and inference latency. |
> 
> Want to see the Streamlit app code structure to build this dashboard?
> 
> Yes