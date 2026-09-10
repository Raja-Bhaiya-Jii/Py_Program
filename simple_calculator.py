"""Program 2: Simple Calculator
Performs addition, subtraction, multiplication, and division."""
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op in ops:
        print(f"Result: {ops[op](a, b)}")
    else:
        print("Invalid operator")

if __name__ == "__main__":
    main()