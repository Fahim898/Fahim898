def addition(value1,value2):
    return value1 + value2

def minus(value1,value2):
    return value1 - value2

def multiplication(value1,value2):
    return value1 * value2

def division(value1,value2):
    return value1 / value2


def chech_symbol(symbol,val1,val2):
    if symbol == "+":
        return addition(val1,val2)
    elif symbol == "-":
        return minus(val1,val2)
    elif symbol == "*":
        return multiplication(val1,val2)
    elif symbol == "/":
        return division(val1,val2)
    else:
        print("invalid symbol input")

def run_again_check():
    run_again = input("do you wan to execute it again(y/n): ")

    if run_again == 'y':
        take_user_input()
    else:
        print("code end")


def take_user_input():
    value1 = float(input("Please enter the first value: "))
    value2 = float(input("Please enter the second value: "))


    symbol = input("Please enter the symbol(+,-,*,/) to execute: ")

    result = chech_symbol(symbol,value1,value2)

    print("Result of your provided symbol '{}' is: {}".format(symbol,result))

    run_again_check()
    

if __name__ == "__main__":
    take_user_input()