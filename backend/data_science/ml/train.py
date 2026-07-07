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


#------------------------Random forest---------------------------------------------------

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)


#----------------------XGBoost------------------------------------------------------------

xgb = XGBRegressor(random_state = 42)

xgb.fit(X_train, y_train)

xgb_pred = xgb.predict(X_test)


#----------------------LightBGM-------------------------------------------------------

from lightgbm import LGBMRegressor

lgbm = LGBMRegressor(
    random_state=42
)

lgbm.fit(X_train, y_train)

lgbm_pred = lgbm.predict(X_test)


#----------------------Model Evaluation----------------------------------

def evaluate(name, y_true, y_pred):
    print("=" * 40)
    print(name)
    print("MAE :", mean_absolute_error(y_true, y_pred))
    print("MSE :", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R2 :", r2_score(y_true, y_pred))   


evaluate("Linear Regression", y_test, lr_pred)
evaluate("Random Forest", y_test, rf_pred)
evaluate("XGBoost", y_test, xgb_pred)
evaluate("LightBGM", y_test, lgbm_pred)


#-----------------------------Cross Validation-----------------------------------

scores = cross_val_score(
    rf,
    X,
    y,
    cv=5,
    scoring="r2"
)

print(scores.mean())


#---------------------------HyperParameter Tuning----------------------------

params = {
    "n_estimators" : [10,200],
    "max_depth":[10,20]
}

grid = GridSearchCV(
    rf,
    params,
    cv=3
)

grid.fit(X_train, y_train)

print(grid.best_params_)


#-----------------------save Best model-------------------------------------

joblib.dump(
    rf,
    "data_science/saved_models/random_forest.pkl"
)