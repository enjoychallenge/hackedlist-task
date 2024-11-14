import pytest
from .contacts import Phonebook


@pytest.mark.parametrize(
    "base_phonebook, expected_phonebook",
    [
        (
            {"123456789": "a"},
            {
                "subtree": {"a": {"phone": "123456789"}},
            },
        ),
        (
            {"123456789": "a", "1": "b"},
            {
                "subtree": {"a": {"phone": "123456789"}, "b": {"phone": "1"}},
            },
        ),
        (
            {"123456789": "a", "1": "b", "2345": "ad"},
            {
                "subtree": {
                    "a": {"phone": "123456789", "subtree": {"d": {"phone": "2345"}}},
                    "b": {"phone": "1"},
                },
            },
        ),
    ],
)
def test_contacts_init(base_phonebook, expected_phonebook):
    phonebook = Phonebook(base_phonebook)
    assert phonebook.prefixed_phonebook == expected_phonebook


@pytest.mark.parametrize(
    "base_phonebook, name, number, expected_phonebook, expected_result",
    [
        (
            {"123456789": "a"},
            "b",
            "1",
            {
                "subtree": {"a": {"phone": "123456789"}, "b": {"phone": "1"}},
            },
            True,
        ),
        (
            {"123456789": "a"},
            "a",
            "123456789",
            {
                "subtree": {"a": {"phone": "123456789"}},
            },
            False,
        ),
        (
            {"123456789": "a"},
            "ad",
            "789",
            {
                "subtree": {
                    "a": {
                        "phone": "123456789",
                        "subtree": {"d": {"phone": "789"}},
                    }
                },
            },
            True,
        ),
    ],
)
def test_add_contact(base_phonebook, name, number, expected_phonebook, expected_result):
    phonebook = Phonebook(base_phonebook)
    result = phonebook.add_contact(name, number)
    assert result == expected_result
    assert phonebook.prefixed_phonebook == expected_phonebook


@pytest.mark.parametrize(
    "base_phonebook, name_prefix, expected_phones",
    [
        (
            {"123456789": "a", "1": "b", "2345": "ad"},
            "a",
            ["123456789", "2345"],
        ),
        (
            {"123456789": "a", "1": "b", "2345": "ad"},
            "x",
            [],
        ),
        (
            {"123456789": "a", "1": "b", "2345": "ad"},
            "ad",
            ["2345"],
        ),
    ],
)
def test_search_contact(base_phonebook, name_prefix, expected_phones):
    phonebook = Phonebook(base_phonebook)
    assert phonebook.search_contact(name_prefix) == expected_phones
