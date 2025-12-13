from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI()

class shop (BaseModel):
    customer_name : str
    bill_id : int=123
    contact_number :str = Field(...,max_length=10)
    
@app.put("/route")
def customer_details(route:shop):
    return{
        "message":"Hello! welcome",
        "customer_details": route

     }

@app.delete("/delete")
def customer_details(delete:shop):
    return{
        "message":"Bye!! I have deleted it!",
        "customer_details": delete

     }


     