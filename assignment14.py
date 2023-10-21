
import assignment12
print (assignment12)

def take_user_input():
    value1 = float(input("Please enter the first value: "))
    value2 = float(input("Please enter the second value: "))


    symbol = input("Please enter the symbol(+,-,*,/) to execute: ")

    result = assignment12.chech_symbol(symbol,value1,value2)

    print("Result of your provided symbol '{}' is: {}".format(symbol,result))

    assignment12.run_again_check()
    

if __name__ == "__main__":
    take_user_input()

