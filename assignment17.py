import os
import datetime

# student data Enter.
def enter_data():
    print("Enter student data list:-")
    with open("student_data.txt", "a") as file:
        while True:
            order_number = input("Enter the order number (0 to stop):- ")
            if order_number == '0':
                break
            name = input("Enter the name of the student:- ")
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %I:%M %p")
            entry = f"Order numbe:-{order_number} | Student name:-{name} |{formatted_time}|\n"
            file.write(entry)
            print(f"Data entered:- Order Number:- {order_number} | Name:- {name} | Time:- {formatted_time} |")


# Student display list.
def display_list():
    try:
        with open("student_data.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No data available. Please enter data first.")
            else:
                print("List of Students:")
                for line in lines:
                    data = line.strip().split()
                    order_number, name, datetime_info = data[0], data[1], (data[2:])
                    print(f"Order Number:- {order_number} | Name:- {name} | Time:- {datetime_info} |")
    except FileNotFoundError:
        print("No saved data found!!!")


# Check student order number.
def check_order_number():
    order_number = input("Enter the order number to check (0 to stop):- ")
    while order_number != '0':
        found = False
        try:
            with open("student_data.txt", "r") as file:
                for line in file:
                    data = line.strip().split()
                    if data[0] == order_number:
                        order_number, name, datetime_info = data[0], data[1], " ".join(data[2:])
                        print(f"The order number {order_number} corresponds to {name}, Time: {datetime_info}.")
                        found = True 
                        break
        except FileNotFoundError:
            print("No saved data found!!!")
        #If user not found data and add data.
        if not found:
            add_new = input("Do you want to add this order number and student name (y/n):- ")
            if add_new.lower() == 'y':
                name = input("Enter the name of the student:- ")
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %I:%M %p")
                entry = f"Order numbe:-{order_number} | Student name:-{name} |{formatted_time}|\n"
                with open("student_data.txt", "a") as file:
                    file.write(entry)
                print(f"Data added:- Order Number: {order_number} | Name:- {name} | Time: {formatted_time} |")
            else:
                print("Data not added!!!")
        order_number = input("Enter another order number to check (0 to stop):- ")


#If user delete TXT file.
def delete_file():
    if os.path.exists("student_data.txt"):
        os.remove("student_data.txt")
        print("Data file deleted.")
    else:
        print("No data file found to delete!!!")


#  Option for user.
while True:
    print("Options:")
    print("1. Enter Student Data")
    print("2. Display Student List")
    print("3. Check Order Number")
    print("4. Delete Data File")
    print("5. Exit")

    options = input("Enter your choice (|1|2|3|4|5|):- ")

    if options == '1':
        enter_data()
    elif options == '2':
        display_list()
    elif options == '3':
        check_order_number()
    elif options == '4':
        delete_file()
    elif options == '5':
        break
    else:
        print("Invalid choice! Please enter (1, 2, 3, 4, or 5).")


# Cord end.