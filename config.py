import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
OWNER_NAME = os.getenv("OWNER_NAME")
CHANNEL = os.getenv("CHANNEL")
PHOTO_CH = os.getenv("PHOTO_CH")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicjepthon"))
call_py = PyTgCalls(bot)
