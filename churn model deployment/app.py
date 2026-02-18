from fastapi import FastAPI
from fastapi.responses import JSONResponse
from user_input import UserInput
from predicted import prediction as predict_fn

from responsance import Predicted_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Churn Prediction API"}

@app.post("/predict", response_model=Predicted_response)
def predict_churn(data: UserInput):
    user_input_dict = {
        "Age": data.Age,
        "Gender": data.Gender,
        "Tenure": data.Tenure,
        "Usage_Frequency": data.Usage_Frequency,
        "Support_Calls": data.Support_Calls,
        "Payment_Delay": data.Payment_Delay,
        "Subscription_Type": data.Subscription_Type,
        "Contract_Length": data.Contract_Length,
        "Total_Spend": data.Total_Spend,
        "Last_Interaction": data.Last_Interaction    
    }
    
    try:
        result = predict_fn(user_input_dict)

        return {'predicted_churn': result}


    except Exception as e:
        return {"error": str(e)}
