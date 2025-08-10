def calculate():
    print("Simple calculator")
    print("choose operation")
    print("1.add")
    print("2.subract")
    print("3.multiply")
    print("4.divide")

    choice = input("Enter expression (1,2,3,4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("num1: "))
        num2 = float(input("num2: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")

            else:
                print("Error: can't divide a number by zero")

    else:
        print("Invalid input")

calculate()