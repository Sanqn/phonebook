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
            raise NameError(f'Such a name exists')
        self.listphonebook[name] = number
        if not isinstance(number, int):
            raise TypeError('Number must be integer')

    @myphonebook.deleter
    def myphonebook(self):
       del self.listphonebook

    def __str__(self):
        list_book = ''
        for name, number in self.listphonebook.items():
            list_book += f'{name}: {number}\n'
        return list_book

person = PhoneBook()
person.myphonebook = 'Lisa', 125457
person.myphonebook = 'Lis', 125457
person.myphonebook = 'Don', 547825457
print(person)
print(person.myphonebook['Lisa'])
del person.myphonebook['Lisa']
print(person)