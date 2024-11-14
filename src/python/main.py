from fastapi import FastAPI
from . import contacts
import os


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

DEFAULT_PHONEBOOK_PATH = os.path.join(DIR_PATH, "data/default_phonebook.txt")


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class PhonebookSingleton(contacts.Phonebook):
    pass


PHONEBOOK = PhonebookSingleton(file_path=DEFAULT_PHONEBOOK_PATH)


app = FastAPI()


@app.get("/phonebook/")
def search_contact(prefix: contacts.Name = ""):
    return PHONEBOOK.search_contact(prefix)


@app.post("/phonebook/")
def add_contact(name: contacts.Name, phone: contacts.PhoneNumber):
    return PHONEBOOK.add_contact(name, phone)
