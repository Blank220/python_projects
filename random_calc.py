import random

num1 = random.randint(1,1000)
num2 = random.randint(1,1000)


def calculate():
    try:
        operator = input("Select Operator: ('+','-','*','/'): ")

        if operator == "+":
            return f'Sum is {num1 + num2}'
        
        elif operator == "-":
            return f'Difference is {num1 - num2}'
        
        elif operator == "*":
            return f'Product is {num1 * num2}'
        
        elif operator == "/":
            return f'Quotient is {num1 / num2}'
    
    except:
        print('Invalid')
    
def main():
    print(f"The first number is {num1}")
    print(f"The second number is {num2}")

    answer = calculate()
    print(answer)

if __name__ == "__main__":
    main()

