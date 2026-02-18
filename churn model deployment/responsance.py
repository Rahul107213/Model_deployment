from pydantic import BaseModel, Field

class Predicted_response(BaseModel):
        predicted_churn: int = Field(..., description="Predicted churn status of the customer (0 for not churn, 1 for churn)")
        