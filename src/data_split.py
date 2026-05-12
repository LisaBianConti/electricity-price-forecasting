def split_data(df, features):
    
    df_train = df[(df.index.year >= 2016) & (df.index.year <= 2020)].copy()
    df_val = df[df.index.year == 2021].copy()
    df_test = df[df.index.year == 2022].copy()
    df_recovery = df[(df.index.year >= 2023) & (df.index.year <= 2024)].copy()

    X_train = df_train[features]
    y_train = df_train[["target_price"]]

    X_val = df_val[features]
    y_val = df_val["target_price"]

    X_test = df_test[features]
    y_test = df_test["target_price"]

    X_recovery = df_recovery[features]
    y_recovery = df_recovery["target_price"]

    return (
        X_train, 
        y_train,
        X_val,
        y_val,
        X_test,
        y_test,
        X_recovery,
        y_recovery
    )