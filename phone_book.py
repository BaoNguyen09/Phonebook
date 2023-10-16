def open_book():
    dict_data = {}
    file = open("phone_book.txt")
    for line in file:
        line = line.strip("\n")
        line=line.split(",")
        key = line[0]
        value = line[1]
        dict_data[key] = value
    original_dict = dict_data
    file.close()
    return dict_data
    

def adding(dict_data):
    name = input("Enter name: ")
    number = input("Enter number: ")
    dict_data[name] = number
    return dict_data

def searching(dict_data):
    name_search = input("Enter name to search: ")
    for key in dict_data:
        if key == name_search:
            print("Number:", end = " ")
            return dict_data[key]
    return "Not found"

def display(dict_data):
    for key in dict_data:
        print(f"Name : {key} , number : {dict_data[key]}")

def delete(dict_data):
    name_delete = input("Enter a name to delete: ")
    del dict_data[name_delete]
    return dict_data

def modify(dict_data):
    name = input("Enter the name to modify: ")
    new_number = input("Enter the new number: ")
    dict_data[name] = new_number
    return dict_data

def close_book(dict_data):
    file = open("phone_book.txt", "wt")
    for key in dict_data:
            file.write(key + "," + dict_data[key] + "\n")
    file.close()
def main():
    dict_data = open_book()
    print('''1. Add new contact
2. Search a contact
3. Display all the contact
4. Delete a contact
5. Modify a contact
6. Quit''')
    choice = int(input("What is your choice: "))
    while choice < 6 and choice > 0:
        
        if choice == 1:
            adding(dict_data)
        elif choice == 2:
            searching(dict_data)
        elif choice == 3:
            display(dict_data)
        elif choice == 4:
            delete(dict_data)
        else:
            modify(dict_data)
        print()
        choice = int(input("What is your choice: "))
    close_book(dict_data)
main()