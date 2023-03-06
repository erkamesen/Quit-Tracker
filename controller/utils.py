from flask import request
from werkzeug.security import generate_password_hash
from models.models import User, db
from contact import Logger
from dotenv import load_dotenv
import os

load_dotenv()

logger = Logger(token=os.getenv("APIKey"),
                chat_id=os.getenv("chatID"))  # TELEGRAM BOT


def send_message(name, email, subject, text):
    """
    Function that forwards to telegram when a message is received from the contact section.
    """
    message = f"New Message !!\n\
Name: {name}\nEmail: {email}\Subject:{subject}\Text:\n  {text}"

    logger.message(message=message)


