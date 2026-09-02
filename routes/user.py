from fastapi import APIRouter

from models.userData import userInputs
from schema.user import serialize, serializers

import pickle


user = APIRouter()

with open("model.sav", "rb") as file:
  model = pickle.load(file)

print("model_type" , type(model))

@user.post('/')
async def userInputs(user: userInputs): 
  print(user)
  user_input = serialize(user)
  list_output = list(user_input.values())
  print("this is user inputs", user_input,list_output)
  prediction =   model.predict([list_output])
  print("prediction: ", prediction)
  print("this is user inputs", user_input,list_output)
  return {"fraud_risk_score": float(prediction[0])}


