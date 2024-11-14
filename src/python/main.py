import os
from fastapi import FastAPI
from pydantic import BaseModel
from . import contacts


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

DEFAULT_PHONEBOOK_PATH = os.path.join(DIR_PATH, "data/default_phonebook.txt")


PHONEBOOK = contacts.Phonebook(file_path=DEFAULT_PHONEBOOK_PATH)


class PhonebookItem(BaseModel):
    name: str
    phone: str


app = FastAPI()


@app.get("/phonebook/contacts")
def search_contact(prefix: contacts.Name = ""):
    return PHONEBOOK.search_contact(prefix)


@app.post("/phonebook/contacts")
def add_contact(phonebook_item: PhonebookItem):
    return PHONEBOOK.add_contact(phonebook_item.name, phonebook_item.phone)
