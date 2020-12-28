from typing import Optional
import os
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from starlette.requests import Request

from fastapi_mail import ConnectionConfig,FastMail, MessageSchema

app = FastAPI()


class Email(BaseModel):
    fistName: str
    lastName: str
    email: EmailStr
    message : str

conf = ConnectionConfig(
    MAIL_PASSWORD = os.environ['MAIL_PWD'],
    MAIL_FROM = "tiaret.shopper@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False
)
template = """
<p>Hi this test mail using BackgroundTasks, thanks for using Fastapi-mail</p> 
"""

@app.get("/send_mail")
async def simple_send() -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=['chihabeddineben@gmail.com'],  # List of recipients, as many as you can pass
        body=template,
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/emails/{email_id}")
def read_item(email_id: int):
    return {"email_id": email_id}


@app.put("/emails/{email_id}")
def update_item(email_id: int, email: Email):
    return { "email_id": email_id}