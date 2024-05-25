data = {628123456789 : {'Name':'Stefanus', 'Address': 'Malang', 'E-mail': 'stefanus@gmail.com'},
        628123456788 : {'Name': 'Petra', 'Address': 'Bekasi', 'E-mail': 'petra@gmail.com'},
        628123456787 : {'Name': 'Oka', 'Address': 'Denpasar' , 'E-mail': 'oka@gmail.com'},
        628123456786 : {'Name': 'Riski', 'Address': 'Semarang' , 'E-mail': 'riski@gmail.com'},
        628123456785 : {'Name': 'Syaiful', 'Address': 'Mataram' , 'E-mail': 'syaiful@gmail.com'},
        628123456784 : {'Name': 'Irfan', 'Address': 'Madiun', 'E-mail': 'irfan@gmail.com'},
        628123456783 : {'Name': 'Haris', 'Address': 'Balikpapan', 'E-mail': 'haris@gmail.com'},
        628123456782 : {'Name': 'Abdul', 'Address': 'Yogyakarta', 'E-mail': 'abdul@gmail.com'}}

def menu():
    print('\nCAPSTONE PROGRAM MENU - YELLOW PAGES')
    print('Press A to enter Read Menu')
    print('Press B to enter Create Menu')
    print('Press C to enter Update Menu')
    print('Press D to enter Delete Menu')
    print('Press E to enter End Program')

def read() :
    print('\nREAD MENU')
    read_menu = input('Do you want to display Yellow Pages data (yes/no)? ').lower()
    if read_menu == 'yes' :
        input_read_menu = input('Do you want to all display Yellow Pages data (yes/no)? ').lower()

        if input_read_menu == 'yes' :
            print('\nDisplaying all data')
            for key, value in data.items() :
                    print(f'{key}: {value}')
        elif input_read_menu == 'no' :
            pass
        else :
            print('\n"Data does not exist"')
            pass

        if input_read_menu == 'no' :
            check_data = input('Do you want to check a Yellow Pages data (yes/no)? ').lower()
            if check_data == 'yes' :
                print('\nChecking Yellow Pages data using phone number format 62xxx')
                try :
                    input_check_data = int(input('Input phone number you want to check: '))
                    if input_check_data in data :
                        print(f'\nNumber: {input_check_data}')
                        for key, value in data[input_check_data].items() :
                            print(f'{key}: {value}')
                    elif input_check_data not in data :
                        print('\n"Data does not exist"')
                except ValueError :
                    print('\n"Wrong input, please input numbers"')
                    pass

                try :
                    check_another_data = int(input('\nInput another phone number you want to check: '))
                    if check_another_data in data :
                        print(f'\nNumber: {check_another_data}')
                        for key, value in data[check_another_data].items() :
                            print(f'{key}: {value}')
                    elif check_another_data not in data :
                        print('\n"Data does not exist"')
                except ValueError :
                    print('\n"Wrong input, please input numbers"')
                    pass

    if read_menu == 'no' :
        read_menu_no = input('Are you finished and return to main menu (yes/no)? ').lower()
        if read_menu_no == 'no' :
            pass
        elif read_menu_no == 'yes' :
            back_to_menu()

def create():
    print('\nCREATE MENU')    
    create_menu = input('Do you want to add data to current Yellow Pages (yes/no)? ').lower()
    if create_menu == 'yes' :
        import math
        while True :
            try :
                print('\nPlease input your phone number format 62xxx')
                add_data = int(input('Input your phone: '))
                digit_add_data = int(math.log10(add_data)) + 1
                if add_data in data :
                    print('\n"Data already exists"')
                    continue
                elif digit_add_data < 10 :
                    print('\n"Wrong phone number, must be between 10 - 12 digits"')
                    continue
                elif digit_add_data > 13 :
                    print('"\nPhone number digits too long"')
                    continue
            except ValueError :
                print('\n"Wrong input, please input correct number"')
            else  :
                break
                
        while True :
            if add_data not in data :
                print('\nThis is not a duplicate data, please input following informations')
                data[add_data] = {}
                data[add_data]['Name'] = input('Input your name: ').capitalize()
                data[add_data]['Address'] = input('Input your address: ').capitalize()
                data[add_data]['E-mail'] = input('Input your e-mail: ').lower()

                print(f'\nAdding data to Yellow Pages\nNumber: {add_data}')
                for key, value in data[add_data].items() :
                    print(f'{key}: {value}')

                save_data = input('\nDo you want to save this dat to Yellow Pages (yes/no)? ').lower()
                if save_data == 'yes' :
                    print('\n"Data successfully saved"')
                    break
                elif save_data == 'no' :
                    print('\n"Canceling, data not saved"')
                    break
                else :
                    print('\n"Choose correct option"')
                    break

    elif create_menu == 'no' :
        create_menu_no = input('Are you finished and return to main menu (yes/no)? ').lower()
        if create_menu_no == 'yes' :
            back_to_menu()
        elif create_menu_no == 'no' :
            pass
        else :
            print('\n"Choose correct option"')
    else :
        print('\n"Choose correct option"')
        pass

