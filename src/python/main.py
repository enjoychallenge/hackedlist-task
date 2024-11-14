import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from . import contacts


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

DEFAULT_PHONEBOOK_PATH = os.path.join(DIR_PATH, "data/default_phonebook.txt")


PHONEBOOK = contacts.Phonebook(file_path=DEFAULT_PHONEBOOK_PATH)


class PhonebookItem(BaseModel):
    name: str
    phone: str


app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/phonebook/contacts")
def search_contact(prefix: contacts.Name = ""):
    return PHONEBOOK.search_contact(prefix)


@app.post("/phonebook/contacts")
def add_contact(phonebook_item: PhonebookItem):
    return PHONEBOOK.add_contact(phonebook_item.name, phonebook_item.phone)
