student_data = {}


# student data Enter
def enter_data():
    print("Enter student data list:")
    while True:
        order_number = input("Enter the order number (0 to stop): ")
        if order_number == '0':
            break
        name = input("Enter the name of the student: ")
        student_data[order_number] = name
        print(f"Data entered: Order Number: {order_number}, Name: {name}")


# Student display list
def display_list():
    print("List of Students:")
    for order_number, name in student_data.items():
        print(f"Order Number: {order_number}, Name: {name}")


# Check student order number
def check_order_number():
    order_number = input("Enter the order number to check (0 to stop): ")
    while order_number != '0':
        if order_number in student_data:
            print(f"The order number {order_number} corresponds to {student_data[order_number]}.")
        else:
            print(f"No data found for order number {order_number}.")
            add_new = input("Do you want to add this order number and student name (y/n): ")
            if add_new.lower() == 'y':
                name = input("Enter the name of the student: ")
                student_data[order_number] = name
                print(f"Data added: Order Number: {order_number}, Name: {name}")
            else:
                print("Not added.")
        order_number = input("Enter another order number to check (0 to stop): ")


#  Option for user
while True:
    print("Options:")
    print("1. Enter Student Data")
    print("2. Display Student List")
    print("3. Check Order Number")
    print("4. Exit")
    
    Option = input("Enter your choice (|1|2|3|4|): ")
    
    if Option == '1':
        enter_data()
    elif Option == '2':
        display_list()
    elif Option == '3':
        check_order_number()
    elif Option == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.") 

# Cord end