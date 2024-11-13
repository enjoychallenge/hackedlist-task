from fastapi import FastAPI

from . import contacts

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

app = FastAPI()

@app.get("/phonebook/")
def search_contact(prefix: contacts.Name=''):
    phonebook = PhonebookSingleton({})
    return phonebook.search_contact(prefix)

@app.post("/phonebook/")
def add_contact(name: contacts.Name, phone: contacts.PhoneNumber):
    phonebook = PhonebookSingleton({})
    return phonebook.add_contact(name, phone)
