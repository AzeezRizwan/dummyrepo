from fastapi import FastAPI 
from pydantic   import BaseModel,field_validator,model_validator
import argparse
parse= argparse.ArgumentParser()
subparsers= parse.add_subparsers(dest="command")
class restaurent(BaseModel):
    friend_name: str
    phone_number: int
    friend_balance: int
    friend_suggestion: str
    @field_validator("friend_name")
    def restaurent_details(cls, value):
        if len(value) >=5:
            print(" Hii da!! vaa ulla va!! welcome")
            return value
    @model_validator(mode="after")
    def validate (self)->"restaurent":
        if (self.friend_balance)>2000:
            print("enna sapadra!! saptu unnoda suggestion sollitu po have a good day!!")
            return self
waiter=subparsers.add_parser("restaurent")
waiter.add_argument("friend_name")
waiter.add_argument("phone_number")
waiter.add_argument("friend_balance")
waiter.add_argument("friend_suggestion")
args=parse.parse_args()
if args.command=="restaurent":
    waiter= restaurent(friend_name=args.friend_name,phone_number=args.phone_number,friend_balance=args.friend_balance,friend_suggestion=args.friend_suggestion)
    print(waiter)