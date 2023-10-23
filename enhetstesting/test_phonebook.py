from phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Kjell", "12345678")
    assert phonebook.lookup("Kjell") == "12345678"

