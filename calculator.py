import sys
def askforinput():
    try:
        n1 = int(input("Enter your first number (or a letter to exit): "))
    except ValueError:
        sys.exit()
    op = input("Enter your operation: ")
    try:
        n2 = int(input("Enter your second number: "))
    except ValueError:
        sys.exit()
    def calculation():
        nonlocal op
        if op == '+':
            print(f"{n1} + {n2} = {n1 + n2}")
            askforinput()
        elif op == '-':
            print(f"{n1} - {n2} = {n1 - n2}")
            askforinput()
        elif op == '*':
            print(f"{n1} * {n2} = {n1 * n2}")
            askforinput()
        elif op == '/':
            print(f"{n1} / {n2} = {n1 / n2}")
            askforinput()
        else:
            print("Not a valid operator.")
            askforinput()
    calculation()
askforinput()