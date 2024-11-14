from typing import TypeAlias

PhoneNumber: TypeAlias = str
Name: TypeAlias = str
Char: TypeAlias = str
BasePhonebook: TypeAlias = dict[PhoneNumber, Name]


class Phonebook:
    phone: PhoneNumber
    subtree: dict[Char, "Phonebook"]

    def __init__(self, initial_phonebook: BasePhonebook = None, file_path: str = None):
        assert initial_phonebook is None or file_path is None
        if initial_phonebook is None and file_path is None:
            initial_phonebook = {}
        if file_path:
            base_phonebook = {}
            with open(file_path, "r") as fd:
                for line in fd:
                    line = line.strip()
                    if line:
                        phone, name = line.split(":")
                        base_phonebook[phone.strip()] = name.strip()
        else:
            base_phonebook = initial_phonebook
        self.subtree = {}
        self.phone = None
        for phone_number, name in base_phonebook.items():
            self.add_contact(name, phone_number)

    @property
    def prefixed_phonebook(self) -> dict:
        result = {}
        if self.phone:
            result["phone"] = self.phone
        if self.subtree:
            result["subtree"] = {
                char: subtree.prefixed_phonebook
                for char, subtree in self.subtree.items()
            }
        return result

    def add_contact(self, name: Name, number: PhoneNumber) -> bool:
        name_clear = name.strip().lower()
        if name_clear:
            first_char, suffix = name_clear[:1], name_clear[1:]
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
        name_clear = name.strip().lower()
        if name_clear:
            first_char, suffix = name_clear[:1], name_clear[1:]
            if first_char in self.subtree:
                result = self.subtree[first_char].search_contact(suffix)
            else:
                result = []
        else:
            result = self.get_all_phones()
        return result
