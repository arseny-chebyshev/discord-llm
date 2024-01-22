import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


DISCORD_BOT_TOKEN: str = os.getenv("DISCORD_TOKEN")
BACKEND_SCHEMA = os.getenv('BACKEND_SCHEMA')
BACKEND_HOST = os.getenv('BACKEND_HOST')
BACKEND_PORT = os.getenv('BACKEND_PORT')
BACKEND_AI_ENDPOINT = os.getenv('BACKEND_AI_ENDPOINT')
BACKEND_URL = f"{BACKEND_SCHEMA}://" \
              f"{BACKEND_HOST}:" \
              f"{BACKEND_PORT}/" \
              f"{BACKEND_AI_ENDPOINT}"
