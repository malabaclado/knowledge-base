---
id: gemini_f50d713d93f59072
title: Snowflake Project Idea
source: gemini
url: https://gemini.google.com/app/f50d713d93f59072
created: 2026-08-31T13:27:52+08:00
modified: 2026-08-31T13:27:52+08:00
tags:
  - ai-conversation
  - gemini
message_count: 2
---

> [!QUESTION] User
> I've passed Snowflake's SnowPro® Core Certification. Use this URL as reference: https://learn.snowflake.com/en/certifications/snowpro-core-c03/?pdf_name=SnowProCoreStudyGuideC03
> Now help me brainstorm for portfolio projects I can do now that I can show to potential employers.  I need help with:
> What story should the project tell? (It should solve a business problem)
> Where do I get the data?
> Consider only free/no-cost ideas.

> [!NOTE] Gemini
> Congratulations on earning your SnowPro® Core Certification!
> 
> To stand out to hiring managers, your portfolio projects should move beyond basic SQL scripts and showcase **end-to-end cloud data engineering**, architectural decision-making, cost awareness, and governance.
> 
> Here are three distinct, production-grade portfolio project blueprints designed to demonstrate core Snowflake capabilities using **100% free data and free tiers** (Snowflake 30-day trial + AWS/GCP free tier + GitHub).
> 
> ## 1\. Automated Financial Market Data Lakehouse & Real-Time Alerting
> 
> ### The Business Problem & Story
> 
> > *"Our quantitative research and risk management teams need near real-time ingestion of tick-level and end-of-day market movements, macroeconomic indicators, and trade anomalies, without paying for expensive 24/7 dedicated compute clusters."*
> 
> You design an event-driven, serverless ingestion and transformation pipeline that ingests daily market data, parses semi-structured feeds, automatically tracks changing dimensions (SCD Type 2), and alerts on price volatility thresholds.
> 
> -   **Free Data Sources:**
>     
>     -   **Alpha Vantage / Yahoo Finance (`yfinance` Python library)**: Free daily and intraday OHLCV stock and crypto price feeds (CSV/JSON).
>         
>     -   **FRED (Federal Reserve Economic Data) API**: Free macroeconomic data (interest rates, CPI, Treasury yields).
>         
>     -   **SEC EDGAR API**: Public corporate filings and quarterly statements.
>         
> -   **Key Snowflake Features Demonstrated:**
>     
>     -   **Continuous Loading:** External Stages (AWS S3/GCS bucket free tier) configured with **Snowpipe** (or auto-ingest with simulated events).
>         
>     -   **Semi-Structured Data Handling:** Ingesting raw JSON payloads directly into `VARIANT` columns and querying them with `FLATTEN` and dot-notation paths.
>         
>     -   **Change Data Capture (CDC):** **Streams and Tasks** to compute continuous aggregations (e.g., 20-day Moving Averages, Volatility Index) down to presentation views.
>         
>     -   **Cost Governance:** Multi-cluster warehouse auto-suspend policies (60 seconds) and resource monitors.
>         
> 
> ## 2\. Secure Multi-Tenant Healthcare & Clinical Analytics Hub
> 
> ### The Business Problem & Story
> 
> > *"A healthtech provider needs to share patient analytics with third-party hospital networks and researchers while complying with strict privacy regulations (HIPAA/GDPR). Personally Identifiable Information (PII) must be dynamically obfuscated depending on the user's role."*
> 
> You build a governed data platform featuring medallion architecture (Bronze/Silver/Gold) where raw clinical logs are transformed, scrubbed, and shared securely using Snowflake’s native governance and zero-copy data sharing.
> 
> -   **Free Data Sources:**
>     
>     -   **MIMIC-IV Demo / Synthea**: Open-source, synthetic electronic health records (EHR) containing patient encounters, medications, and conditions in CSV/JSON format.
>         
>     -   **CDC / WHO Open Data**: Public regional disease and vaccination statistics.
>         
> -   **Key Snowflake Features Demonstrated:**
>     
>     -   **Role-Based Access Control (RBAC):** Hierarchical role structure (`SECURITYADMIN`, `ANALYST_ROLE`, `RESEARCHER_ROLE`, `DATA_ENGINEER`).
>         
>     -   **Data Governance & Privacy:** **Dynamic Data Masking** (masking patient names and IDs based on current role) and **Row Access Policies (RAP)** to restrict hospitals to their own regional records.
>         
>     -   **Zero-Copy Cloning & Time Travel:** Demonstrating continuous data protection by creating a dev/testing clone without incurring storage costs, and running `UNDROP` or query-level Time Travel after a simulated bad update.
>         
>     -   **Direct Secure Data Sharing:** Sharing reader views across Snowflake accounts without data duplication.
>         
> 
> ## 3\. High-Throughput E-Commerce Clickstream & Funnel Intelligence Engine
> 
> ### The Business Problem & Story
> 
> > *"A retail platform experiences heavy web traffic spikes. Marketing needs to identify high-dropoff checkout steps and compute customer lifetime value (LTV), but unpartitioned tables and inefficient queries are causing query timeouts and runaway compute bills."*
> 
> You engineer a high-throughput event processing warehouse using dbt Core and Snowflake, optimizing query pruning, micro-partitioning, and clustering keys for analytical dashboards.
> 
> -   **Free Data Sources:**
>     
>     -   **Kaggle eCommerce Clickstream Dataset**: Large-scale logs of visitor actions (views, cart adds, purchases).
>         
>     -   **Snowflake Sample Data (`SNOWFLAKE_SAMPLE_DATA` shared database)**: Native TPCH/TPCDS benchmark datasets (up to 10TB scale) available inside every Snowflake account.
>         
> -   **Key Snowflake Features Demonstrated:**
>     
>     -   **Data Modeling:** Modern ELT pipeline orchestrated via **dbt Core** (staging, intermediate, and dimensional marts).
>         
>     -   **Performance Tuning:** Query Profiler analysis, Search Optimization Service, Clustering Keys on date/tenant columns, and Materialized Views.
>         
>     -   **Native Visualization:** Embedding an interactive **Streamlit in Snowflake (SiS)** app directly inside Snowflake for marketing stakeholders.
>         
> 
> ## How to Package the Project for Maximum Impact
> 
> | Component | What Employers Look For |
> | --- | --- |
> | Architecture Diagram | Visual flow showing Raw Source → Cloud Storage → Snowpipe → Medallion Layers (Bronze/Silver/Gold) → BI/Streamlit. |
> | GitHub Repository | Modular SQL DDLs, automated CI/CD migration scripts (e.g., using schemachange or dbt), clean folder structure, and detailed README.md. |
> | Cost & Efficiency Metrics | Documented benchmarks: "Reduced query execution time by 68% using custom clustering and reduced warehouse runtime via optimized Task intervals." |
> 
> Where would you like to dive in first to start building?
> 
> Draft the dbt and Stream/Task code for the Financial Market project
> 
> Design the RBAC and Dynamic Data Masking scripts for the Healthcare project
> 
> Generate a detailed README and Architecture Diagram template