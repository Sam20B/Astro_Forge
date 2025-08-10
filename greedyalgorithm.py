print("Change owed: ")
a=int(input())
cents = a 
quaters = int(cents / 25)
cents = cents - quaters * 25
dimes = int (cents / 10)
cents = cents - dimes * 10
nickels = int(cents / 5)
cents = cents - nickels * 5
pennies = int(cents / 1 )
cents = cents - cents * 1
print("quaters: ",quaters)
print("dimes: ",dimes)
print("nickels: ",nickels)
print("pennies: ",pennies)