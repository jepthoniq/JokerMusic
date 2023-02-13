import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("24325615"))
API_HASH = os.getenv("be5835a24d0cdaedc1cd256def4f9957")
SESSION = os.getenv("BACeYmUu25_FkJ0-PpF3bOROUuj2uOc-7PTbTGSUiQVXC14Li4Sf1hX1SkYLI0kz5tQ0Vl6LW24kueXRZRdiaiGb7Rrg2j7NoRcnbF0BzD3dE4j2SxB2EX8UIHu_Tq6EVARMCM1-mlMcK-iAVAupfBX5hhRbhDSd4N4FonwKI2Iu8fvLHKVOflQxzhCTBjpCLl8nnPpgr-OyO3c9_L6Uxn6WO4imI_QM8XStzq08Typ3m7qg4-M2NhTg9GzFitfRxqfADNNM0euvoHcfL8fs5GUbWG5NLLuqRCRnXq_Aan4S53r6YiHhahuz4ZgAc-sausAWfA5YDi1NCY4CNcJDce1WAAAAAUZPwtIA")
OWNER_NAME = os.getenv("c_l_h")
CHANNEL = os.getenv("Goto90")
PHOTO_CH = os.getenv("Goto90")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("c_l_h").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicjepthon"))
call_py = PyTgCalls(G7ht_bot)
