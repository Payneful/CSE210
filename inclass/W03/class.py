import os

class Person:
    def __init__(self, full_name = "", address = "", age = 0):
        self.full_name = full_name
        self.address = address
        self.age = age
        
    def print_info(self):
        print(f"Name: {self.full_name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}\n")


def clear_screen():
    '''Clears terminal for easier viewing'''
    os.system('cls' if os.name=='nt' else 'clear')

def create_person():
    name = input("Full name: ")
    address = input("Address: ")
    age = int(input("Age: "))
    name = Person(name, address, age)
    return name

names = []
choice = "y"

while choice == "y":
    names.append(create_person())
    choice = input("Would you like to add another name? (y/n) ").lower()
    clear_screen()

for name in names:
    name.print_info()