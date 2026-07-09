import joblib
import pandas as pd

from inventory.models import Inventory

model = joblib.load(
    "data_science/saved_models/best_model.pkl"
)


def generate_recommendations():

    recommendations = []

    inventories = Inventory.objects.select_related(
        "product",
        "store"
    )

    for item in inventories:

        features = pd.DataFrame([{

            "price": item.product.unit_price,

            "month": 7,

            "day": 1,

            "week": 27,

            "quarter": 3,

            "year": 2026,

            "is_weekend": 0,

            "is_holiday": 0,

            "promotion": 0,

            "lag_1": 50,

            "rolling_avg_7": 48,

            "season_Autumn": 0,

            "season_Spring": 0,

            "season_Summer": 1,

            "season_Winter": 0,

            "revenue": item.product.unit_price * 50

        }])

        forecast = model.predict(features)[0]

        if item.current_stock < item.safety_stock:

            status = "Low Stock Alert"

        elif forecast > item.current_stock:

            status = "Restock"

        elif item.current_stock > forecast * 2:

            status = "Overstock"

        elif forecast >= 100:

            status = "Fast Moving"

        else:

            status = "Slow Moving"

        recommendations.append({

            "product": item.product.name,

            "store": item.store.name,

            "forecast": round(float(forecast), 2),

            "current_stock": item.current_stock,

            "safety_stock": item.safety_stock,

            "recommendation": status

        })

    return recommendations