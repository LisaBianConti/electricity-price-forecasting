# French Electricity Price Forecasting

## Project Overview

This project investigates whether French day-ahead electricity prices can be forecast using historical market information, including electricity demand, renewable generation, and past market prices.

The project combines data analysis, SQL querying, feature engineering, and machine learning to explore the key drivers of electricity price dynamics and evaluate the predictive performance of different forecasting approaches.

## Business problem

Electricity markets are becoming increasingly complex due to the growing penetration of renewable energy sources. Variations in electricity demand, wind generation, solar generation, and market conditions can lead to substantial price volatility.

Accurate short-term price forecasting is valuable for:
- Energy traders
- Grid operators
- Utility companies
- Renewable energy producers

This project aims to predict the next-hour French day-ahead electricity price using historical market data.

## Dataset

The analysis uses publicly available French electricity market data, including
- Electricity demand (MW)
- Offshore wind generation (MW)
- Onshore wind generation (MW)
- Solar generation (MW)
- Day-ahead electricity price (EUR/MWh)

The dataset was cleaned, validated, and transformed into a machine-learning ready format before modeling.

## Project Workflow

1. Data collection
2. Data cleaning and preprocessing
3. Exploratory data analysis (EDA)
4. SQL-based business analysis
5. Feature engineering
6. Baseline models
7. LightGBM modelling
8. Model evaluation and error analysis

## Key Findings

- Electricity prices show strong daily and seasonal patterns.
- Renewable generation contributes to price suppression during periods of high production.
- High-price events are rare but dominate forecasting errors.
- Simple lag-based baselines outperform an untuned LightGBM model.
- Additional feature engineering is required to capture scarcity events.

## Modelling Result

|Model | MAE | RMSE|
|-----|-----|-----|
|Lag-1 Persistence |	9.05 | 14.25 |
|1Lag-23 Daily Baseline | 19.74 | 31.94|
|LightGBM |	21.68 |	50.80|

## Discussion

The LightGBM model did not outperform the simple Lag-1 Persistence benchmark.
This outcome aligns with the common challenge in electricity price forecasting: strong temporal autocorrelation often allows simple models to perform remarkably well. 
The results suggest that additional feature engineering and specialized treatment of extreme price events are required before machine learning models can consistently exceed baseline performance.

## Repository Structure

|├── notebooks/ |
|├── src/ |
|├── sql/ |
|├── reports/ |
|│ └── figures/ |
|├── README.md |
|├── requirements.txt |
|└── .gitignore |

## Planned Improvements

- Hyperparameter optimization using time-series cross-validation
- Additional lag features
- Scarcity event modelling
- Quantile regression
- XGBoost comparison
- CatBoost comparison

## Key Takeaway

The project demonstrates an end-to-end data science workflow, from data acquisition and SQL analysis through feature engineering, machine learning, and model evaluation. A particularly important finding is that sophisticated machine learning models do not automatically outperform strong baseline models, emphasizing the importance of benchmark-driven model development.
