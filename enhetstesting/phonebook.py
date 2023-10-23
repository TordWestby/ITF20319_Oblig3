class Phonebook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers.get(name)