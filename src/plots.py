from lightgbm import plot_importance
import matplotlib.pyplot as plt
import style
import numpy as np
import pandas as pd

def plot_actual_pred_diff(y_actual, y_pred):
    plt.figure()
    plt.plot(y_actual.iloc[:500].values,
             label = "Actual", 
             color = style.COLORS["primary"])
    plt.plot(y_pred[:500],
             label = "Predicted",
             color = style.COLORS["accent"]
             )
    plt.legend()
    plt.title("Actual vs Predicted Prices")
    plt.show()

def plot_actual_pred_scatter(y_actual, y_pred):
    plt.figure()
    plt.scatter(y_actual, y_pred, alpha = 0.2, 
                color = style.COLORS["accent"])
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted Scatter")
    lims = [min(y_actual.values.min(), y_pred.min()),
            max(y_actual.values.max(), y_pred.max())]
    plt.plot(lims, lims, 
             color = style.COLORS["primary"])
    plt.show()

def plot_residual(y_actual, y_pred):
    residual = y_actual - y_pred
    plt.figure()
    plt.hist(residual, bins = 100, 
             color = style.COLORS["primary"])
    plt.title("Residual Errors Histgram")
    plt.show()

def plot_error_by_price_quantile(y_actual, y_pred):
    y_actual_quantiles = pd.qcut(y_actual, 10, 
                                 labels = [
                                     "0-10%",
                                     "10-20%",
                                     "20-30%",
                                     "30-40%",
                                     "40-50%",
                                     "50-60%",
                                     "60-70%",
                                     "70-80%",
                                     "80-90%",
                                     "90-100%"
                                 ])
    
    df_quantile_errors = pd.DataFrame(
        {
            "actual": y_actual,
            "predicted": y_pred,
            "quantile_bin": y_actual_quantiles
        }
    )

    df_quantile_errors["abs_error"] = (np.abs(
        df_quantile_errors["actual"] - df_quantile_errors["predicted"]))
    
    mae_by_bin = (df_quantile_errors.groupby(
        "quantile_bin", observed = False
    )["abs_error"].mean())

    mae_by_bin.plot(kind = "bar", 
                    color = style.COLORS["primary"])
    plt.xlabel("Price Quantile Bin")
    plt.ylabel("MAE")
    plt.title("MAE Price Quantile")
    plt.xticks(rotation = 45, ha = "right")
    plt.show()

    rsme_by_bin = (df_quantile_errors.assign(
        squared_error = lambda x: (x["actual"] - x["predicted"])**2
    ).groupby("quantile_bin", observed = False)["squared_error"]
    .mean()
    .pipe(np.sqrt)
    )

    rsme_by_bin.plot(kind = "bar", 
                     color = style.COLORS["primary"])
    plt.xlabel("Price Quantile Bin")
    plt.ylabel("RSME")
    plt.title("RSME Price Quantile")
    plt.xticks(rotation = 45, ha = "right")
    plt.show()

def plot_feature_importance(model):
    plot_importance(
        model, 
        max_num_features = 15,
        color = style.COLORS["primary"]
    )
    plt.show()

