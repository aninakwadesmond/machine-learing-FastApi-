from fastapi import FastAPI

from routes.user import user

app = FastAPI()

print("hello")
app.include_router(user)