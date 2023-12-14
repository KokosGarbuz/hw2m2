from abc import ABC, abstractmethod
from AddressBook import *



from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_commands(self, commands):
        pass

    @abstractmethod
    def get_user_input(self):
        pass


class ConsoleInterface(UserInterface):

    def show_message(self, message):
        print(message)

    def show_commands(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))

    def get_user_input(self):
        return input().strip().lower()

class Bot:
    def __init__(self, user_interface):
        self.book = AddressBook()
        self.ui = user_interface

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            self.ui.display_info(self.book.congratulate())
        elif action == 'view':
            self.ui.display_info(str(self.book))
        elif action == 'exit':
            pass
        else:
            self.ui.display_info("There is no such command!")