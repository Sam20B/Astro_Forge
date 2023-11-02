#Dictionary containing list of car models
make = {
    'BMW':'available',
    'Mercedes benz':'available',
    'Toyota':'available',
    'Mitsubishi':'available',
    'Mazda':'out of stock',
    'Volks Wagon':'out of stock',
    'Lexus':'available',
    'Nissan':'available',
    'Audi':'available'
}
print("Hello and welcome to Samz motors")
print("What make are you intrested in? ")
car_list = ['BMW','Mercedes benz','Toyota','Mitsubishi','Mazda','Volks Wagon','Lexus','Nissan','Audi','']
for item in car_list:
    print(item)
#prompts the user to input the model they want to view
x = str(input())
if x in make:
    #if the model is out of stock the code ends here
    if make[x] == 'out of stock':
        print("My apologies...it seems " + x + " is out of stock")
        print("You can have a look at other makes or come back later")
        #if the model is in stock the user is prompted to input the color of their intrest
    if make[x] == 'available':
        print("What color do you prefer? ")
        color = ['black','white','silver','red','blue','violet','maroon','']
        for item in color:
            print(item)
        y = str(input())
#list containing the colors the model is available in
BMW = ['black','white','blue','violet','silver']
if x == 'BMW':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in BMW:
        if y == 'black':
            print("The " + x +" cars available in black are: ")
            black_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X5','BMW X7']
            for item in black_bmw_list:
                print(item)
        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X6','BMW 8 series','BMW X 7']
            for item in white_bmw_list:
                print(item)
        if y == 'blue':
            print("The " + x + " cars available in blue are: ")
            blue_bmw_list = ['BMW 3 series','BMW 7 series','BMW 8 series','BMW X 7']
            for item in blue_bmw_list:
                print(item)
        if y == 'violet':
            print("The " + x + "cars available in violet are: ")
            violet_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X6','BMW 8 series','BMW X 7']
            for item in violet_bmw_list:
                print(item)
        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_bmw_list = ['BMW 3 series','BMW X2','BMW X6','BMW 8 series','BMW X 7']
            for item in silver_bmw_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in BMW:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Mercedes_benz = ['black','white','silver','blue','red']
if x == 'Mercedes benz':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Mercedes_benz:
        if y == 'black':
            print("The " + x +" cars available in black are: ")
            black_benz_list = ['Mercedes-Benz A-class','Mercedes-Benz S-class','Mercedes-Benz B-class','Mercedes-Benz SL','Mercedes-Benz GLS','Mercedes-Benz G-class','Mercedes-Benz GT63','Mercedes-Benz Infinity']
            for item in black_benz_list:
                print(item)
        if y == 'white':
            print("The " + x +" cars available in white are: ")
            white_benz_list = ['Mercedes-Benz S-class','Mercedes-Benz G-class','Mercedes-Benz GLE','Mercedes-Benz GLA','Mercedes-Benz GLS']
            for item in white_benz_list:
                print(item)
        if y == 'silver':
            print("The " + x +" cars available in silver are: ")
            silver_benz_list = ['Mercedes-Benz C-class','Mercedes-Benz G-class','Mercedes-Benz CLS','Mercedes-Benz GT']
            for item in silver_benz_list:
                print(item)
        if y == 'blue':
            print("The " + x +" cars available in blue are: ")
            blue_benz_list = ['Mercedes-Benz G-class','Mercedes-Benz C-class','Mercedes-Benz GT']
            for item in blue_benz_list:
                print(item)
        if y == 'red':
            print("The " + x +" cars available in red are: ")
            red_benz_list = ['Mercedes-Benz G-class','Mercedes-Benz C-class','Mercedes-Benz GT','Mercedes-Benz SLC','Mercedes-Benz B-class']
            for item in red_benz_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Mercedes_benz:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Toyota = ['black','white','silver','blue']
if x == 'Toyota':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Toyota:
        if y == 'black':
            print("The " + x + " cars available in black are: ")
            black_toyota_list = ['Toyota Sienna','Toyota Tacoma','Toyota Land Cruiser','Toyota Supra','Toyota 4Runner','Toyota Supra','Toyota Corolla']
            for item in black_toyota_list:
                print(item)
        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_toyota_list = ['Toyota Land Cruiser','Toyota Corolla','Toyota Supra','Toyota Tundra','Toyota C-HR','Toyota Sequoia']
            for item in white_toyota_list:
                print(item)
        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_toyota_list = ['Toyota Supra','Toyota Corolla','Toyota Sienna','Toyota 4Runner','Toyota Land Cruiser']
            for item in silver_toyota_list:
                print(item)
        if y == 'blue':
            print("The " + x + " cars available in blue are: ")
            blue_toyota_list = ['Toyota Land Cruiser','Toyota Corolla','Toyota Sienna','Toyota Supra','Toyota GT Supra']
            for item in blue_toyota_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Toyota:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Mitsubishi = ['black','white','silver']
if x == 'Mitsubishi':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Mitsubishi:
        if y == 'black':
            print("The " + x + " cars available in black are: ")
            black_mitsubishi_list = ['Mitsubishi Outlander','Mitsubishi Lancer','Mitsubishi Outlander Sport']
            for item in black_mitsubishi_list:
                print(item)
        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_mitsubishi_list = ['Mitsubishi Outlander','Mitsubishi Lancer']
            for item in white_mitsubishi_list:
                print(item)
        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_mitsubishi_list = ['Mitsubishi Outlander','Mitsubishi Eclipse Cross']
            for item in silver_mitsubishi_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Mitsubishi:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Lexus = ['black','white']
if x == 'Lexus':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Lexus:
        if y == 'black':
            print("The " + x + " cars available in black are: ")
            black_lexus_list = ['Lexus UN','Lexus GX','Lexus LC','Lexus UX','Lexus IS','Lexus ES','Lexus RC','Lexus LX']
            for item in black_lexus_list:
                print(item)
        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_lexus_list = ['Lexus GX','Lexus NX','Lexus UX','Lexus RC','Lexus GS','Lexus LS','Lexus ES']
            for item in white_lexus_list:
                print(list)
     #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Lexus:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Nissan = ['black','white']
if x == 'Nissan':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Nissan:
        if y == 'black':
            print("The " + x + " cars available in black are: ")
            black_nissan_list = ['Nissan altima','Nissan pathfinder','Nissan GT-R']
            for item in black_nissan_list:
                print(item)
        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_nissan_list = ['Nissan sentra','Nissan versa','Nissan Pathfinder','Nissan armada','Nissan rogue','Nissan Maxima']
            for item in white_nissan_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Nissan:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
#list containing the colors the model is available in
Audi = ['black','blue','maroon']
if x == 'Audi':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Audi:
        if y == 'black':
            print("The " + x + " cars available in black are: ")
            black_audi_list = ['Audi A3','Audi A4','Audi A5','Audi A6','Audi A7','Audi A7','Audi Q2','Audi Q3']
            for item in black_audi_list:
                print(item)
        if y == 'blue':
            print("The " + x + " cars availablein blue are: ")
            blue_audi_list = ['Audi A3','Audi A4','Audi A5','Audi A7','Audi A7','Audi Q2','Audi Q3']
            for item in blue_audi_list:
                print(item)
        if y == 'maroon':
            print("The " + x + " cars available in maroon are: ")
            maroon_audi_list = ['Audi A5','Audi A7','Audi A7','Audi Q2','Audi Q3']
            for item in maroon_audi_list:
                print(item)
    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Audi:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")