def update():
    print('\nUPDATE MENU')
    update_menu = input('Do you want to update Yellow Pages data? ').lower()
    if update_menu == 'yes' :
        while True :
            try :
                print('\nPlease input your phone number format 62xxx')
                update_data = int(input('Input phone number you want to update: '))
                if update_data not in data :
                    print('\n"Data not exists"')
                    continue
            except ValueError :
                print('\n"Wrong input, please input correct number"')
            else :
                break

        if update_data in data :
            print(f'\nYellow pages data\nPhone: {update_data}')
            for key, value in data[update_data].items() :
                print(f'{key}: {value}')
            update_menu_data_continue = input('\nDo you want to update this phone number (yes/no)? ').lower()

            if update_menu_data_continue == 'yes' :
                import math
                print('\nPlease provide your new information below')
                
                while True :
                    try :
                        update_data_phone = int(input('Input new phone number: '))
                        update_data_phone_digit = int(math.log10(update_data_phone)) + 1
                        if update_data_phone_digit < 10 :
                            print('\n"Wrong phone number, must be between 10 - 12 digits"\n')
                            continue
                        elif update_data_phone_digit > 13 :
                            print('"\nPhone number digits too long"\n')
                            continue
                    except ValueError :
                        print('\n"Wrong input, please input correct number"\n')
                    else  :
                        break
                
                update_data_name = input('Input new name: ').capitalize()
                update_data_address = input('Input new address: ').capitalize()
                update_data_email = input('Input new email address: ').lower()
                update_data_confirm = input(f'\nDo you want to update all data containing {update_data} - {data[update_data]['Name']} (yes/no)? ')

                if update_data_confirm == 'yes' :
                    data[update_data_phone] = data[update_data]
                    del data[update_data]
                    if len(update_data_name) >= 2 :
                        data[update_data_phone]['Name'] = update_data_name
                    if len(update_data_address) >= 3 :
                        data[update_data_phone]['Address'] = update_data_address
                    if len(update_data_email) > 7 and '@' in update_data_email:
                        data[update_data_phone]['E-mail'] = update_data_email
                    
                    print(f'\nNew Yellow pages data\nPhone: {update_data_phone}')
                    for key, value in data[update_data_phone].items() :
                        print(f'{key}: {value}')
                    print('\n"Data successfully updated"')
                    pass
                    
                print('\nYellow Pages update data log:')
                if update_data_phone_digit < 10 > 13 :
                    print('"Phone number not updated, user choose not to update the data"')
                if len(update_data_name) < 2 :
                    print('"Name not updated, user choose not to update the data"')
                if len(update_data_address) < 3 :
                    print('"Address not updated, user choose not to update the data"')
                if len(update_data_email) < 7 and '@' not in update_data_email :
                    print('"E-mails not updated, user choose not to update the data"')

                else :
                    pass
            else :
                pass
        else :
            print('\n"The data you are looking for does not exist"')
            pass
    if update_menu == 'no' :
        update_menu_no = input('Are you finished and return to main menu (yes/no)? ').lower()
        if update_menu_no == 'no':
            pass
        elif update_menu_no == 'yes':
            back_to_menu()
        else :
            print('\n"Choose correct option"')

def delete() :
    print('\nDELETE MENU')
    delete_menu = input('Do you want to delete a Yellow Pages data (yes/no)? ').lower()
    if delete_menu == 'yes' :
        while True :
            try :
                import math
                input_delete = int(input('Input phone number you want to delete format 62xxx: '))
                input_delete_digit = int(math.log10(input_delete)) + 1
                if input_delete in data :
                    break
                elif input_delete not in data or input_delete_digit < 10 > 13 :
                    print('\n"The data you are looking for does not exist"\n')
                    continue
            except ValueError :
                print('\n"Wrong input, please input correct number"\n')
            else :
                break

        print(f'\nYellow Pages data\nPhone: {input_delete}')
        for key, value in data[input_delete].items() :
            print(f'{key}: {value}')
            
        while True :
            delete_menu_confirm = input(f'\nAre you sure you want to delete {input_delete} - {data[input_delete]['Name']} from Yellow Pages data (yes/no)? ').lower()
            if delete_menu_confirm == 'yes' :
                del data [input_delete]
                print('\n"Data successfully deleted"')
                break
            elif delete_menu_confirm == 'no' :
                break
            else :
                break

    elif delete_menu == 'no' :
        delete_data_no = input('Are you finished and return to main menu (yes/no)? ').lower()
        if delete_data_no == 'no' :
            pass
        elif delete_data_no == 'yes' :
            back_to_menu()
    else :
        print('\n"Choose correct options"')
        pass

menu()
option = input('\nEnter your option: ').upper()

def back_to_menu() :
    menu()
    option = input('\nEnter your option: ').upper()

while option != '' and len(option) > 0 :
    if option == 'A' :
        read()
    elif option == 'B' :
        create()
    elif option == 'C' :
        update()
    elif option == 'D' :
        delete()
    elif option == 'E' :
        print('\nEND PROGRAM')
    else :
        print('\n"The option you entered is not valid"')
        back_to_menu()
