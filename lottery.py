print("Please enter your number:")
number = int(input())
for number in range (1, 1000):
    if number % 545 == 0:
        print("Congratulations user number: ",number)
        print("You are the WINNER!")
    else:
        print("Sorry user number ",number)
        print("You did not win this time...You can always try again later")
