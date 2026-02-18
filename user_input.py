from  pydantic import BaseModel, Field, computed_field , field_validator
from typing import Literal,Annotated  

class UserInput(BaseModel):
    Age: Annotated[int, Field(...,gt = 0 , description = "age of the coustomer")]
    Gender : Annotated[Literal['Male','Female','Other'],Field(..., description="Gender of the coustmer")]
    Tenure : Annotated[int, Field(...,gt = 0 , description = "tenure of the coustomer in months")]
    Usage_Frequency : Annotated[int, Field(...,gt = 0 , description = "usage frequency of the coustomer in times per month")]
    Support_Calls : Annotated[int, Field(...,gt = -1, description = "number of support calls made by the coustomer")]
    Payment_Delay : Annotated[int, Field(...,gt = -1, description = "payment delay of the coustomer in days")]
    Subscription_Type : Annotated[Literal['Basic','Standard','Premium'], Field(..., description = "subscription type of the coustomer")]
    Contract_Length : Annotated[Literal['Monthly', 'Annual', 'Quarterly'], Field(..., description = "contract length of the coustomer")]
    Total_Spend : Annotated[int, Field(...,gt = 0 , description = "total spend of the coustomer ")]
    Last_Interaction : Annotated[int, Field(...,gt = -1, description = "last interaction of the coustomer in days")]
    
    @field_validator('Gender','Subscription_Type','Contract_Length')
    @classmethod
    def normalize(cls,v:str) -> str:
        return v.strip().title()
    