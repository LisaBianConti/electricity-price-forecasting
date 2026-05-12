from sklearn.metrics import (mean_absolute_error, 
                             root_mean_squared_error)

def evaluate_regression(y_actual, y_pred):

    return {
        "mae": mean_absolute_error(y_actual, y_pred),
        "rmse": root_mean_squared_error(y_actual, y_pred)
    }