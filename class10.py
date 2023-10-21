import re

# Define a dictionary to map SIM operator prefixes to operator name
sim_operators = {
    "017": "Grameenphone",
    "018": "Robi",
    "019": "Banglalink",
    "015": "Teletalk",
    "013": "Grameenphone",
    "014": "Banglalink",
    "016": "Airtel"
}

# Regular expression to validate 11-digit numbers in Bangladesh
number_pattern = re.compile(r'^01[3-9]\d{8}$')

try:
    num_of_numbers = int(input("How many 11-digit numbers do you want to input? "))
    
    if num_of_numbers <= 0:
        print("Error: Please enter a valid positive number.")
    else:
        numbers = set()  # Use a set to store unique numbers

        for i in range(num_of_numbers):
            while True:
                number = input(f"Enter {i + 1}: ")
                if number_pattern.match(number):
                    if number in numbers:
                        print(f"{number} is a duplicate entry.")
                    else:
                        numbers.add(number)
                        prefix = number[:3]
                        if prefix in sim_operators:
                            sim_operator = sim_operators[prefix]
                            print(f"{number} is valid in Bangladesh and belongs to {sim_operator}.")
                        else:
                            print(f"{number} is valid in Bangladesh but the SIM operator is unknown.")
                    break
                else:
                    print("Error: Please enter a valid 11-digit number.")

except ValueError:
    print("Error: Please enter a valid number for the quantity of numbers.")
