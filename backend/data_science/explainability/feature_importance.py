import joblib
import pandas as pd
import matplotlib.pyplot as plt


##----------------Here We are calculating the feature importance-----------------

model = joblib.load(
    "data_science/saved_models/best_model.pkl"
)

df = pd.read_csv(
    "data_science/feature_data/training_dataset.csv"
)

X = df.drop(columns=["quantity"])

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

importance.plot(
    x="Feature",
    y="Importance",
    kind="bar",
    figsize=(12,6)
)

plt.tight_layout()

plt.savefig(
    "data_science/explainability/shap_plots/feature_importance.png"
)

plt.close()