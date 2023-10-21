# class Through Calculator

class Calculator:
    def addition(self, value1, value2):
        return value1 + value2

    def subtraction(self, value1, value2):
        return value1 - value2

    def multiplication(self, value1, value2):
        return value1 * value2

    def division(self, value1, value2):
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
# Check symbol. 
    def check_symbol(self, symbol, val1, val2):
        if symbol == "+":
            return self.addition(val1, val2)
        elif symbol == "-":
            return self.subtraction(val1, val2)
        elif symbol == "*":
            return self.multiplication(val1, val2)
        elif symbol == "/":
            return self.division(val1, val2)
        else:
            return "Invalid symbol input"

    def run(self):
        while True:
            value1 = float(input("Please enter the first value: "))
            value2 = float(input("Please enter the second value: "))
            symbol = input("Please enter the symbol (+, -, *, /) to execute: ")
            result = self.check_symbol(symbol, value1, value2)
            print("Result of your provided symbol '{}' is: {}".format(symbol, result))
            run_again = input("Do you want to execute it again? (y/n): ")
            if run_again.lower() != 'y':
                print("Code end")
                break

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()

# cord End.