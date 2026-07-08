import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import joblib


df = pd.read_csv("data_science/feature_data/training_dataset.csv")

X = df.drop(columns = ["quantity"])
y = df["quantity"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)


#-------------------------Linear regression---------------------------------------------

lr = LinearRegression();

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("lr Done")


#------------------------Random forest---------------------------------------------------

rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("rf Done")


#----------------------XGBoost------------------------------------------------------------

xgb = XGBRegressor(random_state = 42)

xgb.fit(X_train, y_train)

xgb_pred = xgb.predict(X_test)

print("xgb Done")


#----------------------LightBGM-------------------------------------------------------

from lightgbm import LGBMRegressor

lgbm = LGBMRegressor(
    random_state=42
)

lgbm.fit(X_train, y_train)

lgbm_pred = lgbm.predict(X_test)

print("lgbm Done")


#----------------------Model Evaluation----------------------------------

def evaluate(name, y_true, y_pred):

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    print("=" * 40)
    print(name)
    print("MAE :", mae)
    print("RMSE :", rmse)
    print("R2 :", r2)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


#-----------------------------Cross Validation-----------------------------------

# scores = cross_val_score(
#     rf,
#     X,
#     y,
#     cv=5,
#     scoring="r2"
# )

# print(scores.mean())


#---------------------------HyperParameter Tuning----------------------------

# params = {
#     "n_estimators" : [10,200],
#     "max_depth":[10,20]
# }

# grid = GridSearchCV(
#     rf,
#     params,
#     cv=3
# )

# grid.fit(X_train, y_train)

# print(grid.best_params_)


#-----------------------Compare models-------------------------------------

results = {

    "Linear Regression": evaluate(
        "Linear Regression",
        y_test,
        lr_pred
    ),

    "Random Forest": evaluate(
        "Random Forest",
        y_test,
        rf_pred
    ),

    "XGBoost": evaluate(
        "XGBoost",
        y_test,
        xgb_pred
    ),

    "LightGBM": evaluate(
        "LightGBM",
        y_test,
        lgbm_pred
    )
}

comparison = pd.DataFrame(results).T
print(comparison)

best_model_name = comparison["R2"].idxmax()

print(f"Best Model: {best_model_name}")

#-----------------------save Best model-------------------------------------

models = {
    "Linear Regression": lr,
    "Random Forest": rf,
    "XGBoost": xgb,
    "LightGBM": lgbm,
}


joblib.dump(
    models[best_model_name],
    "data_science/saved_models/best_model.pkl"
)
