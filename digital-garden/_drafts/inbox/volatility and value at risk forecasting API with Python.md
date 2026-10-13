---
tags:
  - Time-series-analysis
Type: Project
---
AI-notes
- [[Is there an end-user workflow that uses both volatility and VaR. My API only calculates one stock at a time.]]
- [[Does it make sense to calculate both parametric and historical var]]
- [[Would a 1-year or 252-day EOD data enough training sample for this usecase]]


# Current Tasks
- [ ] Work on /model/fit endpoint
	- [x] Create function for retrieving data from database and from API
	- [x] Create the logic for creating a GARCH model
	- [x] Work on displaying the correct JSON response in the endpoint
	- [ ] Save the model
- [ ] Work on /model/forecast endpoint
- [ ] Work on /models and /models /{model-id} endpoint









JSON DESIGN  
POST /volatility = predict volatility  
```
"volatility_metrics": {  
    "current_spot_volatility": 0.2200,  
    "long_term_mean_volatility": 0.1350,  
    "regime": "intensifying",  
    "term_structure": [  
      { "horizon_days": 1, "forecasted_volatility": 0.2180 },  
      { "horizon_days": 5, "forecasted_volatility": 0.1950 },  
      { "horizon_days": 15, "forecasted_volatility": 0.1620 },  
      { "horizon_days": 30, "forecasted_volatility": 0.1410 }  
    ]  
      
 "value_at_risk_metrics": {  
    "parametric_var_usd": 2600.00,  
    "historical_var_usd": 2450.00,  
"var_percentage_of_portfolio": 2.60
  }
```


**Notes on existing classes**

- `data.py`
	- `SQLRepository` - manages saving and retrieving data from the SQL database
	- `TwelveDataAPI` - manages getting data from Twelve Data API
- `model.py`
	- `GARCHModel` - manages all actions relating to the GARCH model


**Notes on endpoints**
- `diagnostic/check`
	- [ ] Get data
	- [ ] Run `het_arch` & `ADF`
- `/model/fit`
	- `build_model()`: creates a `GARCHModel` instance
	- `wrangle_data()`: extracts data from database 


# How to run the program

```python
fastapi dev main.py
```

# Updated Endpoint Architecture
- GET */models*
	- Returns a list of saved models satisfying a filter criteria
- GET */models/{model_id}*
	- Returns key information about a saved model
- GET  */diagnostics/check*
	- Checks for stationarity and ARCH effects
- POST */models/fit*
	- Fits a GARCH model and saves it.
- POST */models/forecast*
	- Returns a forecast of 

# Program flow for /model/fit

model/fit: fits a GARCH model and returns the name, with specific information about the model
1. Get data
2. Train GARCH model
3. Save model
4. Build response
5. Return response

Response Schema:
```json
{
  "status": "success",
  "model_id": "garch_AAPL_20260824_9f8b2c",
  "identifier": "AAPL",
  "model_type": "GARCH(1,1)",
  "distribution": "student_t",
  "trained_at": "2026-08-24T19:56:43Z",
  "data_summary": {
    "start_date": "2023-08-25",
    "end_date": "2026-08-24",
    "total_observations": 756,
    "last_close_price": 225.40
  },
  "parameters": {
    "mu": 0.0008,
    "omega": 0.000015,
    "alpha": { "alpha[1]": 0.085 },
    "beta": { "beta[1]": 0.895 },
    "nu": 6.45
  },
  "diagnostics": {
    "converged": true,
    "log_likelihood": 2341.12,
    "aic": -4672.24,
    "bic": -4649.10,
    "persistence": 0.98,
    "last_conditional_volatility_daily": 0.0142,
    "last_conditional_volatility_annualized": 0.2254
  },
  "message": "GARCH model successfully trained and persisted. Reference model_id for forecasts."
}
```


# Response schema for a /models/forecast
```JSON
{
  "model_id": "garch_AAPL_20260714_9f8b2c",
  "ticker": "AAPL",
  "as_of_date": "2026-07-14T16:00:00Z",
  "forecast_horizon_days": 1,
  "confidence_level": 0.99,
  "volatility_analysis": {
    "conditional_volatility_daily": 0.0185,
    "conditional_volatility_annualized": 0.2937,
    "trend": "expanding",
    "persistence_half_life_days": 7.4
  },
  "value_at_risk": {
    "value_at_risk_pct": -0.0432,
    "dollar_loss_per_10k": -432.00,
    "conditional_var_pct": -0.0585
  },
  "metadata": {
    "model_type": "EGARCH(1,1)",
    "distribution": "skewed_student_t",
    "model_auto_refreshed": false
  }
}
```


# Implementation
```Python
import sqlite3
import pandas as pd

# Hardcoded exchange configuration
EXCHANGE_TZ = "America/New_York"
EOD_AVAILABLE_HOUR = 17  # 5:00 PM Eastern (allows buffer for data vendor to post EOD)

def get_latest_expected_eod() -> pd.Timestamp:
	"""
	
	"""
    now_ny = pd.Timestamp.now(tz=EXCHANGE_TZ)
    
    # If it's before 5:00 PM Eastern, the latest completed EOD bar is from the previous business day
    if now_ny.hour < EOD_AVAILABLE_HOUR:
        expected = now_ny - pd.tseries.offsets.BDay(1)
    else:
        expected = now_ny
        
    # If the computed date falls on a weekend, roll back to Friday
    if expected.dayofweek > 4:
        expected -= pd.tseries.offsets.BDay(1)
        
    # Return as timezone-naive midnight timestamp to match SQLite date formats
    return expected.normalize().tz_localize(None)

def get_eod_data(ticker: str, lookback_years: int = 3) -> pd.Series:
    expected_eod = get_latest_expected_eod()
    
    with sqlite3.connect("market_data.db") as conn:
        query = "SELECT date, close FROM prices WHERE ticker = ? ORDER BY date ASC"
        df = pd.read_sql(query, conn, params=(ticker,), parse_dates=["date"])
        
        # Refresh only if DB is empty or lacks the latest completed session
        if df.empty or df["date"].max() < expected_eod:
            fresh_df = fetch_from_stock_api(ticker, lookback_years)
            
            if not fresh_df.empty:
                fresh_df["ticker"] = ticker
                # Atomic cache refresh per ticker
                conn.execute("DELETE FROM prices WHERE ticker = ?", (ticker,))
                fresh_df.to_sql("prices", conn, if_exists="append", index=False)
                df = fresh_df
                
    return df.set_index("date")["close"]
```