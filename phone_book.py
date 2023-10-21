#path = "C:\Users\84909\OneDrive\Desktop\CSC 110 Fall 2023\Projects\phone book\phone_book.txt"
def open_book():
    # this function transfer info in a text file storing numbers into a dictionary
    phone_book_dict = {}
    file = open('phone_book.txt')
    for line in file:
        if line.strip():
            line = line.strip("\n").split(",")
            name = line[0]
            number = line[1]
            phone_book_dict[name] = number
    #original_dict = phone_book_dict
    file.close()
    return phone_book_dict
    

def adding(phone_book_dict):
    # this function add new contact into the phone book
    name = input("Enter name: ")
    number = input("Enter number: ")
    phone_book_dict[name] = number
    return phone_book_dict

def searching(phone_book_dict):
    # this function search a contact in the phone book
    name_search = input("Enter name to search: ")
    if name_search in phone_book_dict:
        print("Number:", end = phone_book_dict[name_search])
    else: 
        print("Not found")

def display(phone_book_dict):
    # this function display every contact in the book
    for name in phone_book_dict:
        print(f"Name : {name} , number : {phone_book_dict[name]}")

def delete(phone_book_dict):
    # this function deletes a contact
    name_delete = input("Enter a name to delete: ")
    del phone_book_dict[name_delete]
    return phone_book_dict

def modify(phone_book_dict):
    # this function modifies a contact's number
    name = input("Enter the name to modify: ")
    new_number = input("Enter the new number: ")
    phone_book_dict[name] = new_number
    return phone_book_dict


def close_book(phone_book_dict):
    # this function store the contacts in the dictionary to a text file
    file = open('phone_book.txt', "wt")
    for name in phone_book_dict:
            file.write(name + "," + phone_book_dict[name] + "\n")
    file.close()


def main():
    # this function combines all functions to make an interactive program
    phone_book_dict = open_book()
    print('''1. Add new contact
2. Search a contact
3. Display all the contact
4. Delete a contact
5. Modify a contact
6. Quit''')
    choice = int(input("What is your choice: "))
    while choice < 6 and choice > 0:
        
        if choice == 1:
            adding(phone_book_dict)
        elif choice == 2:
            searching(phone_book_dict)
        elif choice == 3:
            display(phone_book_dict)
        elif choice == 4:
            delete(phone_book_dict)
        else:
            modify(phone_book_dict)
        print()
        choice = int(input("What is your choice: "))
    close_book(phone_book_dict)
main()