def add_price_features(df, 
                       lags = None,
                       rolling_windows = None):
    df = df.copy()
    if lags is not None:
        for lag in lags:
            df[f"price_lag_{lag}"] = (df["Day-ahead Price (EUR/MWh)"].shift(lag))
    if rolling_windows is not None:
        for window in rolling_windows:
            df[f"price_roll_mean_{window}"] = (df["Day-ahead Price (EUR/MWh)"]
                                               .rolling(window).mean())
            df[f"price_roll_std_{window}"] = (df["Day-ahead Price (EUR/MWh)"]
                                              .rolling(window).std())
            df[f"price_roll_max_{window}"] = (df["Day-ahead Price (EUR/MWh)"]
                                              .rolling(window).max())
            df[f"price_roll_min_{window}"] = (df["Day-ahead Price (EUR/MWh)"]
                                              .rolling(window).min())
            
    return df