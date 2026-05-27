

import joblib
import pandas as pd
import numpy as np


model = joblib.load("sales_prediction_model.pkl")


model_features = getattr(model, "feature_names_in_", None)




def make_prediction(input_data: dict):

    df = pd.DataFrame([input_data])

    
    if model_features is None:
        raise ValueError("model_features is None")

    missing = set(model_features) - set(df.columns)
    for col in missing:
        df[col] = 0

   
    df = df[model_features]

    prediction = model.predict(df)[0]

    return max(float(prediction), 0)