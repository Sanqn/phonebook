import pandas as pd

# class PhoneBook:
#
#     def __init__(self):
#         self.listphonebook = {}
#
#     def getlistbook(self, name):
#         return self.listphonebook[name]
#
#     def addlistbook(self, name, value):
#         self.listphonebook[name] = value
#
#     def updatelistbook(self, name, value):
#         self.listphonebook[name] = value
#
#     def delitelistbook(self, name):
#         self.listphonebook.pop(name)
#
#     def __str__(self):
#         more_spis = ''
#         for name, value in self.listphonebook.items():
#             more_spis += f'{name},{value}\n'
#         return more_spis
#
# new_person = PhoneBook()
# new_person.addlistbook('Lisa', 375296581244)
# new_person.addlistbook('Don', 3752964525444)
# print(new_person)
# new_person.updatelistbook('Lisa', +375292045578)
# new_person.delitelistbook('Lisa')
# print(new_person)
# print(new_person.getlistbook('Don'))


class PhoneBook:

    def __init__(self):
        self.listphonebook = {}

    @property
    def myphonebook(self):
        return self.listphonebook

    @myphonebook.setter
    def myphonebook(self, arg):
        name, number = arg
        if name in self.listphonebook:
            raise NameError(f'Name {name} exists')
        self.listphonebook[name] = number
        if not isinstance(number, int):
            raise TypeError('Number must be integer')

    @myphonebook.deleter
    def myphonebook(self):
       del self.listphonebook

    def get_table(self):
        list_book = {}
        for name, number in self.listphonebook.items():
            list_book['Name'] = list_book.get('Name', []) + [name]
            list_book['Number'] = list_book.get('Number', []) + [number]
        list = pd.DataFrame(list_book)
        return list

    def save_note(self):
        table = ''
        for name, number in self.listphonebook.items():
            table += f'{name}: {number}\n'
        file = open('phonebook.txt').read()
        for i in table.split(': '):
            if i in file:
                continue
            file = open('phonebook.txt', 'a+', encoding='utf-8')
            file.write(i + ' ')

        return table

    def __str__(self):
        table = ''
        for name, number in self.listphonebook.items():
            table += f'{name} - +{number}\n'
        return table


person = PhoneBook()
person.myphonebook = 'Lisa', 125457
person.myphonebook = 'Lis', 125457
person.myphonebook = 'Don', 547825457
person.myphonebook = 'Dak', 451575515
print(person.save_note())
person.myphonebook = 'Dracula', 75515
print(person.save_note())






