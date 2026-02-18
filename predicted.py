import pickle
import pandas as pd

with open('model_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)


def prediction(data: dict):

    df = pd.DataFrame([data])

    pred = model.predict(df)[0]

    return int(pred)
