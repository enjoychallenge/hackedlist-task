from typing import TypeAlias

PhoneNumber: TypeAlias = str
Name: TypeAlias = str
Char: TypeAlias = str
BasePhonebook: TypeAlias = dict[PhoneNumber, Name]


class Phonebook:
    phone: PhoneNumber
    subtree: dict[Char, 'Phonebook']

    def __init__(self, initial_phonebook: BasePhonebook):
        self.subtree = {}
        self.phone = None
        for phone_number, name in initial_phonebook.items():
            self.add_contact(name, phone_number)

    @property
    def prefixed_phonebook(self) -> dict:
        result = {}
        if self.phone:
            result['phone'] = self.phone
        if self.subtree:
            result['subtree'] = {char: subtree.prefixed_phonebook for char, subtree in self.subtree.items()}
        return result

    def add_contact(self, name: Name, number: PhoneNumber) -> bool:
        if name:
            first_char, suffix = name[:1], name[1:]
            subtree = self.subtree.setdefault(first_char, Phonebook({}))
            result = subtree.add_contact(suffix, number)
        else:
            if self.phone is None:
                self.phone = number
                result = True
            else:
                result = False
        return result

    def get_all_phones(self) -> list[PhoneNumber]:
        phones = []
        if self.phone:
            phones.append(self.phone)
        for subtree in self.subtree.values():
            phones += subtree.get_all_phones()
        return phones

    def search_contact(self, name: Name) -> list[PhoneNumber]:
        if name:
            first_char, suffix = name[:1], name[1:]
            if first_char in self.subtree:
                result = self.subtree[first_char].search_contact(suffix)
            else:
                result = []
        else:
            result = self.get_all_phones()
        return result
