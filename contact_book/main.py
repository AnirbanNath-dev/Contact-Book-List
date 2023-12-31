import json 
from tabulate import tabulate
import time as t

FILE_PATH = 'contacts_book.json'

class Contact_Book:

    def __init__(self , name):
        self.name = name
        self.loc = self.read_data(FILE_PATH)


    def change_data(self ,data ,  filepath):
        with open(filepath , 'w') as f:
            json.dump(data , f , indent=4)


    def read_data(self , filepath):
        try:
            with open(filepath , 'r') as f:
                data = json.load(f) 
                return data
        except:
            return {}


    def _add_contact(self):
        repeat = 0
        while True:
            contact_name = input('\nEnter the name of the contact : ')
            if self.name in self.loc:
                for i in range(len(self.loc[self.name])):
                    if contact_name == self.loc[self.name][i]['contact name']:
                        repeat = 1
                if repeat == 1:
                    print('Contact already exists . Type a different contact name')
                    repeat = 0
                    continue
                else:
                    contact_number = input('Enter the number of the contact : ')
                    data = {
                        'contact name' : contact_name,
                        'contact number' : contact_number
                    }

                    self.loc[self.name].append(data)
                    self.change_data(self.loc, FILE_PATH)
                    print('Contact has been saved !')
                    
                    break


            else: 
                contact_number = input('Enter the number of the contact : ')
                data = [{
                    'contact name' : contact_name,
                    'contact number' : contact_number
                }]

                self.loc[self.name] = data
                self.change_data(self.loc, FILE_PATH)
                print('Contact has been saved !')
                break


    def _del_contact(self):
        if self.name not in self.loc:
            print('\nYou dont have a any record in the contact book')
            t.sleep(1)
        else:
            name = input('\nEnter the name of the contact: ')
            no_repeat = 0
            index = 0
            for i in range(len(self.loc[self.name])):
                if name != self.loc[self.name][i]['contact name']:
                    no_repeat  = 1
                else:
                    no_repeat = 0
                    index = i
                    break
            
            if no_repeat == 1:
                print('Invalid contact name')
            else:
                print('Deleting.....')
                t.sleep(1)
                del self.loc[self.name][index]
                self.change_data(self.loc , FILE_PATH)
                print('Contact has been succesfully deleted')


        

    def _show_all_contacts(self):
        print('\nLoading....\n')
        t.sleep(2)
        if self.name not in self.loc:
            print('\nYou donot have any record in our contact book')
            t.sleep(1)
        else:
            headers = ['Contact name', 'Contact number']
            data = []

            for i in range(len(self.loc[self.name])):
                contact_name = self.loc[self.name][i]['contact name']
                contact_number = self.loc[self.name][i]['contact number']
                stored_data = [contact_name , contact_number]
                data.append(stored_data)

            table = tabulate(data , headers=headers , tablefmt='grid')
            print(table)
            t.sleep(2)
            
        

    def _show_a_contact(self):
        repeat = 0
        if self.name in self.loc:
            
            name = input('\nEnter the contact name: ')
            for i in range(len(self.loc[self.name])):
                if name in self.loc[self.name][i]['contact name']:
                    repeat = 1
                
            if repeat == 0:
                print('No such contact exist')
                t.sleep(1)
            else:
                contact_name = self.loc[self.name][i]['contact name']
                contact_num = self.loc[self.name][i]['contact number']
                print(f'Contact name : {contact_name}\nContact number : {contact_num}')
                t.sleep(2)
        else:
            print('\nYou have no valid record in data')
            t.sleep(1)


    
    def ask_for_opt(self):
        while True:
            opt = input('\nDo you want to :\n1.Add contact\n2.Delete contact\n3.Show all contacts\n4.Show a contact\n5.Exit\n:')

            if opt == '1':
                self._add_contact()
                continue
            elif opt == '2':
                self._del_contact()
                continue
            elif opt == '3':
                self._show_all_contacts()
                continue
            elif opt == '4':
                self._show_a_contact()
                continue
            elif opt == '5':
                print('Thanks for using!\n')
                break
            else:
                print('Invalid option')
                continue


    def screen(self):
        self.ask_for_opt()


def main():
    name = input('\nEnter you name: ')
    person = Contact_Book(name)
    person.screen()


if __name__ == '__main__':
    main()
