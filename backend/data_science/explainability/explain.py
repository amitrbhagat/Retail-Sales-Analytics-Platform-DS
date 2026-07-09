import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load(
    "data_science/saved_models/best_model.pkl"
)

df = pd.read_csv(
    "data_science/feature_data/training_dataset.csv"
)

X = df.drop(columns=["quantity"])

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.savefig(
    "data_science/explainability/shap_plots/summary_plot.png"
)

plt.close()

shap.summary_plot(
    shap_values,
    X,
    plot_type="bar",
    show=False
)

plt.savefig(
    "data_science/explainability/shap_plots/bar_plot.png"
)

plt.close()