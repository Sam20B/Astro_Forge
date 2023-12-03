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
    'Audi':'available',
    'Honda':'available',
    'Hyundai':'out of stock',
    'Subaru':'available',
    'Chevrolet':'available'
}
print("Hello and welcome to Samz motors")
print("What make are you intrested in? ")
car_list = ['BMW','Mercedes benz','Toyota','Mitsubishi','Mazda','Volks Wagon','Lexus','Nissan','Audi','Honda','Hyundai','Subaru','Chevrolet','']
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
            print("The " + x +" cars available in black are:")
            black_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X5','BMW X7','']
            for item in black_bmw_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_bmw_3_series = ['','color : black','year : 2021','petrol engine : 3.0-liter twinpower turbo inline-4','Diesel engines : 2.0-liter twinpower turbo inline-4','Power output : 180 - 400+ horsepower','Transmission : 6-speed automatic transmission','Drive type : RWD','Brakes : dynamic brake control','Wheels : Alloy','Interior : Apple CarPlay and android compatibility,','           bluetooth connectivity','           Navigation system','Safety : multiple airbags','Exterior : LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency','Optional : Panoramic sunroof','           upgraded sound system','           Driver assistance packages','           Ambient lighting','           Rear-seat entertainment system','']
            black_bmw_7_series = ['','color : black','year : 2019','Engine : 4.4-liter TwinPower Turbo V8(750i)','Power Output : 320 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive type : RWD','Suspension : Front and rear independent suspension','Brake : Anti-lock braking system','Wheels : Alloy','Interior : BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Advanced driver assistance features','Saftey : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and surround-view camera system','Exterior : Iconic BMW kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency and performance','Optional : Bowers & Wilkins diamond surround sound system','           Panoramic sky lounge LED roof','           Driving assistance proffesional package','']
            black_bmw_x2 = ['','color : black','year : 2021','Engine : 2.0-litre Twinpower turbo inline-4','Power output : 192 - 302 horsepower','Transmission : 7 or 8-speed automatic transmission','Drive type : Front-wheel drive','Suspension : Front and rear independent suspension','Brakes : Dynamic brake control','Wheels : Alloy','Interior : Premium materials, including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and rear view camera','Exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Sporty and compact SUV design','Optional : Panomaric sunroof','           Upgraded sound sysytem','           Driver assistance packages with additional safety features','           M sport X package for enhanced performance and styling','']
            black_bmw_x5 = ['','color : black','year : 2018','Engine : 3.0-litre Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Anti-lock braking system(ABS)','Wheels : Alloy','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibilty','           Bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emrgency braking','         Parking sensors and rear view camera','Exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Driver assistance packages with additional safety features','           Third-row seating','']
            black_bmw_x7 = ['','color : black','year : 2018','Engine : 4.4-liter Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Brake assist','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Blue tooth connectivity','           Navigation sysytem','Safety : Multiple airbags(front,side,curtain)','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision with automatic emergency braking','         Parking sensors and rear view camera','exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Rear-seat entertainment system','           Driver assistance packages with additional safety features','           Luxury and M sport packages for enhanced performance and styling','']
            if z == 'BMW 3 series':
                for item in black_bmw_3_series:
                    print(item)
            if z == 'BMW 7 series':
                for item in black_bmw_7_series:
                    print(item)
            if z == 'BMW X2':
                for item in black_bmw_x2:
                    print(item)
            if z == 'BMW X5':
                for item in black_bmw_x5:
                    print(item)
            if z == 'BMW X7':
                for item in black_bmw_x7:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X6','BMW 8 series','BMW X7','']
            for item in white_bmw_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_bmw_3_series = ['','color : white','year : 2021','petrol engine : 3.0-liter twinpower turbo inline-4','Diesel engine : 2.0-liter twinpower turbo inline-4','Power output : 180 - 400+ horsepower','Transmission : 6-speed automatic transmission','Drive type : RWD','Brakes : dynamic brake control','Wheels : Alloy','Interior : Apple CarPlay and android compatibility,','           bluetooth connectivity','           Navigation system','Safety : multiple airbags','Exterior : LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency','Optional : Panoramic sunroof','           upgraded sound system','           Driver assistance packages','           Ambient lighting','           Rear-seat entertainment system','']
            white_bmw_7_series = ['','color : white','year : 2019','Engine : 4.4-liter TwinPower Turbo V8(750i)','Power Output : 320 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive type : RWD','Suspension : Front and rear independent suspension','Brake : Anti-lock braking system','Wheels : Alloy','Interior : BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Advanced driver assistance features','Saftey : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and surround-view camera system','Exterior : Iconic BMW kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency and performance','Optional : Bowers & Wilkins diamond surround sound system','           Panoramic sky lounge LED roof','           Driving assistance proffesional package','']
            white_bmw_x2 = ['','color : white','year : 2021','Engine : 2.0-litre Twinpower turbo inline-4','Power output : 192 - 302 horsepower','Transmission : 7 or 8-speed automatic transmission','Drive type : Front-wheel drive','Suspension : Front and rear independent suspension','Brakes : Dynamic brake control','Wheels : Alloy','Interior : Premium materials, including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and rear view camera','Exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Sporty and compact SUV design','Optional : Panomaric sunroof','           Upgraded sound sysytem','           Driver assistance packages with additional safety features','           M sport X package for enhanced performance and styling','']
            white_bmw_x6 = ['','color : white','year : 2018','Petrol engine : 4.4-liter Twinpower turbo V8','Diesel engine : 3.0-liter Twinppower turbo inline-6','Power output : 300 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with touchscreen display','           Smartphone intergration','           Premium audio system','Safety : Advanced driver assistance system','         Multiple airbags','         Anti-lock braking system(ABS)','Electronic stability control(ESC)','Exterior : Signature BMW kidney grille','           LED headlights and taillights','           Power-folding mirrors','           Sunroof/moonroof','']
            white_bmw_8_series = ['','color : white','year : 2021','Engine : 4.4-liter Twinpower turbo V8','Power output : 335 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with a touchscreen display','           Navigation system','           Smartphone intergration','           Premium audio system','Safety : Advance driver assistance systems','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Distinctive BMW grille design','           LED headlights and taillights','           Power-folding mirrors','           Coupe convertible','']
            white_bmw_x7 = ['','color : white','year : 2019','Engine : 4.4-liter Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Brake assist','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Blue tooth connectivity','           Navigation sysytem','Safety : Multiple airbags(front,side,curtain)','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision with automatic emergency braking','         Parking sensors and rear view camera','exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Rear-seat entertainment system','           Driver assistance packages with additional safety features','           Luxury and M sport packages for enhanced performance and styling','']
            if z == 'BMW 3 series':
                for item in white_bmw_3_series:
                    print(item)
            if z == 'BMW 7 series':
                for item in white_bmw_7_series:
                    print(item)
            if z == 'BMW X2':
                for item in white_bmw_x2:
                    print(item)
            if z == 'BMW X6':
                for item in white_bmw_x6:
                    print(item)
            if z == 'BMW 8 series':
                for item in white_bmw_8_series:
                    print(item)
            if z == 'BMW X7':
                for item in white_bmw_x7:
                    print(item)

        if y == 'blue':
            print("The " + x + " cars available in blue are: ")
            blue_bmw_list = ['BMW 3 series','BMW 7 series','BMW 8 series','BMW X7','']
            for item in blue_bmw_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_bmw_3_series = ['','color : blue','year : 2021','petrol engine : 3.0-liter twinpower turbo inline-4','Diesel engines : 2.0-liter twinpower turbo inline-4','Power output : 180 - 400+ horsepower','Transmission : 6-speed automatic transmission','Drive type : RWD','Brakes : dynamic brake control','Wheels : Alloy','Interior : Apple CarPlay and android compatibility,','           bluetooth connectivity','           Navigation system','Safety : multiple airbags','Exterior : LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency','Optional : Panoramic sunroof','           upgraded sound system','           Driver assistance packages','           Ambient lighting','           Rear-seat entertainment system','']
            blue_bmw_7_series = ['','color : blue','year : 2019','Engine : 4.4-liter TwinPower Turbo V8(750i)','Power Output : 320 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive type : RWD','Suspension : Front and rear independent suspension','Brake : Anti-lock braking system','Wheels : Alloy','Interior : BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Advanced driver assistance features','Saftey : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and surround-view camera system','Exterior : Iconic BMW kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency and performance','Optional : Bowers & Wilkins diamond surround sound system','           Panoramic sky lounge LED roof','           Driving assistance proffesional package','']
            blue_bmw_8_series = ['','color : blue','year : 2021','Engine : 4.4-liter Twinpower turbo V8','Power output : 335 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with a touchscreen display','           Navigation system','           Smartphone intergration','           Premium audio system','Safety : Advance driver assistance systems','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Distinctive BMW grille design','           LED headlights and taillights','           Power-folding mirrors','           Coupe convertible','']
            blue_bmw_x7 = ['','color : blue','year : 2019','Engine : 4.4-liter Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Brake assist','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Blue tooth connectivity','           Navigation sysytem','Safety : Multiple airbags(front,side,curtain)','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision with automatic emergency braking','         Parking sensors and rear view camera','exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Rear-seat entertainment system','           Driver assistance packages with additional safety features','           Luxury and M sport packages for enhanced performance and styling','']
            if z == 'BMW 3 series':
                for item in blue_bmw_3_series:
                    print(item)
            if z == 'BMW 7 series':
                for item in blue_bmw_7_series:
                    print(item)
            if z == 'BMW 8 series':
                for item in blue_bmw_8_series:
                    print(item)
            if z == 'BMW X7':
                for item in blue_bmw_x7:
                    print(item)

        if y == 'violet':
            print("The " + x + "cars available in violet are: ")
            violet_bmw_list = ['BMW 3 series','BMW 7 series','BMW X2','BMW X6','BMW 8 series','BMW X7','']
            for item in violet_bmw_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            violet_bmw_3_series = ['','color : violet','year : 2021','petrol engine : 3.0-liter twinpower turbo inline-4','Diesel engines : 2.0-liter twinpower turbo inline-4','Power output : 180 - 400+ horsepower','Transmission : 6-speed automatic transmission','Drive type : RWD','Brakes : dynamic brake control','Wheels : Alloy','Interior : Apple CarPlay and android compatibility,','           bluetooth connectivity','           Navigation system','Safety : multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency','Optional : Panoramic sunroof','           upgraded sound system','           Driver assistance packages','           Ambient lighting','           Rear-seat entertainment system','']
            violet_bmw_7_series = ['','color : violet','year : 2019','Engine : 6.6-liter TwinPower Turbo V12(M760i xDrive)','Power Output : 320 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive type : RWD','Suspension : Front and rear independent suspension','Brake : Anti-lock braking system','Wheels : Alloy','Interior : BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Advanced driver assistance features','Saftey : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and surround-view camera system','Exterior : Iconic BMW kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency and performance','Optional : Bowers & Wilkins diamond surround sound system','           Panoramic sky lounge LED roof','           Driving assistance proffesional package','']
            violet_bmw_x2 = ['','color : violet','year : 2021','Engine : 2.0-litre Twinpower turbo inline-4','Power output : 192  - 302 horsepower','Transmission : 7 or 8-speed automatic transmission','Drive type : Front-wheel drive','Suspension : Front and rear independent suspension','Brakes : Dynamic brake control','Wheels : Alloy','Interior : Premium materials, including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and rear view camera','Exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Sporty and compact SUV design','Optional : Panomaric sunroof','           Upgraded sound sysytem','           Driver assistance packages with additional safety features','           M sport X package for enhanced performance and styling','']
            violet_bmw_x6 = ['','color : violet','year : 2018','Petrol engine : 4.4-liter Twinpower turbo V8','Diesel engine : 3.0-liter Twinppower turbo inline-6','Power output : 300 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with touchscreen display','           Smartphone intergration','           Premium audio system','Safety : Advanced driver assistance system','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Signature BMW kidney grille','           LED headlights and taillights','           Power-folding mirrors','           Sunroof/moonroof','']
            violet_bmw_8_series = ['','color : violet','year : 2021','Engine : 4.4-liter Twinpower turbo V8','Power output : 335 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with a touchscreen display','           Navigation system','           Smartphone intergration','           Premium audio system','Safety : Advance driver assistance systems','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Distinctive BMW grille design','           LED headlights and taillights','           Power-folding mirrors','           Coupe convertible','']
            violet_bmw_x7 = ['','color : violet','year : 2018','Engine : 4.4-liter Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Brake assist','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Blue tooth connectivity','           Navigation sysytem','Safety : Multiple airbags(front,side,curtain)','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision with automatic emergency braking','         Parking sensors and rear view camera','exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Rear-seat entertainment system','           Driver assistance packages with additional safety features','           Luxury and M sport packages for enhanced performance and styling','']
            if z == 'BMW 3 series':
                for item in violet_bmw_3_series:
                    print(item)
            if z == 'BMW 7 series':
                for item in violet_bmw_7_series:
                    print(item)
            if z == 'BMW X2':
                for item in violet_bmw_x2:
                    print(item)
            if z == 'BMW X6':
                for item in violet_bmw_x6:
                    print(item)
            if z == 'BMW 8 series':
                for item in violet_bmw_8_series:
                    print(item)
            if z == 'BMW X7':
                for item in violet_bmw_x7:
                    print(item)

        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_bmw_list = ['BMW 3 series','BMW X2','BMW X6','BMW 8 series','BMW X7','']
            for item in silver_bmw_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            silver_bmw_3_series = ['','color : silver','year : 2021','petrol engine : 3.0-liter twinpower turbo inline-4','Diesel engines : 2.0-liter twinpower turbo inline-4','Power output : 180 - 400+ horsepower','Transmission : 6-speed automatic transmission','Drive type : RWD','Brakes : dynamic brake control','Wheels : Alloy','Interior : Apple CarPlay and android compatibility,','           bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','Exterior : LED headlights and taillights','           Power-folding side mirrors','           Aerodynamic design-improved fuel efficiency','Optional : Panoramic sunroof','           upgraded sound system','           Driver assistance packages','           Ambient lighting','           Rear-seat entertainment system','']
            silver_bmw_x2 = ['','color : silver','year : 2021','Engine : 2.0-litre Twinpower turbo inline-4','Power output : 192  - 302 horsepower','Transmission : 7 or 8-speed automatic transmission','Drive type : Front-wheel drive','Suspension : Front and rear independent suspension','Brakes : Dynamic brake control','Wheels : Alloy','Interior : Premium materials, including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Bluetooth connectivity','           Navigation system','Safety : Multiple airbags','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision warning with automatic emergency braking','         Parking sensors and rear view camera','Exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Sporty and compact SUV design','Optional : Panomaric sunroof','           Upgraded sound sysytem','           Driver assistance packages with additional safety features','           M sport X package for enhanced performance and styling','']
            silver_bmw_x6 = ['','color : silver','year : 2018','Petrol engine : 4.4-liter Twinpower turbo V8','Diesel engine : 3.0-liter Twinppower turbo inline-6','Power output : 300 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with touchscreen display','           Smartphone intergration','           Premium audio system','Safety : Advanced driver assistance system','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Signature BMW kidney grille','           LED headlights and taillights','           Power-folding mirrors','           Sunroof/moonroof','']
            silver_bmw_8_series = ['','color : silver','year : 2021','Engine : 4.4-liter Twinpower turbo V8','Power output : 335 - 600+ horsepower','Transmission : 8-speed automatic transmission','Drive system : BMW xDrive','Suspension : Adaptive suspension','Wheels : Alloy','Interior : Premium leather upholstery','           Advanced infotainment system with a touchscreen display','           Navigation system','           Smartphone intergration','           Premium audio system','Safety : Advance driver assistance systems','         Multiple airbags','         Anti-lock braking system(ABS)','         Electronic stability control(ESC)','Exterior : Distinctive BMW grille design','           LED headlights and taillights','           Power-folding mirrors','           Coupe convertible','']
            silver_bmw_x7 = ['','color : silver','year : 2018','Engine : 4.4-liter Twinpower turbo inline-6(xDrive40i)','Power output : 335 - 523 horsepower','Transmission : 8-speed automatic transmission','Drive type : All-wheel drive(xDrive)','Suspension : Front and rear independent suspension','Brakes : Brake assist','Interior : Premium materials including optional leather upholstery','           BMW iDrive infotainment system with a central display screen','           Apple carplay and Android auto compatibility','           Blue tooth connectivity','           Navigation sysytem','Safety : Multiple airbags(front,side,curtain)','         Stability and traction control systems','         Adaptive cruise control','         Lane departure warning and lane-keeping assist','         Collision with automatic emergency braking','         Parking sensors and rear view camera','exterior : BMW signature kidney grille design','           LED headlights and taillights','           Power-folding side mirrors','           Roof rails and aerodynamic design','Optional : Panoramic sunroof','           Upgraded sound system','           Rear-seat entertainment system','           Driver assistance packages with additional safety features','           Luxury and M sport packages for enhanced performance and styling','']
            if z == 'BMW 3 series':
                for item in silver_bmw_3_series:
                    print(item)
            if z == 'BMW X2':
                for item in silver_bmw_x2:
                    print(item)
            if z == 'BMW X6':
                for item in silver_bmw_x6:
                    print(item)
            if z == 'BMW 8 series':
                for item in silver_bmw_8_series:
                    print(item)
            if z == 'BMW X7':
                for item in silver_bmw_x7:
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
            print("The " + x +" cars available in black are:")
            black_benz_list = ['Mercedes-Benz A-class','Mercedes-Benz S-class','Mercedes-Benz B-class','Mercedes-Benz SL','Mercedes-Benz GLS','Mercedes-Benz G-class','Mercedes-Benz GT','Mercedes-Benz Infinity','']
            for item in black_benz_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_a_class = ['','Color : black','Year : 2018','Petrol engines : 2.0-liter turbocharged inline-4-engine','Diesel engines : 2.0-liter turbocharged inline-4-diesel engine','Power output : 180 - 188 horsepower','Transmission : 7-speed dual clutch transmission','Interior : Modern design and high-quality materials','            Central infotainment display','            Multifunction steering wheel','            Premium audio systems','            Customizable ambient lighting','Technology : Voice recogniton','             Touch controls','             Touchpad controller intergrated into user interface','             Smartphone intergration','Safety : Advanced driver assistance systems','         Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','             Blind-spot monitoring','             Parking assistance']
            black_s_class = ['','Color : black','Year : 2019','Petrol engines : 2.0-liter turbocharged inline-4','Diesel engines : 2.0-liter turbocharged inline-4','Transmission : automatic transmission','Technology : Mercedes-Benz user experience (MBUX) infotainment system','             Driver assistance features','Interior : Premium upholestry and trim options','           multicontour seats with adjustable bolsters for enhanced comfort','Safety : Pre-safe system','         Multiple airbags','']
            black_b_class = ['','Color : black','Year : 2019','Petrol engines : 2.0-liter turbocharged inline-4 engine','Diesel engines : 2.0-liter turbocharged inline-4 engine','Transmission : Automatic transmission','Technology : MBUX infotainment system','             Driver assistance features','Interior : Adjustable seat configurations and high quality materials','Safety : Multiple airbags','         Stability control systems','         Advanced safety technologies to ensure occupant protection','']
            black_sl = ['','Color : black','Year : 2018','Petrol engines : 2.0-liter turbocharged V8','Diesel engines : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Technology : High-resolution infotainment system','             Advanced driver assistance systems','             Connectivity options','             Premium sound systems','             Navigation and voice control','Interior : High quality materials','           Premium leather upholstery','           Adjustable seats','           Climate control','Retractable hardtop','Safety : Multiple airbags','         Stability control systems','         Adaptive cruise control','         Lane-keeping assist','']
            black_gls = ['','Color : black','Year : 2018','Petrol engine : 2.0-liter turbocharged V6','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','Interior : Adjustable air suspension','           Adaptive damping','Safety : Multiple airbags','         Stability control systems','         Advanced driver assistance technologies','']
            black_g_class = ['','Color : black','Year : 2019','Petrol engines : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Off-road features : Three differential locks','                    A low-range gearbox','                    Advanced traction systems','                    Adjustable ride height','Technology : High-resolution infotainment system','             Premium sound system','             Driver assistance features','Interior : Premium leather upholstery','           Adjustable seating','           Modern convinience amenities','Covertible option','']
            if z == 'Mercedes-Benz A-class':
                for item in black_a_class:
                    print(item)
            if z == 'Mercedes-Benz S-class':
                for item in black_s_class:
                    print(item)
            if z == 'Mercedes-Benz B-class':
                for item in black_b_class:
                    print(item)
            if z == 'Mercedes-Benz SL':
                for item in black_sl:
                    print(item)
            if z == 'Mercedes-Benz GLS':
                for item in black_gls:
                    print(item)
            if z == 'Mercedes-Benz G-class':
                for item in black_g_class:
                    print(item)

        if y == 'white':
            print("The " + x +" cars available in white are: ")
            white_benz_list = ['Mercedes-Benz S-class','Mercedes-Benz G-class','Mercedes-Benz GLE','Mercedes-Benz GLA','Mercedes-Benz GLS','']
            for item in white_benz_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_s_class = ['','Color : White','Year : 2019','Petrol engines : 2.0-liter turbocharged inline-4','Diesel engines : 2.0-liter turbocharged inline-4','Transmission : automatic transmission','Technology : Mercedes-Benz user experience (MBUX) infotainment system','             Driver assistance features','Interior : Premium upholestry and trim options','           multicontour seats with adjustable bolsters for enhanced comfort','Safety : Pre-safe system','         Multiple airbags','']
            white_g_class = ['','Color : White','Year : 2019','Petrol engines : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Off-road features : Three differential locks','                    A low-range gearbox','                    Advanced traction systems','                    Adjustable ride height','Technology : High-resolution infotainment system','             Premium sound system','             Driver assistance features','Interior : Premium leather upholstery','           Adjustable seating','           Modern convinience amenities','Covertible option','']
            white_gle = ['','Color : White','Year : 2019','Petrol engine : 2.0-liter turbocharged inline-6','Diesel engine : 2.0-liter turbocharrged inline-6','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control system','             Lane-keeping assist','             Automatic emergency braking','Interior : Premium leather upholstrey','           Adjustable seats','           Modern convinience amenities','Comfort features : Adjustable air suspension','                   Adaptive damping contribute','']
            white_gla = ['','Color : White','Year : 2018','Petrol engine : 2.0-liter turbocharged inline-4','Diesel engine : 2.0-liter turbocharged inline-4','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking system','Interior : Premium leather upholstery','           Adjustable seats','           Modern convinience amenities','Comfort features : Climate control','Drive type : All-wheel drive','']
            white_gls = ['','Color : White','Year : 2018','Petrol engine : 2.0-liter turbocharged V6','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','Interior : Adjustable air suspension','           Adaptive damping','Safety : Multiple airbags','         Stability control systems','         Advanced driver assistance technologies','']
            if z == 'Mercedes-Benz S-class':
                for item in white_s_class:
                    print(item)
            if z == 'Mercedes-Benz G-class':
                for item in white_g_class:
                    print(item)
            if z == 'Mercedes-Benz GLE':
                for item in white_gle:
                    print(item)
            if z == 'Mercedes-Benz GLA':
                for item in white_gla:
                    print(item)
            if z == 'Mercedes-Benz GLS':
                for item in white_gls:
                    print(item)

        if y == 'silver':
            print("The " + x +" cars available in silver are: ")
            silver_benz_list = ['Mercedes-Benz C-class','Mercedes-Benz G-class','Mercedes-Benz CLS','Mercedes-Benz GT','']
            for item in silver_benz_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            silver_c_class = ['','Color : Silver','Year : 2019','Petrol engine : 2.0-liter turbocharged inline-6','Diesel engine : 2.0-liter turbocharged inline-6','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','Interior : Premium leather upholstery','           Adjustable seating','           Modern amenities convinience','Comfort features : Sport-tuned suspension','                   Climate control','']
            silver_g_class = ['','Color : Silver','Year : 2019','Petrol engines : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Off-road features : Three differential locks','                    A low-range gearbox','                    Advanced traction systems','                    Adjustable ride height','Technology : High-resolution infotainment system','             Premium sound system','             Driver assistance features','Interior : Premium leather upholstery','           Adjustable seating','           Modern convinience amenities','Covertible option','']
            silver_cls = ['','Color : Silver','Year : 2021','Petrol engine : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Druver assistance features','Interior : Premium upholstery','           Adjustable seating','           Modern convinience amenities','Comfort features : Sport-tuned suspension','                   Climate control','Four-door coupe design','']
            silver_gt = ['','Color : Silver','Year : 2020','Petrol enigne : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : High-performance automatic transmission','Suspension system : adjustable dumpers and adaptive air suspension','Exterior : Distinctive and aerodynamic design','Interior : Premium leather upholstery','Infotainment system : COMAND infotainment system','                      Touch-screen display','                      Navigation','                      Smartphone intergration','                      Voice control','Digital cockpit','Safety : Adaptive cruise control','         Lane-keeping assist','Automatic emergency braking','Performance exhaust system','Braking system : equipped with large ,ventilated brake discs and poerful calipers','Wheels and tires : enhanced grip','Convertible','']
            if z == 'Mercedes-Benz C-class':
                for item in silver_c_class:
                    print(item)
            if z == 'Mercedes-Benz G-class':
                for item in silver_g_class:
                    print(item)
            if z == 'Mercedes-Benz CLS':
                for item in silver_cls:
                    print(item)
            if z == 'Mercedes-Benz GT':
                for item in silver_gt:
                    print(item)

        if y == 'blue':
            print("The " + x +" cars available in blue are: ")
            blue_benz_list = ['Mercedes-Benz G-class','Mercedes-Benz C-class','Mercedes-Benz GT','']
            for item in blue_benz_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_g_class = ['','Color : Blue','Year : 2019','Petrol engines : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Off-road features : Three differential locks','                    A low-range gearbox','                    Advanced traction systems','                    Adjustable ride height','Technology : High-resolution infotainment system','             Premium sound system','             Driver assistance features','Interior : Premium leather upholstery','           Adjustable seating','           Modern convinience amenities','Covertible option','']
            blue_c_class = ['','Color : Blue','Year : 2021','Petrol engine : 2.0-liter turbocharged inline-6','Diesel engine : 2.0-liter turbocharged inline-6','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','Interior : Premium leather upholstery','           Adjustable seating','           Modern amenities convinience','Comfort features : Sport-tuned suspension','                   Climate control','']
            blue_gt = ['','Color : Blue','Year : 2020','Petrol enigne : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : High-performance automatic transmission','Suspension system : adjustable dumpers and adaptive air suspension','Exterior : Distinctive and aerodynamic design','Interior : Premium leather upholstery','Infotainment system : COMAND infotainment system','                      Touch-screen display','                      Navigation','                      Smartphone intergration','                      Voice control','Digital cockpit','Safety : Adaptive cruise control','         Lane-keeping assist','Automatic emergency braking','Performance exhaust system','Braking system : equipped with large ,ventilated brake discs and poerful calipers','Wheels and tires : enhanced grip','Convertible','']
            if z == 'Mercedes-Benz G-class':
                for item in blue_g_class:
                    print(item)
            if z == 'Mercedes-Benz C-class':
                for item in blue_c_class:
                    print(item)
            if z == 'Mercedes-Benz GT':
                for item in blue_gt:
                    print(item)

        if y == 'red':
            print("The " + x +" cars available in red are: ")
            red_benz_list = ['Mercedes-Benz G-class','Mercedes-Benz C-class','Mercedes-Benz GT','Mercedes-Benz SLC','Mercedes-Benz B-class','']
            for item in red_benz_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            red_g_class = ['','Color : Red','Year : 2019','Petrol engines : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : Sophisticated automatic transmission','Off-road features : Three differential locks','                    A low-range gearbox','                    Advanced traction systems','                    Adjustable ride height','Technology : High-resolution infotainment system','             Premium sound system','             Driver assistance features','Interior : Premium leather upholstery','           Adjustable seating','           Modern convinience amenities','Covertible option','']
            red_c_class = ['','Color : Red','Year : 2021','Petrol engine : 2.0-liter turbocharged inline-6','Diesel engine : 2.0-liter turbocharged inline-6','Transmission : Sophisticated automatic transmission','Technology : MBUX infotainment system','             Adaptive cruise control','             Lane-keeping assist','             Automatic emergency braking','Interior : Premium leather upholstery','           Adjustable seating','           Modern amenities convinience','Comfort features : Sport-tuned suspension','                   Climate control','']
            red_gt = ['','Color : Red','Year : 2021','Petrol enigne : 2.0-liter turbocharged V8','Diesel engine : 2.0-liter turbocharged V8','Transmission : High-performance automatic transmission','Suspension system : adjustable dumpers and adaptive air suspension','Exterior : Distinctive and aerodynamic design','Interior : Premium leather upholstery','Infotainment system : COMAND infotainment system','                      Touch-screen display','                      Navigation','                      Smartphone intergration','                      Voice control','Digital cockpit','Safety : Adaptive cruise control','         Lane-keeping assist','Automatic emergency braking','Performance exhaust system','Braking system : equipped with large ,ventilated brake discs and poerful calipers','Wheels and tires : enhanced grip','Convertible','']
            red_slc = ['','Color : Red','Year : 2019','Petrol engine : 2.0-liter turbocharged inline-4','Diesel engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Convertible hardtop','Interior : Leather upholstery','           Heated seats','           Premium audio systems','Infotainment system : COMAND infotainment system','Safety : Multiple airbags','         Adaptive cruise control','         Blind-spot monitoring','         Automatic emergency braking','Airscarf neck-level heating','Convertible wind deflector','Exterior : Sporty and aerodynamic design','Dual exhaust system','']
            red_b_class = ['','Color : Red','Year : 2019','Petrol engines : 2.0-liter turbocharged inline-4 engine','Diesel engines : 2.0-liter turbocharged inline-4 engine','Transmission : Automatic transmission','Technology : MBUX infotainment system','             Driver assistance features','Interior : Adjustable seat configurations and high quality materials','Safety : Multiple airbags','         Stability control systems','         Advanced safety technologies to ensure occupant protection','']
            if z == 'Mercedes-Benz G-class':
                for item in red_g_class:
                    print(item)
            if z == 'Mercedes-Benz C-class':
                for item in red_c_class:
                    print(item)
            if z == 'Mercedes-Benz GT':
                for item in red_gt:
                    print(item)
            if z == 'Mercedes-Benz SLC':
                for item in red_slc:
                    print(item)
            if z == 'Mercedes-Benz B-class':
                for item in red_b_class:
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
            print("The " + x + " cars available in black are:")
            black_toyota_list = ['Toyota Sienna','Toyota Tacoma','Toyota Land Cruiser','Toyota Supra','Toyota 4Runner','Toyota Corolla','']
            for item in black_toyota_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_sienna = ['','Color : black','Year : 2022','Engine : 2.0-liter turbocharged inline-4','Interior : Spacious and versatile','           Leather upholstery','           Power adjustable seats','           Premium material','Infotainment : Touchsreen infotainment system','Connectivity : Bluetooth connectivity for hand-free calling and audio streaming','Safety : Adaptive cruise control','         Lane departure warning','         Automatic emergency braking','         Multiple airbags','         Rearview camera','Comfort : Climate control for front passengers','          Sliding doors for easy access to rear seats','          Power liftgate for convinient access to rear cargo area','Versatility : Third-row seating','              Foldable rear seats to expand cargo space','Entertainment : Rear-seat entertainment system','']
            black_tacoma = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic and manual transmission','4WD and off-road capability','Towing and payload capacity','Infotainment : Touchscreen infotainment system','Connectivity : Bluetooth connectivity','               USB ports','Safety : Pre-collision system with pedestrian detection','         Lane departure alert','         Adaptive cruise control','Interior : Power-adjustable seats','           Leather upholstery','Bed features : composite bed,bed liner and storage compartments','Off-road packages','Exterior : Alloy wheels','           Hood scoop','Entertainment : Optional JBL premium audio system','']
            black_landcruiser = ['','Color : black','Year : 2018','Engine : 2.0-liter turbocharged V8','Full-time 4WD system for off-road capability','Off-road features : Multi-terrain select system','                    Crawl control','                    Locking center differential','                    Kinetic Dynamic Suspension System(KDSS)','Luxury : Premium leather upholstery','         Heated and ventilated front seats','         Heated rear seats','Infotainment : Touchscreen infotainment system','Connectivity : Bluetooth connectivity','Safety : Pre-collision system','         lane departure alert','         Adaptive cruise control','Seating : Three-row seating','          Foldable rear seats','Climate control','Exterior : Power moonroof','           Roof rack for additional cargo carrying','Towing capability','Multi-terrain monitor','Kinetic Dynamic Suspension System','Multi terrain select system','']
            black_supra = ['','Color : black','Year : 2017','Engine : 3.0-liter turbocharged inline-6','Transmission : 8-speed automatic transmission with paddle shifters','Acceleratio : Sporty performance','Chassis and suspension : Rigid chassis and sport-tuned suspension','Interior : Driver-focused cockpit design','           Advanced infotainment system with touchscreen display','           Connectivity features including smartphone intergration','Safety : Adaptive cruise control','         Lane departure alert','         Automatic emergency brakingBraking system : High-performance','Wheels and tires : Sporty wheels and high performance tires for optimal grip','Limited-slip differential : For improved traction during acceleration','']
            black_4runner = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-6','4WD systems for different trims','Off-road features : Skid plates for underbody protection','                    Off-road-tuned suspension for improved performance on rough terrain','                    Crawl control and multi terrain select','Towing capacity','Seat capacity : five passengers','Cargo space : Foldable rear seats for more cargo space','Infotainment system : Touchscreen with smartphone intergration','Safety : Suite of airbags','         Stability control','         Traction control','         Pre-collision systems','         Lane departure warning','         Adaptive cruise control','Interior : Leather upholstery','       Power-adjustable driver seat','           Heated and ventilated front seats','Sunroof : Power-sliding moonroof for open-air driving experience','Roof rails : For additional cargo space','Multi-information display : Display information and fuel efficiency,trip data and vehicle status','Smart key system : Keyless entry and push-button start for convinience','']
            black_corolla = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Fuel efficiency : econimical consuption','Safety : Pre-collision systems','         Lane departure alert','         Adaptive cruise control','Infotainment system : Touchscreen with bluetooth connectivity','Interior : Upgraded upholstery','           Power-adjustable driver seat','Driver assistance features : Rear view camera','                             Blind-spot monitoring','                             Rear cross-traffic alert','Multifunction steering wheel : Mounted controls for audio,phone and cruise control','Smart key system : Push-button start for convinience','LED headlights','USB ports','Automatic climate control : Enhanced comfort','Spacious interior : Ample legroom for passengers','']
            if z == 'Toyota Sienna':
                for item in black_sienna:
                    print(item)
            if z == 'Toyota Tacoma':
                for item in black_tacoma:
                    print(item)
            if z == 'Toyota Land Cruiser':
                for item in black_landcruiser:
                    print(item)
            if z == 'Toyota Supra':
                for item in black_supra:
                    print(item)
            if z == 'Toyota 4Runner':
                for item in black_4runner:
                    print(item)
            if z == 'Toyota Corolla':
                for item in black_corolla:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_toyota_list = ['Toyota Land Cruiser','Toyota Corolla','Toyota Supra','Toyota Tundra','Toyota C-HR','Toyota Sequoia','']
            for item in white_toyota_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_landcruiser = ['','Color : White','Year : 2018','Engine : 2.0-liter turbocharged V8','Full-time 4WD system for off-road capability','Off-road features : Multi-terrain select system','                    Crawl control','                    Locking center differential','                    Kinetic Dynamic Suspension System(KDSS)','Luxury : Premium leather upholstery','         Heated and ventilated front seats','         Heated rear seats','Infotainment : Touchscreen infotainment system','Connectivity : Bluetooth connectivity','Safety : Pre-collision system','         lane departure alert','         Adaptive cruise control','Seating : Three-row seating','          Foldable rear seats','Climate control','Exterior : Power moonroof','           Roof rack for additional cargo carrying','Towing capability','Multi-terrain monitor','Kinetic Dynamic Suspension System','Multi terrain select system','']
            white_corolla = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Fuel efficiency : econimical consuption','Safety : Pre-collision systems','         Lane departure alert','         Adaptive cruise control','Infotainment system : Touchscreen with bluetooth connectivity','Interior : Upgraded upholstery','           Power-adjustable driver seat','Driver assistance features : Rear view camera','                             Blind-spot monitoring','                             Rear cross-traffic alert','Multifunction steering wheel : Mounted controls for audio,phone and cruise control','Smart key system : Push-button start for convinience','LED headlights','USB ports','Automatic climate control : Enhanced comfort','Spacious interior : Ample legroom for passengers','']
            white_supra = ['','Color : White','Year : 2017','Engine : 3.0-liter turbocharged inline-6','Transmission : 8-speed automatic transmission with paddle shifters','Acceleratio : Sporty performance','Chassis and suspension : Rigid chassis and sport-tuned suspension','Interior : Driver-focused cockpit design','           Advanced infotainment system with touchscreen display','           Connectivity features including smartphone intergration','Safety : Adaptive cruise control','         Lane departure alert','         Automatic emergency brakingBraking system : High-performance','Wheels and tires : Sporty wheels and high performance tires for optimal grip','Limited-slip differential : For improved traction during acceleration','']
            white_tundra = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged V8','Towing capacity : Suitable for hauling trailers','4WD : Enhanced off-road capability and traction','Transmission : Robust automatic transmission for smooth shifting','CrewMax and Double Cab Options','Payload capacity : Suitable for both work and recreational activities','Safety : Airbags','         Stability control','         Traction control','Infotainment system : Touchscreen with bluetooth connectivity','Tundra TRD off-road packages : Off-road-tuned suspension,skid plates','Driver assistance features : Foward collision warning','                             Lane departure warning','                             Adaptive cruise control','Power-adjustable seats','Trailer sway control : Maintain stability while towing','']
            white_c_hr = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission for smooth and efficient performance','Exterior : Stylish with sharp lines and coupe-like roofline','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Pre-collision systems','         Adaptive cruise control','         Lane departure warning','Driver assistance features : Bllind-spot monitoring','Interior : Leather trimmed seating','Dual-zone climate control','Cargo space : Split foldable rear seats','LED headlights','Wheels : Alloy','Handling and suspension : Responsive handling and wee-tuned suspension','Traction control : Improved stability during various driving conditions','Compact size : Maneuverable and compact size for urban driving and easy parking','']
            white_sequoia = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V8','Towing capacity : Capable of towing trailers and boats','Seating capacity : Three-row seating accomodating 7 passengers','Cargo space : Foldable rear seats','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rear-view camera','         Foward collision warning','         Lane departure warning','         Adaptive cruise control','Driver assistance features : Blind-spot monitoring','Climate control : For front and rear passengers','Power-adjustable seats','Keyless entry ignition : Push-button start for ease of access','Sunroof : Power-sliding moonroof for open air driver experince','Off-road capability : Multi-mode 4WD system','Entertaiinment : DVD or Blu-ray player','Advanced suspension system : Adaptive variable suspension','']
            if z == 'Toyota Land Cruiser':
                for item in white_landcruiser:
                    print(item)
            if z == 'Toyota corolla':
                for item in white_corolla:
                    print(item)
            if z == 'Toyota Supra':
                for item in white_supra:
                    print(item)
            if z == 'Toyota Tundra':
                for item in white_tundra:
                    print(item)
            if z == 'Toyota C-HR':
                for item in white_c_hr:
                    print(item)
            if z == 'Toyota Sequoia':
                for item in white_sequoia:
                    print(item)

        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_toyota_list = ['Toyota Supra','Toyota Corolla','Toyota Sienna','Toyota 4Runner','Toyota Land Cruiser','']
            for item in silver_toyota_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            silver_supra = ['','Color : Silver','Year : 2017','Engine : 3.0-liter turbocharged inline-6','Transmission : 8-speed automatic transmission with paddle shifters','Acceleratio : Sporty performance','Chassis and suspension : Rigid chassis and sport-tuned suspension','Interior : Driver-focused cockpit design','           Advanced infotainment system with touchscreen display','           Connectivity features including smartphone intergration','Safety : Adaptive cruise control','         Lane departure alert','         Automatic emergency brakingBraking system : High-performance','Wheels and tires : Sporty wheels and high performance tires for optimal grip','Limited-slip differential : For improved traction during acceleration','']
            silver_corolla = ['','Color : Silver','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Fuel efficiency : econimical consuption','Safety : Pre-collision systems','         Lane departure alert','         Adaptive cruise control','Infotainment system : Touchscreen with bluetooth connectivity','Interior : Upgraded upholstery','           Power-adjustable driver seat','Driver assistance features : Rear view camera','                             Blind-spot monitoring','                             Rear cross-traffic alert','Multifunction steering wheel : Mounted controls for audio,phone and cruise control','Smart key system : Push-button start for convinience','LED headlights','USB ports','Automatic climate control : Enhanced comfort','Spacious interior : Ample legroom for passengers','']
            silver_sienna = ['','Color : Silver','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Interior : Spacious and versatile','           Leather upholstery','           Power adjustable seats','           Premium material','Infotainment : Touchsreen infotainment system','Connectivity : Bluetooth connectivity for hand-free calling and audio streaming','Safety : Adaptive cruise control','         Lane departure warning','         Automatic emergency braking','         Multiple airbags','         Rearview camera','Comfort : Climate control for front passengers','          Sliding doors for easy access to rear seats','          Power liftgate for convinient access to rear cargo area','Versatility : Third-row seating','              Foldable rear seats to expand cargo space','Entertainment : Rear-seat entertainment system','']
            silver_4runner = ['','Color : Silver','Year : 2021','Engine : 2.0-liter turbocharged inline-6','4WD systems for different trims','Off-road features : Skid plates for underbody protection','                    Off-road-tuned suspension for improved performance on rough terrain','                    Crawl control and multi terrain select','Towing capacity','Seat capacity : five passengers','Cargo space : Foldable rear seats for more cargo space','Infotainment system : Touchscreen with smartphone intergration','Safety : Suite of airbags','         Stability control','         Traction control','         Pre-collision systems','         Lane departure warning','         Adaptive cruise control','Interior : Leather upholstery','       Power-adjustable driver seat','           Heated and ventilated front seats','Sunroof : Power-sliding moonroof for open-air driving experience','Roof rails : For additional cargo space','Multi-information display : Display information and fuel efficiency,trip data and vehicle status','Smart key system : Keyless entry and push-button start for convinience','']
            silver_landcruiser = ['','Color : Silver','Year : 2018','Engine : 2.0-liter turbocharged V8','Full-time 4WD system for off-road capability','Off-road features : Multi-terrain select system','                    Crawl control','                    Locking center differential','                    Kinetic Dynamic Suspension System(KDSS)','Luxury : Premium leather upholstery','         Heated and ventilated front seats','         Heated rear seats','Infotainment : Touchscreen infotainment system','Connectivity : Bluetooth connectivity','Safety : Pre-collision system','         lane departure alert','         Adaptive cruise control','Seating : Three-row seating','          Foldable rear seats','Climate control','Exterior : Power moonroof','           Roof rack for additional cargo carrying','Towing capability','Multi-terrain monitor','Kinetic Dynamic Suspension System','Multi terrain select system','']
            if z == 'Toyota Supra':
                for item in silver_supra:
                    print(item)
            if z == 'Toyota Corolla':
                for item in silver_corolla:
                    print(item)
            if z == 'Toyota Sienna':
                for item in silver_sienna:
                    print(item)
            if z == 'Toyota 4Runner':
                for item in silver_4runner:
                    print(item)
            if z == 'Toyota Land Cruiser':
                for item in silver_landcruiser:
                    print(item)

        if y == 'blue':
            print("The " + x + " cars available in blue are: ")
            blue_toyota_list = ['Toyota Land Cruiser','Toyota Corolla','Toyota Sienna','Toyota Supra','Toyota GT Supra','']
            for item in blue_toyota_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_landcruiser = ['','Color : Blue','Year : 2018','Engine : 2.0-liter turbocharged V8','Full-time 4WD system for off-road capability','Off-road features : Multi-terrain select system','                    Crawl control','                    Locking center differential','                    Kinetic Dynamic Suspension System(KDSS)','Luxury : Premium leather upholstery','         Heated and ventilated front seats','         Heated rear seats','Infotainment : Touchscreen infotainment system','Connectivity : Bluetooth connectivity','Safety : Pre-collision system','         lane departure alert','         Adaptive cruise control','Seating : Three-row seating','          Foldable rear seats','Climate control','Exterior : Power moonroof','           Roof rack for additional cargo carrying','Towing capability','Multi-terrain monitor','Kinetic Dynamic Suspension System','Multi terrain select system','']
            blue_corolla = ['','Color : Blue','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Fuel efficiency : econimical consuption','Safety : Pre-collision systems','         Lane departure alert','         Adaptive cruise control','Infotainment system : Touchscreen with bluetooth connectivity','Interior : Upgraded upholstery','           Power-adjustable driver seat','Driver assistance features : Rear view camera','                             Blind-spot monitoring','                             Rear cross-traffic alert','Multifunction steering wheel : Mounted controls for audio,phone and cruise control','Smart key system : Push-button start for convinience','LED headlights','USB ports','Automatic climate control : Enhanced comfort','Spacious interior : Ample legroom for passengers','']
            blue_sienna = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Interior : Spacious and versatile','           Leather upholstery','           Power adjustable seats','           Premium material','Infotainment : Touchsreen infotainment system','Connectivity : Bluetooth connectivity for hand-free calling and audio streaming','Safety : Adaptive cruise control','         Lane departure warning','         Automatic emergency braking','         Multiple airbags','         Rearview camera','Comfort : Climate control for front passengers','          Sliding doors for easy access to rear seats','          Power liftgate for convinient access to rear cargo area','Versatility : Third-row seating','              Foldable rear seats to expand cargo space','Entertainment : Rear-seat entertainment system','']
            blue_supra = ['','Color : Blue','Year : 2017','Engine : 3.0-liter turbocharged inline-6','Transmission : 8-speed automatic transmission with paddle shifters','Acceleratio : Sporty performance','Chassis and suspension : Rigid chassis and sport-tuned suspension','Interior : Driver-focused cockpit design','           Advanced infotainment system with touchscreen display','           Connectivity features including smartphone intergration','Safety : Adaptive cruise control','         Lane departure alert','         Automatic emergency brakingBraking system : High-performance','Wheels and tires : Sporty wheels and high performance tires for optimal grip','Limited-slip differential : For improved traction during acceleration','']
            blue_gt_supra = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-6','Transmission : 8-speed automatic transmission','Acceleration : Sporty performance','Chassis : Rigid chassis','Suspension : Sport-tuned suspension for enhanced handling and responsiveness','Design : Sleek and aerodynamic design withclassic sports car proportions','Inyterior : Driver-focused cockpit design','Infotainment system with touchscreen display and navigation','Safety : Airbags','         Foward collision warning','         Automatic emergency braking','Driving modes : Sport and normal modes','Braking system : High-performance for effective stopping power','Limited-slip differential : Improved traction and cornering','Wheels and tires : Sporty wheels and high performance tires for optimal grip','Exhaust system : Sport-tuned exhaust system for a distinctive engine sound','Seats : Sport seats with adjustable features for comfort','Head-up display : Provides essential information without taking eyes off the road','']
            if z == 'Toyota Land Cruiser':
                for item in blue_landcruiser:
                    print(item)
            if z == 'Toyota Corolla':
                for item in blue_corolla:
                    print(item)
            if z == 'Toyota Sienna':
                for item in blue_sienna:
                    print(item)
            if z == 'Toyota Supra':
                for item in blue_supra:
                    print(item)
            if z == 'Toyota GT Supra':
                for item in blue_gt_supra:
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
            print("The " + x + " cars available in black are:")
            black_mitsubishi_list = ['Mitsubishi Outlander','Mitsubishi Outlander Sport','']
            for item in black_mitsubishi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_outlander = ['','Color : black','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Transmission : Traditional automatic transmission','Seating capacity : two-row seating for five passengers','Cargo space : Foldable rear seats','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rearview camera','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Driver assistance features : Blind-spot monitoring','Interior : Leather trimmed seating','Climate control : Automatic for front and rear seats','Keyless entry and ignition : Push-button for ease of use','Panooramic sunroof : Open and airy feeling','Towing capability : Capable of towing trailers','Off--road capability : Enhance traction','']
            black_outlander_sport = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Transmission : Continuously variable transmission','Seating capacity : Two-row seating for five passengers','Cargo space : Foldable rear seats','Infotaiinment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rearview camera','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Driver assistance features : Blind-spot monitoring','Interior : Leather trimmed seating','           Power-adjustable seats','Climate control : For front and rear passengers','Keyless entry and ignition : Push-button start for easy use','Panoramic sunroof : For ventilation','Towint capability : For smaller loads','Wheels : Stylish alloy wheels','Off-road capability : Enhanced traction on various surfaces','']
            if z == 'Mitsubishi Outlander':
                for item in black_outlander:
                    print(item)
            if z == 'Mitsubishi Outlander Sport':
                for item in black_outlander_sport:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_mitsubishi_list = ['Mitsubishi Outlander','']
            for item in white_mitsubishi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_outlander = ['','Color : White','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Transmission : Traditional automatic transmission','Seating capacity : two-row seating for five passengers','Cargo space : Foldable rear seats','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rearview camera','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Driver assistance features : Blind-spot monitoring','Interior : Leather trimmed seating','Climate control : Automatic for front and rear seats','Keyless entry and ignition : Push-button for ease of use','Panooramic sunroof : Open and airy feeling','Towing capability : Capable of towing trailers','Off--road capability : Enhance traction','']
            if z == 'Mitsubishi Outlander':
                for item in white_outlander:
                    print(item)
        if y == 'silver':
            print("The " + x + " cars available in silver are: ")
            silver_mitsubishi_list = ['Mitsubishi Outlander','Mitsubishi Eclipse Cross','']
            for item in silver_mitsubishi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            silver_outlander = ['','Color : Silver','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Transmission : Traditional automatic transmission','Seating capacity : two-row seating for five passengers','Cargo space : Foldable rear seats','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rearview camera','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Driver assistance features : Blind-spot monitoring','Interior : Leather trimmed seating','Climate control : Automatic for front and rear seats','Keyless entry and ignition : Push-button for ease of use','Panooramic sunroof : Open and airy feeling','Towing capability : Capable of towing trailers','Off--road capability : Enhance traction','']
            silver_eclipse_cross = ['','Color : Silver','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission','Seating capacity : Two-row seating for five passengers','Cargo space : Foldable rear seats','Infotainment system : Touchscreen with bluetooth connectivity','Safety : Airbags','         Stability control','         Traction control','         Rearview camera','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Driver assistance features : Blind-spot monitoring','Interior : Leather trimmed seating','           Power-adjustable seats','Climate control : For front and rear passengers','Keyless entry and ignition : Push-button start for easee of use','Panoramic sunroof : Ventilation','Towing capability : For smaller loads','Wheels : Stylish alloy','All-wheel drive','']
            if z == 'Mitsubishi Outlander':
                for item in silver_outlander:
                    print(item)
            if z == 'Mitsubishi Eclipse Cross':
                for item in silver_eclipse_cross:
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
            black_lexus_list = ['Lexus GX','Lexus LC','Lexus UX','Lexus IS','Lexus ES','Lexus RC','Lexus LX','']
            for item in black_lexus_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_lexus_gx = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged V8','4WD system','Interior : Spacious and luxurious cabin with high-quality materials','           Leather-trimmed seats','           Heated and ventilated front seats','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision alert','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Off-road capability : Built on rugged body-on-frame chassis suitable for off-road driving','                      Adajustable suspension for better handling on different terrains','Seating and cargo space : Three-row seating accomodating upto seven passengers','                          Power-folding third-row seats for increased cargo space','Luxury and comfort : Wood and leather-trimmed interior','                     Multi-zone climate control','                     Power-adjustable steering wheel and driver seat','Exterior : Stylishand distinctive exterior design','          Power-retractable side mirrors','          Roof-rails for additional cargo options','Towing capacity : Can tow trailers or boats','']
            black_lexus_lc = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged V8','RWD configuration','Interior : Leather-trimmed seats','          Heated and ventilated front seats','          Driver-focused cockpit design','Infotainment : Lexus enform infotainment system','               High-resolution touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Convertible option : With a retractable soft top','Performance : Variable Gear Ratio Steering(VGRS) for impproved steering response','Exterior : Striking and aerodynamic design','         LED headlights and taillights','         Power-folding side mirrors','Audio system : High-end such as Mark Levinson sound system','Drive modes : Eco,Comfort,Sport','']
            black_lexus_ux = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','AWD configuration','Interior : Leather-trimmed seats','         Heated and ventilated front seats','         Driver-focused cockpit design','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Exterior : Distinctive and aerodynamic exterior design','           LED headlights and taillights','           Power-folding side mirrors','Audio system : High-quality Mark Levinson sound system','Drive modes : Eco,Normal,Sport','Cargo space : Versatile cargo space','Smart key and push-button start','']
            black_lexus_is = ['','Color : black','Year : 2018','Engine : 2.0-liter turbocharged V6','Right Wheel Drive(RWD)','Interior : Leather-trimmed','         Heated and ventilated front seats','         Driver-centric cockpit design','Infotainment : Lexus enform infotainment system','               Touchscreen display','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Exterior : Distinctive and aerodynamic exterior design','           LED headlights and taillights','           Power-folding side mirrors','Driving modes : Eco,Normal.Sport','Audio system : High-quality like Mark Levinson sound system','Smart key and push-button start','Performance : Sport-tuned suspension for responsive handling','              Variable Gear Ratio Steering(VGRS) for improved steering response','Sunroof : Available','']
            black_lexus_es = ['','Color : black','Year : 2019','Engine :2.0-liter turbocharged V6','Four Wheel Drive','Interior : Leather-trimmed seats','         Heated and ventilated front seats','         Spacious and comfortable cabin design','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Exterior : Elegant aerodynamic design','           LED headlights and taillights','           Power-folding side mirrors','Drive modes : Eco,Normal,Sport','Audio : High-quality like Mark Levinson sound system','Smart key and push-button start','Sunroof : Available','Comfort : Dual-zone automatic climate control','          Available ambient lighting','']
            black_lexus_rc = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged V6','Rear-Wheel Drive(RWD)','Interior : Leather-trimmed seats','           Heated and ventilated front seats','           Driver-focused cockpit design','Infotainment : Lexus enform infortainment system','               Touchscreen display','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and a comprehensive airbag system','         Blind-spot monitoring','Exterior : Striking and aerodynamic design','           LED headlights and taillights','           Power-folding side mirrors','Driving modes : Eco,Normal,Sport','Audio : Mark Levinson sound system','Smart key and push-button start','Performance : Sport-tuned suspension for responsive handling','Sunroof : Available','']
            black_lexus_lx = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Comfort : High-quality leather upholstery','           Spacious and comfortable seating for passengers','Technology : Advanced infotainment with touchscreen display','               Navigation system with real-time traffic updates','               Premium audio system','Connectivity : Bluetooth,USB and smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Multiple airbags','         Parking assist features','Off-road capabilities : Four-wheel drive system','Design : Iconic spindle grille','         Exterior design that reflects a blend of luxury and ruggedness','Interior : High-end interior','           Multi-zone climate control for personalised comfort','']
        
            if z == 'Lexus GX':
                for item in black_lexus_gx:
                    print(item)
            if z == 'Lexus LC':
                for item in black_lexus_lc:
                    print(item)
            if z == 'Lexus UX':
                for item in black_lexus_ux:
                    print(item)
            if z == 'Lexus IS':
                for item in black_lexus_is:
                    print(item)
            if z == 'Lexus ES':
                for item in black_lexus_es:
                    print(item)
            if z == 'Lexus RC':
                for item in black_lexus_rc:
                    print(item)
            if z == 'Lexus LX':
                for item in black_lexus_lx:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_lexus_list = ['Lexus GX','Lexus NX','Lexus UX','Lexus RC','Lexus GS','Lexus LS','Lexus ES','']
            for item in white_lexus_list:
                print(list)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_lexus_gx = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V8','4WD system','Interior : Spacious and luxurious cabin with high-quality materials','           Leather-trimmed seats','           Heated and ventilated front seats','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision alert','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Off-road capability : Built on rugged body-on-frame chassis suitable for off-road driving','                      Adajustable suspension for better handling on different terrains','Seating and cargo space : Three-row seating accomodating upto seven passengers','                          Power-folding third-row seats for increased cargo space','Luxury and comfort : Wood and leather-trimmed interior','                     Multi-zone climate control','                     Power-adjustable steering wheel and driver seat','Exterior : Stylishand distinctive exterior design','          Power-retractable side mirrors','          Roof-rails for additional cargo options','Towing capacity : Can tow trailers or boats','']
            white_lexus_nx = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','Comfort : High-quality material including high-quality upholstery','          Comfortable seating with available power adjustable and heated options','Technology : Lexus enform infotainment system with touchscreen display','             Smartphone intergration','             Navigation system with real-time traffic updates','             Premium audio system','Safety : Adaptive cruise control','         Lane departure warning','         Autoomatic emergency braking','         Multiple airbags for occupant protection','         Blind-spot monitoring and rear cross-traffic alert','Design : Spindle grille and sleek exterior designs','Interior : User-friendly and stylish dashboard design','Multi-zone climate control for personaliized comfort','Hybrid technology : Improved fuel efficiency and lower emissions','Cargo space : Adequate','']
            white_lexus_ux = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','AWD configuration','Interior : Leather-trimmed seats','         Heated and ventilated front seats','         Driver-focused cockpit design','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Exterior : Distinctive and aerodynamic exterior design','           LED headlights and taillights','           Power-folding side mirrors','Audio system : High-quality Mark Levinson sound system','Drive modes : Eco,Normal,Sport','Cargo space : Versatile cargo space','Smart key and push-button start','']
            white_lexus_rc = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged V6','Rear-Wheel Drive(RWD)','Interior : Leather-trimmed seats','           Heated and ventilated front seats','           Driver-focused cockpit design','Infotainment : Lexus enform infortainment system','               Touchscreen display','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and a comprehensive airbag system','         Blind-spot monitoring','Exterior : Striking and aerodynamic design','           LED headlights and taillights','           Power-folding side mirrors','Driving modes : Eco,Normal,Sport','Audio : Mark Levinson sound system','Smart key and push-button start','Performance : Sport-tuned suspension for responsive handling','Sunroof : Available','']
            white_lexus_gs = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged V8','Drive type : Rear-Wheel Drive(RWD)','Comfort : Premium leather upholstery','          Comfortable and well-appointed seating with power-adjustable options','Technology : Lexus enform infotainment system with central display screen','               Smartphone intergration','               Navigation system','               Premium audio system','Safety : Adaptive cruise control','         Lane departure warning','         Automatic emergency braking','         Multiple airbags for occupant protection','         Blind-spot monitoring and rear-cross-traffic alert','Design : Spindle grille and sophisticated exterior lines','Interior : Well designed dashboard with high-quality finishes','           Multi-zone climate control for comfort','Performance : Adaptive suspension for balance between comfort and handling','              Variable gear ratio steering for improved responsiveness','']
            white_lexus_ls = ['','Color : White','Year : 2019','Engine :2.0-liter turbocharged V8','Comfort : Sumptios and spacious interior','          Comfortable,power-adjustable seats with heating,ventilation and massage functions','Technology : Large touchscreen infotainment system','             Lexus enform multimedia system with navigation and smartphone intergration','               Premium Mark Levinson audio system','               Rear-seat entertainment system with dual screens','Safety : Adaptive cruise control','         Lane departure warning','         Automatic emergency braking','         Multiple airbags','         Pre-collision systems','         Parking assist','Design : Spindle grille','         High attention in detail','Interior : Opulent interior design','           Ambient lighting','           Rear-seat amenities','           Reclining and massaging rear seats','Performance : Adaptive air suspension for a smooth ride and adjustable ride height','             Adavanced chassis control systems for enhanced handling','']
            white_lexus_es = ['','Color : White','Year : 2019','Engine :2.0-liter turbocharged V6','Four Wheel Drive','Interior : Leather-trimmed seats','         Heated and ventilated front seats','         Spacious and comfortable cabin design','Infotainment : Lexus enform infotainment system','               Touchscreen display','               Navigation system','Connectivity : Smartphone intergration','Safety : Adaptive cruise control','         Lane departure warning','         Foward collision warning','         Automatic emergency braking','         Multiple airbags and comprehensive airbag system','         Blind-spot monitoring','Exterior : Elegant aerodynamic design','           LED headlights and taillights','           Power-folding side mirrors','Drive modes : Eco,Normal,Sport','Audio : High-quality like Mark Levinson sound system','Smart key and push-button start','Sunroof : Available','Comfort : Dual-zone automatic climate control','          Available ambient lighting','']
            if z == 'Lexus GX':
                for item in white_lexus_gx:
                    print(item)
            if z == 'Lexus NX':
                for item in white_lexus_nx:
                    print(item)
            if z == 'Lexus UX':
                for item in white_lexus_ux:
                    print(item)
            if z == 'Lexus RC':
                for item in white_lexus_rc:
                    print(item)
            if z == 'Lexus GS':
                for item in white_lexus_gs:
                    print(item)
            if z == 'Lexus LS':
                for item in white_lexus_ls:
                    print(item)
            if z == 'Lexus ES':
                for item in white_lexus_es:
                    print(item)

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
            print("The " + x + " cars available in black are:")
            black_nissan_list = ['Nissan altima','Nissan pathfinder','Nissan GT-R','']
            for item in black_nissan_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_nissan_altima = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Fuel efficiency : Good','Infotainment : Central infotainment system with a touchscreen display','               Bluetooth connectivity','Safety : Automatic emergency braking','         Foward collision warning','         Lane departure warning','         Multiple airbags','         Rearview camera for improved visibility when reversing','Interior : Comfortable seating for both front and rear passengers','           Available power-adkustable driver seat','           Dual-zone automatic climate control in some models','Design : Interior with attention to comfort and practicality','Perfomance : Smooth ride and handling characteristics','             Enhanced performance features','Connectivity : USB ports','               Keyless entry and push-button start in some models','']
            black_nissan_pathfinder = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged V6','Drive type : Front-Wheel Drive(FWD)','Infotainment : Central infotainment system with a touchscreen display','Connectivity : Bluetooth','               Smartphone intergration','Safety : Automatic emergency braking','         Foward collision warning','         Blind-spot monitoring','         Multiple airbags','         Rearview camera for improved reversing','Interior : Spacious interior with three rows of seating','           Adjustable seating configurations for flexibity in cargo','Available power-adjustable driver seat and heated seats','Design : A mix of ruggedness and modern styling','         Roofrails for additional cargo carrying capability','Perfomance : Smooth ride and handling characteristics','             Towing capacity suitable for towing trailers or boats','Off-road features','']
            black_nissan_gt_r = ['','Color : black','Year : 2019','Engine : Twin-turbocharged V6 with high horsepower and torque','Drive type : All-Wheel Drive system','Transmission : Dual-clutch automatic transmission with manual mode','Performance : Adjustable performance settings for the engine','Aerodynamics : Design with features such spoiler and front splitter for improved stability at high speeds','Infotainment : Central infotainment system with a touchscreen display','Interior : Sport-oriented interior with supportive seats','           Driver-focused cockpit with a multifunctional display providing performance data','Safety : Multiple airbags','         Traction control','         Stability control','Design : Iconic and aggressive exterior styling','         Lightweight and high-strength materials','Track performance : Including cooling systems for brakes','']
            if z == 'Nissan altima':
                for item in black_nissan_altima:
                    print(item)
            if z == 'Nissan pathfinder':
                for item in black_nissan_pathfinder:
                    print(item)
            if z == 'Nissan GT-R':
                for item in black_nissan_gt_r:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in white are: ")
            white_nissan_list = ['Nissan sentra','Nissan versa','Nissan Pathfinder','Nissan armada','Nissan rogue','Nissan Maxima','']
            for item in white_nissan_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_nissan_sentra = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Infotainment : Central touchscreen infotainment system','             Bluetooth connectivity','             Smartphone intergration','Safety : Automatic emergency braking','         Foward collision warning','         Lane departure warning','         Multiple airbags for occupant protection','         Rearview camera for improved visibity when reversing','Interior : Comfortable seating for front and rear passengers','           Available power-adjustable driver seat','           Dual-zone automatic climate control in some models','Design : Modern streamlined exterior design','         LED highlights and taillights for improved visibility','Performance : Balanced ride and handling characteristics suitable for daily commuting','Connectivity : USB ports','Convinience : Keyless entry and push-button start in some models','Fuel efficiency : Making cost effective choice for daily commuting','Driver assistance features : Blind-spot monitoringand rear cross-traffic alert may be available','']
            white_nissan_versa = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Drive type : Front-Wheel drive configuration','Infotainment : Central touchscreen infotainment system','             Bluetooth connectivity','             Smartphone intergration','Safety : Automatic emergency braking','          Foward collision warning','          Lane departure warning','          Multiple airbags','          Rearview camera','Interior : Comfortable seating for front and rear passengers','            Available power-adjustable driver seat','            Air conditioning or climate control','Design : LED headlights and taillights','Performance : Balanced ride and handling characteristics','Connectivity : USB ports','Fuel efficiency : Economical choice for daily commuting','Cargo space : Decent amount of space','']
            white_nissan_pathfinder = ['','Color : White','Year : 2018','Engine : 2.0-liter turbocharged V6','Drive type : Front-Wheel Drive(FWD)','Infotainment : Central infotainment system with a touchscreen display','Connectivity : Bluetooth','               Smartphone intergration','Safety : Automatic emergency braking','         Foward collision warning','         Blind-spot monitoring','         Multiple airbags','         Rearview camera for improved reversing','Interior : Spacious interior with three rows of seating','           Adjustable seating configurations for flexibity in cargo','Available power-adjustable driver seat and heated seats','Design : A mix of ruggedness and modern styling','         Roofrails for additional cargo carrying capability','Perfomance : Smooth ride and handling characteristics','             Towing capacity suitable for towing trailers or boats','Off-road features','']
            white_nissan_armada = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','Space : Three-row seating for seven or eight passengers','safety : Foward collision warning','         Automatic emergency braking','         Blind-spot monitoring','Infotainment : Touchscreen display','               Smartphone intergration','               Navigation system','Towing capability : Suitable for towing trailers and boats','Luxury : Premium leather upholstery','         Heated and ventilated seats','         Advanced technology options','Off-road capability : Four-wheel drive,                      off-road modes','                      Robust suspension system','']
            white_nissan_rogue = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','         Fuel efficient','         Offer a good balance of power and fuel economy','Interior : Comfortable and versatile interior','           Three-row seating for seven passengers','Safety : Foward collision warning','         Automatic emergency braking','         Blind-spot monitoring','         Rear cross-traffic alert','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Cargo space : Foldable rear seats','Comfort : Power-adjustable driver seat','          Heated front seats','          Dual-zone climate control','          Panoramic sunroof','Fuel efficiency : Practical choice for those seeking good gas mileage in an SUV','AWD : For improved stability and traction control','']
            white_nissan_maxima = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged V6','Sporty design : A distinctive grille design and sleek lines','Interior : Comfortable seating','           Leather upholstery','           Power-adjustable seats','           Premium audio system','Safety : Collision warning','         Automatic emergency braking','         Blind-spot monitoring','Infotainment : Touchscreen display','             Smartphone intergration','             Navigation options','             Bluetooth connectivity','Driver assistance system : Adaptive cruise control','Performance-tuned suspension : For enhanced handling and provide more engaging deriver experience','Dual-panel panoramic moonroof : Open and airy feel','Intelligent trace control and active ride control','']
            if z == 'Nissan sentra':
                for item in white_nissan_sentra:
                    print(item)
            if z == 'Nissan versa':
                for item in white_nissan_versa:
                    print(item)
            if z == 'Nissan pathfinder':
                for item in white_nissan_pathfinder:
                    print(item)
            if z == 'Nissan armada':
                for item in white_nissan_armada:
                    print(item)
            if z == 'Nissan rogue':
                for item in white_nissan_rogue:
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
            print("The " + x + " cars available in black are:")
            black_audi_list = ['Audi A3','Audi A4','Audi A5','Audi A6','Audi A7','Audi Q2','Audi Q3','']
            for item in black_audi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_audi_a3 = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows the driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver-assistance system : Adaptive cruise control','                           Lnae departure warning','                           Automatic emergency braking','Panoramic sunroof : Available','Audi drive select : Adjust parameters such as steering feel,                    throttle response and suspension','Bang and olufsen premium sound system : Enhhanced audio experience','Connectivity : USB ports','']
            black_audi_a4 = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            black_audi_a5 = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            black_audi_a6 = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            black_audi_a7 = ['','Color : black','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            black_audi_q2 = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            black_audi_q3 = ['','Color : black','Year : 2022','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            if z == 'Audi A3':
                for item in black_audi_a3:
                    print(item)
            if z == 'Audi A4':
                for item in black_audi_a4:
                    print(item)
            if z == 'Audi A5':
                for item in black_audi_a5:
                    print(item)
            if z == 'Audi A6':
                for item in black_audi_a6:
                    print(item)
            if z == 'Audi A7':
                for item in black_audi_a7:
                    print(item)
            if z == 'Audi Q2':
                for item in black_audi_q2:
                    print(item)
            if z == 'Audi Q3':
                for item in black_audi_q3:
                    print(item)

        if y == 'blue':
            print("The " + x + " cars availablein blue are: ")
            blue_audi_list = ['Audi A3','Audi A4','Audi A5','Audi A7','Audi Q2','Audi Q3','']
            for item in blue_audi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_audi_a3 = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows the driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver-assistance system : Adaptive cruise control','                           Lnae departure warning','                           Automatic emergency braking','Panoramic sunroof : Available','Audi drive select : Adjust parameters such as steering feel,                    throttle response and suspension','Bang and olufsen premium sound system : Enhhanced audio experience','Connectivity : USB ports','']
            blue_audi_a4 = ['','Color : Blue','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            blue_audi_a5 = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            blue_audi_a7 = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            blue_audi_q2 = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            blue_audi_q3 = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            if z == 'Audi A3':
                for item in blue_audi_a3:
                    print(item)
            if z == 'Audi A4':
                for item in blue_audi_a4:
                    print(item)
            if z == 'Audi A5':
                for item in blue_audi_a5:
                    print(item)
            if z == 'Audi A7':
                for item in blue_audi_a7:
                    print(item)
            if z == 'Audi Q2':
                for item in blue_audi_q2:
                    print(item)
            if z == 'Audi Q3':
                for item in blue_audi_q3:
                    print(item)

        if y == 'maroon':
            print("The " + x + " cars available in maroon are: ")
            maroon_audi_list = ['Audi A5','Audi A7','Audi Q2','Audi Q3','']
            for item in maroon_audi_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            maroon_audi_a5 = ['','Color : Maroon','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            maroon_audi_a7 = ['','Color : Maroon','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Virtual cockpit : Allows driver to customize and view information in a high resolution display','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance systems : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Leather upholstery : For enhanced luxurious feel','Sunroof : For enhanced driver experience','Audi drive select : Select differnt driving modes','                    Adjusting parameters such as steering feel,throttle response','                    Suspension settings to suit different driving conditions','Bang and olufsen premium sound system : Enhanced audio experience','Connectivity : Bluetooth','               USB ports','               Smartphone intergration','Comfort : Power-adjustable seats','           Three-zone automatic climate control','           Ambient interior lighting','']
            maroon_audi_q2 = ['','Color : Maroon','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            maroon_audi_q3 = ['','Color : Maroon','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Quattro All-Wheel Drive : Enhanced traction and stability','Design : Compact size , suitable for urban environments','         Signature audi grille and modern aesthetics','MMI infotainment system : Central touchscreen display','                          Rotary controller','                          Smartphone intergration','                          Navigation system','Driver assistance system : Adaptive cruise control','                           Lane departure warning','                           Automatic emergency braking','Virtual cockpit : Provides customizable information and graphics','Premium interior material : Leather upholstery','Compact size and versatile interior : Flexible seating arrangements','Panoramic sunroof : Enhanced openness','Connectivity : USB ports','Dynamic Drive Select : Allow driver to choose different driving modes','Parking assistance : Rearview mirror','                     Semi-automated parking assistance','']
            if z == 'Audi A5':
                for item in maroon_audi_a5:
                    print(item)
            if z == 'Audi A7':
                for item in maroon_audi_a7:
                    print(item)
            if z == 'Audi Q2':
                for item in maroon_audi_q2:
                    print(item)
            if z == 'Audi Q3':
                for item in maroon_audi_q3:
                    print(item)

    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Audi:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")

#list containing the colors the model is available in
Honda = ['black','white','red','blue']
if x == 'Honda':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Honda:
        if y == 'black':
            print("The " + x + " cars available in black are:")
            black_honda_list = ['Honda Civic','Honda Accord','Honda HR-V','Honda CR-V','Honda Passport','Honda Pilot','Honda Odyssey','Honda Ridgeline','Honda Insight','']
            for item in black_honda_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_honda_civic = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Honda sensing suite : suite of safety and driver assistance features','Infotainment : Central screen display','Connectivity : Bluetooth','               Smartphone intergration','               USB ports','Multi-angle rearview camera : Parking assist','Comfort : Quality interior material','          Premium leather upholstery','          Power-adjustable seats','Eco assist system : Optimize fuel efficiency by providing feedback on driving habits','Hondalink connectivity : A suite of connected services,including remote start and vehicle tracking','Advanced Compatibility Engineering body structure : Enhance occupant protection and crash compatibility in frontal collisions','Lanewatch : Uses camera to display the passenger-side blind-spot on the central screen when the right turn signal is activated','Power moonroof : Open and airy cabin feel','Dual-zone automatic climate control : Personalized comfort','']
            black_honda_accord = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission','Infotainment : Modern with a touchscreen display','               Smartphone intergration','               Bluetooth connectivity','               Navigation system','Safety : Foward collision warning system','         Automatic emergency braking','         Lane departure warning','         Adaptive cruise control','Interior : Dual-zone automatic climate control','Advanced driver assistance system : Adaptive cruise control','Keyless entry and ignition : For convinience','Exterior : LED headlights','           Stylish alloy wheels','           Daytime running lights','Fuel efficiency : Suitable for a range of driving conditions','']
            black_honda_hr_v = ['','Color : White','Year : 2020','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','']
            black_honda_cr_v = ['','Color : black','Year : 2019','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','Smart entry and push-button start : For convinience','']
            black_honda_passport = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged V6','Transmission : Responsive automatic transmission','All-Wheel drive : Enhanced traction and stability','Infotainment : Touchscreen','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking','Power-adjustable seats : Enhanced comfort','Tri-zone automatic climate control : Personalised climate settings','Leather-trimmed seats : More luxurious feel','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Smart entry and push-button start : Allowing key-less access','Roof rails : Additional cargo-carrying options','LED lighting : Improved visibility','Hill start assist : Prevent rollback when starting on a hill','']
            black_honda_pilot = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Three-row seating : Suitable for larger families','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibility','Honda sensing suite : For advanced safety features','Tri-zone automatic climate control : Allow personalized climate settings for the driver','Power-adjustable seats : Enhanced comfort','Rear entertainment system : With a DVD to provide entertainment for rear passengers','Power tailgate : Easier access to cargo area','All-Wheel drive : Enhanced traction and stability','Blind-spot monitoring : Enhance awareness of surrounding traffic','Cross traffic monitor : Alert driver on approaching traffic from the side when backing out of parking spaces','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Wireless phone charging : Available for compatible smartphones','Hill start assist : Prevent rollback when starting on a hill','']
            black_honda_odyssey = ['','Color : black','Year : 2018','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Interior : Roomy flexible interior for upto eight passengers','Magic-slide second-row seats : Allows the second-row seats to be easily reconfigured for optimal flexibility','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibilitywhile parking or reversing','Honda sensing suite : For advanced safety featutres','Tri-zone automatic climate control : Allowing personalized climate settings for a driver and passengers','Power-adjustable seats : Enhanced comfort','Leather trimmed seats : Comfortable interior','Rear entertainment system : With a DVD for entertainment for rear passengers','Power sliding doors : Convinient entry and exit','Hands-free power tailgate : Easy access to cargo area','Vacuum cleaner : Easy to  clean messes','Bluetooth handsfreelink and streaming audio','Cabinwatch and cabintalk : Allow the driver to see rear seats through camera','']
            black_honda_ridgeline = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged V6','All-Wheel drive : Enhanced traction and stability','In-bed trunk : Beneath the bed floor for secure storage and can also be an ice chest','Dual-action tailgate : Can swing down or open sideways providing easier access to the bed','Truck-bed lights : Facilitate visibility and usability','Intergrated trailer hitch : Making towing more convinient','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               Smartphone intergration','Tri-zone automatic climate control : Allow personalized climate settings','Leather trimmed seats : More upscale and comfortable interior','Honda sensing suite : Advanced safety features','Power-adjustable seats : Enhanced comfort','Rearview camera : Improved visibility while parking or reversing','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow driver to start the engine from a distance for pre-heating or cooling the interior','Hill start assist : Prevent rollback when starting on a hill','Collision mitigation braking system : Bring the vehicle to stop when an unavoidable collision is detected','']
            black_honda_insight = ['','Color : black','Year : 2020','Hybrid powertrain : Combning a gasoline engine with an electric motor to optimize fuel efficiency','Three driving modes : EV mode for electric-only driving at low speeds','                      Hybrid mode for normal driving conditions','                      ECON mode for maximizing fuel efficiency','Regenerative braking : To capture and covert kinetic energy back to electric energy enhancing overall efficiency','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Lanewatch : Camera mounted on passengers-side mirror for a live feed when the right turn signal is activated','Smart entry and push-button start','Dual-zone automatic climate control : Personalized comfort','Leather trimmed seats : Comfortable interior','Power-adjustable seats : Enhanced comfort','LED lighting : Improved visibility','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Collision mitigation braking system : Bring the vehicle to a stop when an unavoidable collision is detected','']
            if z == 'Honda Civic':
                for item in black_honda_civic:
                    print(item)
            if z == 'Honda Accord':
                for item in black_honda_accord:
                    print(item)
            if z == 'Honda HR-V':
                for item in black_honda_hr_v:
                    print(item)
            if z == 'Honda CR-V':
                for item in black_honda_cr_v:
                    print(item)
            if z == 'Honda Passport':
                for item in black_honda_passport:
                    print(item)
            if z == 'Honda Pilot':
                for item in black_honda_pilot:
                    print(item)
            if z == 'Honda Odyssey':
                for item in black_honda_odyssey:
                    print(item)
            if z == 'Honda Ridgeline':
                for item in black_honda_ridgeline:
                    print(item)
            if z == 'Honda Insight':
                for item in black_honda_insight:
                    print(item)

        if y == 'white':
            print("The " + x + " cars availablein blue are: ")
            blue_honda_list = ['Honda Civic','Honda Accord','Honda HR-V','Honda CR-V','Honda Passport','Honda Pilot','Honda Odyssey','Honda Ridgeline','Honda Insight','']
            for item in blue_honda_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_honda_civic = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Honda sensing suite : suite of safety and driver assistance features','Infotainment : Central screen display','Connectivity : Bluetooth','               Smartphone intergration','               USB ports','Multi-angle rearview camera : Parking assist','Comfort : Quality interior material','          Premium leather upholstery','          Power-adjustable seats','Eco assist system : Optimize fuel efficiency by providing feedback on driving habits','Hondalink connectivity : A suite of connected services,including remote start and vehicle tracking','Advanced Compatibility Engineering body structure : Enhance occupant protection and crash compatibility in frontal collisions','Lanewatch : Uses camera to display the passenger-side blind-spot on the central screen when the right turn signal is activated','Power moonroof : Open and airy cabin feel','Dual-zone automatic climate control : Personalized comfort','']
            white_honda_accord = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission','Infotainment : Modern with a touchscreen display','               Smartphone intergration','               Bluetooth connectivity','               Navigation system','Safety : Foward collision warning system','         Automatic emergency braking','         Lane departure warning','         Adaptive cruise control','Interior : Dual-zone automatic climate control','Advanced driver assistance system : Adaptive cruise control','Keyless entry and ignition : For convinience','Exterior : LED headlights','           Stylish alloy wheels','           Daytime running lights','Fuel efficiency : Suitable for a range of driving conditions','']
            white_honda_hr_v = ['','Color : White','Year : 2020','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','']
            white_honda_cr_v = ['','Color : White','Year : 2019','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','Smart entry and push-button start : For convinience','']
            white_honda_passport = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged V6','Transmission : Responsive automatic transmission','All-Wheel drive : Enhanced traction and stability','Infotainment : Touchscreen','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking','Power-adjustable seats : Enhanced comfort','Tri-zone automatic climate control : Personalised climate settings','Leather-trimmed seats : More luxurious feel','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Smart entry and push-button start : Allowing key-less access','Roof rails : Additional cargo-carrying options','LED lighting : Improved visibility','Hill start assist : Prevent rollback when starting on a hill','']
            white_honda_pilot = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Three-row seating : Suitable for larger families','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibility','Honda sensing suite : For advanced safety features','Tri-zone automatic climate control : Allow personalized climate settings for the driver','Power-adjustable seats : Enhanced comfort','Rear entertainment system : With a DVD to provide entertainment for rear passengers','Power tailgate : Easier access to cargo area','All-Wheel drive : Enhanced traction and stability','Blind-spot monitoring : Enhance awareness of surrounding traffic','Cross traffic monitor : Alert driver on approaching traffic from the side when backing out of parking spaces','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Wireless phone charging : Available for compatible smartphones','Hill start assist : Prevent rollback when starting on a hill','']
            white_honda_odyssey = ['','Color : White','Year : 2018','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Interior : Roomy flexible interior for upto eight passengers','Magic-slide second-row seats : Allows the second-row seats to be easily reconfigured for optimal flexibility','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibilitywhile parking or reversing','Honda sensing suite : For advanced safety featutres','Tri-zone automatic climate control : Allowing personalized climate settings for a driver and passengers','Power-adjustable seats : Enhanced comfort','Leather trimmed seats : Comfortable interior','Rear entertainment system : With a DVD for entertainment for rear passengers','Power sliding doors : Convinient entry and exit','Hands-free power tailgate : Easy access to cargo area','Vacuum cleaner : Easy to  clean messes','Bluetooth handsfreelink and streaming audio','Cabinwatch and cabintalk : Allow the driver to see rear seats through camera','']
            white_honda_ridgeline = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','All-Wheel drive : Enhanced traction and stability','In-bed trunk : Beneath the bed floor for secure storage and can also be an ice chest','Dual-action tailgate : Can swing down or open sideways providing easier access to the bed','Truck-bed lights : Facilitate visibility and usability','Intergrated trailer hitch : Making towing more convinient','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               Smartphone intergration','Tri-zone automatic climate control : Allow personalized climate settings','Leather trimmed seats : More upscale and comfortable interior','Honda sensing suite : Advanced safety features','Power-adjustable seats : Enhanced comfort','Rearview camera : Improved visibility while parking or reversing','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow driver to start the engine from a distance for pre-heating or cooling the interior','Hill start assist : Prevent rollback when starting on a hill','Collision mitigation braking system : Bring the vehicle to stop when an unavoidable collision is detected','']
            white_honda_insight = ['','Color : White','Year : 2020','Hybrid powertrain : Combning a gasoline engine with an electric motor to optimize fuel efficiency','Three driving modes : EV mode for electric-only driving at low speeds','                      Hybrid mode for normal driving conditions','                      ECON mode for maximizing fuel efficiency','Regenerative braking : To capture and covert kinetic energy back to electric energy enhancing overall efficiency','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Lanewatch : Camera mounted on passengers-side mirror for a live feed when the right turn signal is activated','Smart entry and push-button start','Dual-zone automatic climate control : Personalized comfort','Leather trimmed seats : Comfortable interior','Power-adjustable seats : Enhanced comfort','LED lighting : Improved visibility','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Collision mitigation braking system : Bring the vehicle to a stop when an unavoidable collision is detected','']
            if z == 'Honda Civic':
                for item in white_honda_civic:
                    print(item)
            if z == 'Honda Accord':
                for item in white_honda_accord:
                    print(item)
            if z == 'Honda HR-V':
                for item in white_honda_hr_v:
                    print(item)
            if z == 'Honda CR-V':
                for item in white_honda_cr_v:
                    print(item)
            if z == 'Honda Passport':
                for item in white_honda_passport:
                    print(item)
            if z == 'Honda Pilot':
                for item in white_honda_pilot:
                    print(item)
            if z == 'Honda Odyssey':
                for item in white_honda_odyssey:
                    print(item)
            if z == 'Honda Ridgeline':
                for item in white_honda_ridgeline:
                    print(item)
            if z == 'Honda Insight':
                for item in white_honda_insight:
                    print(item)

        if y == 'red':
            print("The " + x + " cars available in maroon are: ")
            maroon_honda_list = ['Honda Civic','Honda Accord','Honda HR-V','Honda CR-V','Honda Pilot','Honda Ridgeline','Honda Insight','']
            for item in maroon_honda_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            red_honda_civic = ['','Color : Red','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Honda sensing suite : suite of safety and driver assistance features','Infotainment : Central screen display','Connectivity : Bluetooth','               Smartphone intergration','               USB ports','Multi-angle rearview camera : Parking assist','Comfort : Quality interior material','          Premium leather upholstery','          Power-adjustable seats','Eco assist system : Optimize fuel efficiency by providing feedback on driving habits','Hondalink connectivity : A suite of connected services,including remote start and vehicle tracking','Advanced Compatibility Engineering body structure : Enhance occupant protection and crash compatibility in frontal collisions','Lanewatch : Uses camera to display the passenger-side blind-spot on the central screen when the right turn signal is activated','Power moonroof : Open and airy cabin feel','Dual-zone automatic climate control : Personalized comfort','']
            red_honda_accord = ['','Color : Red','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission','Infotainment : Modern with a touchscreen display','               Smartphone intergration','               Bluetooth connectivity','               Navigation system','Safety : Foward collision warning system','         Automatic emergency braking','         Lane departure warning','         Adaptive cruise control','Interior : Dual-zone automatic climate control','Advanced driver assistance system : Adaptive cruise control','Keyless entry and ignition : For convinience','Exterior : LED headlights','           Stylish alloy wheels','           Daytime running lights','Fuel efficiency : Suitable for a range of driving conditions','']
            red_honda_hr_v = ['','Color : Red','Year : 2020','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','']
            red_honda_cr_v = ['','Color : Red','Year : 2019','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','Smart entry and push-button start : For convinience','']
            red_honda_pilot = ['','Color : Red','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Three-row seating : Suitable for larger families','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibility','Honda sensing suite : For advanced safety features','Tri-zone automatic climate control : Allow personalized climate settings for the driver','Power-adjustable seats : Enhanced comfort','Rear entertainment system : With a DVD to provide entertainment for rear passengers','Power tailgate : Easier access to cargo area','All-Wheel drive : Enhanced traction and stability','Blind-spot monitoring : Enhance awareness of surrounding traffic','Cross traffic monitor : Alert driver on approaching traffic from the side when backing out of parking spaces','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Wireless phone charging : Available for compatible smartphones','Hill start assist : Prevent rollback when starting on a hill','']
            red_honda_ridgeline = ['','Color : Red','Year : 2019','Engine : 2.0-liter turbocharged V6','All-Wheel drive : Enhanced traction and stability','In-bed trunk : Beneath the bed floor for secure storage and can also be an ice chest','Dual-action tailgate : Can swing down or open sideways providing easier access to the bed','Truck-bed lights : Facilitate visibility and usability','Intergrated trailer hitch : Making towing more convinient','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               Smartphone intergration','Tri-zone automatic climate control : Allow personalized climate settings','Leather trimmed seats : More upscale and comfortable interior','Honda sensing suite : Advanced safety features','Power-adjustable seats : Enhanced comfort','Rearview camera : Improved visibility while parking or reversing','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow driver to start the engine from a distance for pre-heating or cooling the interior','Hill start assist : Prevent rollback when starting on a hill','Collision mitigation braking system : Bring the vehicle to stop when an unavoidable collision is detected','']
            red_honda_insight = ['','Color : Red','Year : 2020','Hybrid powertrain : Combning a gasoline engine with an electric motor to optimize fuel efficiency','Three driving modes : EV mode for electric-only driving at low speeds','                      Hybrid mode for normal driving conditions','                      ECON mode for maximizing fuel efficiency','Regenerative braking : To capture and covert kinetic energy back to electric energy enhancing overall efficiency','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Lanewatch : Camera mounted on passengers-side mirror for a live feed when the right turn signal is activated','Smart entry and push-button start','Dual-zone automatic climate control : Personalized comfort','Leather trimmed seats : Comfortable interior','Power-adjustable seats : Enhanced comfort','LED lighting : Improved visibility','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Collision mitigation braking system : Bring the vehicle to a stop when an unavoidable collision is detected','']
            if z == 'Honda Civic':
                for item in red_honda_civic:
                    print(item)
            if z == 'Honda Accord':
                for item in red_honda_accord:
                    print(item)
            if z == 'Honda HR-V':
                for item in red_honda_hr_v:
                    print(item)
            if z == 'Honda CR-V':
                for item in red_honda_cr_v:
                    print(item)
            if z == 'Honda Pilot':
                for item in red_honda_pilot:
                    print(item)
            if z == 'Honda Ridgeline':
                for item in red_honda_ridgeline:
                    print(item)
            if z == 'Honda Insight':
                for item in red_honda_insight:
                    print(item)

        if y == 'blue':
            print("The " + x + " cars available in maroon are: ")
            maroon_honda_list = ['Honda Civic','Honda Accord','Honda HR-V','Honda CR-V','Honda Pilot','Honda Ridgeline','Honda Insight','Honda Fit','']
            for item in maroon_honda_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_honda_civic = ['','Color : Blue','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission','Honda sensing suite : suite of safety and driver assistance features','Infotainment : Central screen display','Connectivity : Bluetooth','               Smartphone intergration','               USB ports','Multi-angle rearview camera : Parking assist','Comfort : Quality interior material','          Premium leather upholstery','          Power-adjustable seats','Eco assist system : Optimize fuel efficiency by providing feedback on driving habits','Hondalink connectivity : A suite of connected services,including remote start and vehicle tracking','Advanced Compatibility Engineering body structure : Enhance occupant protection and crash compatibility in frontal collisions','Lanewatch : Uses camera to display the passenger-side blind-spot on the central screen when the right turn signal is activated','Power moonroof : Open and airy cabin feel','Dual-zone automatic climate control : Personalized comfort','']
            blue_honda_accord = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Transmission : Continously variable transmission','Infotainment : Modern with a touchscreen display','               Smartphone intergration','               Bluetooth connectivity','               Navigation system','Safety : Foward collision warning system','         Automatic emergency braking','         Lane departure warning','         Adaptive cruise control','Interior : Dual-zone automatic climate control','Advanced driver assistance system : Adaptive cruise control','Keyless entry and ignition : For convinience','Exterior : LED headlights','           Stylish alloy wheels','           Daytime running lights','Fuel efficiency : Suitable for a range of driving conditions','']
            blue_honda_hr_v = ['','Color : Blue','Year : 2020','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','']
            blue_honda_cr_v = ['','Color : Blue','Year : 2019','Engine :2.0-liter turbocharged inline-4','Continously variable transmission : For smooth and efficient power delivery','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Suite of advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Dual-zone automatic climate control : For personalized comfort for the driver and front passenger','Power-adjustable seats : Enhanced comfort','Leather upholstery : For more luxurious feel','Panoramic sunroof : For ventilation','Hands-free power tailgate : For easy access to cargo area','Remote engine start : Start the engine from a distance for pre-heating or cooling the interior','Blind spot monitoring : Enhance awareness of surrounding traffic','Wireless charging : For compatible smartphones','LED lighting : Improved visibility','All-Wheel drive : Stability and traction','Smart entry and push-button start : For convinience','']
            blue_honda_pilot = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Three-row seating : Suitable for larger families','Infotainment : Bluetooth connectivity','               USB ports','               Smartphone intergration','Rearview camera : Improved visibility','Honda sensing suite : For advanced safety features','Tri-zone automatic climate control : Allow personalized climate settings for the driver','Power-adjustable seats : Enhanced comfort','Rear entertainment system : With a DVD to provide entertainment for rear passengers','Power tailgate : Easier access to cargo area','All-Wheel drive : Enhanced traction and stability','Blind-spot monitoring : Enhance awareness of surrounding traffic','Cross traffic monitor : Alert driver on approaching traffic from the side when backing out of parking spaces','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Bluetooth handsfreelink and streaming audio','Wireless phone charging : Available for compatible smartphones','Hill start assist : Prevent rollback when starting on a hill','']
            blue_honda_ridgeline = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged V6','All-Wheel drive : Enhanced traction and stability','In-bed trunk : Beneath the bed floor for secure storage and can also be an ice chest','Dual-action tailgate : Can swing down or open sideways providing easier access to the bed','Truck-bed lights : Facilitate visibility and usability','Intergrated trailer hitch : Making towing more convinient','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               Smartphone intergration','Tri-zone automatic climate control : Allow personalized climate settings','Leather trimmed seats : More upscale and comfortable interior','Honda sensing suite : Advanced safety features','Power-adjustable seats : Enhanced comfort','Rearview camera : Improved visibility while parking or reversing','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow driver to start the engine from a distance for pre-heating or cooling the interior','Hill start assist : Prevent rollback when starting on a hill','Collision mitigation braking system : Bring the vehicle to stop when an unavoidable collision is detected','']
            blue_honda_insight = ['','Color : Blue','Year : 2020','Hybrid powertrain : Combning a gasoline engine with an electric motor to optimize fuel efficiency','Three driving modes : EV mode for electric-only driving at low speeds','                      Hybrid mode for normal driving conditions','                      ECON mode for maximizing fuel efficiency','Regenerative braking : To capture and covert kinetic energy back to electric energy enhancing overall efficiency','Infotainment : Touchscreen infotainment system','               Bluetooth connectivity','               USB ports','               Smartphone intergration','Honda sensing suite : Advanced safety features','Multi-angle rearview camera : Improved visibility while parking or reversing','Lanewatch : Camera mounted on passengers-side mirror for a live feed when the right turn signal is activated','Smart entry and push-button start','Dual-zone automatic climate control : Personalized comfort','Leather trimmed seats : Comfortable interior','Power-adjustable seats : Enhanced comfort','LED lighting : Improved visibility','Bluetooth handsfreelink and streaming audio','Remote engine start : Allow the driver to start the engine from a distance for pre-heating or cooling the interior','Collision mitigation braking system : Bring the vehicle to a stop when an unavoidable collision is detected','']
            blue_honda_fit = ['','Color : Blue','Year : 2018','Engine : 2.0-liter turbocharged inline-4','Compact size : Designed for urban driving and easy maneuverability','Magic seat : Foldable rear seats','Fuel efficiency : Economical choice for fuel saving','Infotainment : Touchscreen display','               Bluetooth connectivity','               Smartphone intergration','Safety : Airbag system','         Anti-lock brakes','         Stability control','         Driver-assistance technologiies','Spacious interior : Ample room for passengers and cargo','Maneuverability : Nimble handling and easy maneuverability suitable for city driving and parkung in tight spaces','Versatile storage : Storage compartment and cupholders throught the cabin to enhance practicality','Reliability : Regular maintenance and adherence to recommended service intervals contribute to longevity of the vehicle','']
            if z == 'Honda Civic':
                for item in blue_honda_civic:
                    print(item)
            if z == 'Honda Accord':
                for item in blue_honda_accord:
                    print(item)
            if z == 'Honda HR-V':
                for item in blue_honda_hr_v:
                    print(item)
            if z == 'Honda CR-V':
                for item in blue_honda_cr_v:
                    print(item)
            if z == 'Honda Pilot':
                for item in blue_honda_pilot:
                    print(item)
            if z == 'Honda Ridgeline':
                for item in blue_honda_ridgeline:
                    print(item)
            if z == 'Honda Insight':
                for item in blue_honda_insight:
                    print(item)
            if z == 'Honda Fit':
                for item in blue_honda_fit:
                    print(item)

    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Nissan:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")

#list containing the colors the model is available in
Subaru = ['black','white','blue']
if x == 'Subaru':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Subaru:
        if y == 'black':
            print("The " + x + " cars available in black are:")
            black_subaru_list = ['Subaru Impreza','Subaru Legacy','Subaru WRX','Subaru BRZ','Subaru Crosstrek','Subaru Forester','']
            for item in black_subaru_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_subaru_impreza = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Enhanced traction and stability','Boxer engine : Contributes to a lower center of gravity and improved balance','Safety : Rearview camera','         Traction control','         Stability control','         Subaru eyesight driver assist technology','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Spacious interior : Roomy interior for passengers and cargo','Subaru starlink : Multimedia system allows access to various entertainment navigation and safety features','Build quality : Durable material contributing to a solid and well-constructed vehicle','Transmission : Allowing drivers to choose based on their personal preferences','Fuel efficiency : Practical choice for daily commuting','Eyesight driver assist technology : Adaptive cruise control and other driver assist features','']
            black_subaru_legacy = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Provide enhanced traction and stability','Boxer engine : Contributing to a lower center of gravity and improved balance','Safety : Subaru eyesight driver assist','         Technology with adaptive cruise control','         Lane departure warning','         Lane-keeping assist','Infotainment : Touchscreen infotainment display','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Harman kardon audio system : Improved sound quality','Spacious interior : Foldable rear seats','Build quality : Quality material contribute to a solid and well-constructed sedan','CVT transmission : Continously variable transmission','Dual-zone automatic climate control : Maintain individual temperature preferences','Driver assistance features : Blind-spot monitoring','Fuel efficiency : Suitable for both highway cruising and city driving','']
            black_subaru_wrx = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Produces a distinctive engine sound','Symmetrical All-Wheel drive : Excellent traction and handling','Suspension : Sport-tuned for improved handling and more engaging driving experience','Performance : High-perfomance braking system provides high stopping power','Sport seats : Provide additional support and comfort during high perfomance driving','Sport-tuned exhaust system : Contributing to the distinctive exhaust note and perfomance feel','SI-Drive(Subaru Intelligent Drive) : Allows the driver to select different driving modes','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Perfomance-oriented wheels and tires : Enhanced grip and handling','Driver assistance features : Adaptive cruise control and other features','Subaru starlink : Proviide access to entertainment,navigation and connectivity features','Rearview camera : Assist in parking and maneuvering','']
            black_subaru_brz = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Provide a lower center of gravity for improved handling','Rear-Wheel drive : More performance-oriented drining experience','Sport-tuned suspension : Provide precise handling and a responsive feel on the road','Limited-slip differential : Enhanced traction and stability during aggressive driving and cornering','Lightweight design : Contributes to agility and nimble handling','Sport seats : Provide extra support during spirited driving','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Performance brakes : Strong stopping power during dynamic driving','Alloy wheels : Contribute to aesthetic and performance','Vehicle stability control : Maintain vehicle stability during challenging driving conditions','Track mode : Allow drivers to optimize performance for track or spirited driving','Keyless entry and push-button start : Added convinience','LED lighting : For both headlights and taillights for visibility','Subaru starlink : With various entertainment and connectivity options','']
            black_subaru_crosstrek = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Symmetrical All-Wheel drive : Enhanced traction and stability','Ground clearance : Suitable for light-off-road adventures and providing a commanding view of the road','Boxer engine : Lower center of gravity for improved stability and handling','X-mode : Enhanced off-road capability','Eyesight driver assist technology : Driver assistance features','Infotainment : Smartphone intergration','             Bluetooth connectivity','             Navigation system','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More carrgo space','Transmission : Continously variable transmission','Rearview camera : Assist in parking and maneuvering','High-strength ateel construction : Contribute to durability and safety','Key-less entry and push button start : Added convinience','Blind-spot detection and rear-cross traffic alert : Enhance awareness and safety','']
            black_subaru_forester = ['','Color : black','Year : 2019','Engine : 2.0-liter torbocharged inline-4','Symmetrical All-wheel drive : Enhanced stability and traction','Boxer engine : Lower center of gravity for improved stability and handling','X-mode : Optimizes the AWD system engine and transmission','Eyesight driver assist technology : Driver assistance features','Infotainment : Touchscraan infotainment system','             Smartphone intergration','             Navigation system','             Bluetooth connectivity','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More space for cargo','Power-adjustable drivers seat : Added comfort and convinience','Panoramic moonroof : For airy feel','Transmission : Continous variable transmission','Rearview camera : Assist with parking and maneuvering','Keyless entry and push-button start : Added convinience','High-strength steel construction : Enhanced durability and safety','Subaru global platform : Enhannces safety,driving dynamics and overall performance','']
            if z == 'Subaru Impreza':
                for item in black_subaru_impreza:
                    print(item)
            if z == 'Subaru Legacy':
                for item in black_subaru_legacy:
                    print(item)
            if z == 'Subaru WRX':
                for item in black_subaru_wrx:
                    print(item)
            if z == 'Subaru BRZ':
                for item in black_subaru_brz:
                    print(item)
            if z == 'Subaru Crosstrek':
                for item in black_subaru_crosstrek:
                    print(item)
            if z == 'Subaru Forester':
                for item in black_subaru_forester:
                    print(item)

        if y == 'white':
            print("The " + x + " cars available in blue are: ")
            blue_subaru_list = ['Subaru Impreza','Subaru Legacy','Subaru WRX','Subaru BRZ','Subaru Crosstrek','Subaru Forester','Subaru Outback','']
            for item in blue_subaru_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_subaru_impreza = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Enhanced traction and stability','Boxer engine : Contributes to a lower center of gravity and improved balance','Safety : Rearview camera','         Traction control','         Stability control','         Subaru eyesight driver assist technology','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Spacious interior : Roomy interior for passengers and cargo','Subaru starlink : Multimedia system allows access to various entertainment navigation and safety features','Build quality : Durable material contributing to a solid and well-constructed vehicle','Transmission : Allowing drivers to choose based on their personal preferences','Fuel efficiency : Practical choice for daily commuting','Eyesight driver assist technology : Adaptive cruise control and other driver assist features','']
            white_subaru_legacy = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Provide enhanced traction and stability','Boxer engine : Contributing to a lower center of gravity and improved balance','Safety : Subaru eyesight driver assist','         Technology with adaptive cruise control','         Lane departure warning','         Lane-keeping assist','Infotainment : Touchscreen infotainment display','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Harman kardon audio system : Improved sound quality','Spacious interior : Foldable rear seats','Build quality : Quality material contribute to a solid and well-constructed sedan','CVT transmission : Continously variable transmission','Dual-zone automatic climate control : Maintain individual temperature preferences','Driver assistance features : Blind-spot monitoring','Fuel efficiency : Suitable for both highway cruising and city driving','']
            white_subaru_wrx = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Produces a distinctive engine sound','Symmetrical All-Wheel drive : Excellent traction and handling','Suspension : Sport-tuned for improved handling and more engaging driving experience','Performance : High-perfomance braking system provides high stopping power','Sport seats : Provide additional support and comfort during high perfomance driving','Sport-tuned exhaust system : Contributing to the distinctive exhaust note and perfomance feel','SI-Drive(Subaru Intelligent Drive) : Allows the driver to select different driving modes','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Perfomance-oriented wheels and tires : Enhanced grip and handling','Driver assistance features : Adaptive cruise control and other features','Subaru starlink : Proviide access to entertainment,navigation and connectivity features','Rearview camera : Assist in parking and maneuvering','']
            white_subaru_brz = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Provide a lower center of gravity for improved handling','Rear-Wheel drive : More performance-oriented drining experience','Sport-tuned suspension : Provide precise handling and a responsive feel on the road','Limited-slip differential : Enhanced traction and stability during aggressive driving and cornering','Lightweight design : Contributes to agility and nimble handling','Sport seats : Provide extra support during spirited driving','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Performance brakes : Strong stopping power during dynamic driving','Alloy wheels : Contribute to aesthetic and performance','Vehicle stability control : Maintain vehicle stability during challenging driving conditions','Track mode : Allow drivers to optimize performance for track or spirited driving','Keyless entry and push-button start : Added convinience','LED lighting : For both headlights and taillights for visibility','Subaru starlink : With various entertainment and connectivity options','']
            white_subaru_crosstrek = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged inline-4','Symmetrical All-Wheel drive : Enhanced traction and stability','Ground clearance : Suitable for light-off-road adventures and providing a commanding view of the road','Boxer engine : Lower center of gravity for improved stability and handling','X-mode : Enhanced off-road capability','Eyesight driver assist technology : Driver assistance features','Infotainment : Smartphone intergration','             Bluetooth connectivity','             Navigation system','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More carrgo space','Transmission : Continously variable transmission','Rearview camera : Assist in parking and maneuvering','High-strength ateel construction : Contribute to durability and safety','Key-less entry and push button start : Added convinience','Blind-spot detection and rear-cross traffic alert : Enhance awareness and safety','']
            white_subaru_forester = ['','Color : White','Year : 2019','Engine : 2.0-liter torbocharged inline-4','Symmetrical All-wheel drive : Enhanced stability and traction','Boxer engine : Lower center of gravity for improved stability and handling','X-mode : Optimizes the AWD system engine and transmission','Eyesight driver assist technology : Driver assistance features','Infotainment : Touchscraan infotainment system','             Smartphone intergration','             Navigation system','             Bluetooth connectivity','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More space for cargo','Power-adjustable drivers seat : Added comfort and convinience','Panoramic moonroof : For airy feel','Transmission : Continous variable transmission','Rearview camera : Assist with parking and maneuvering','Keyless entry and push-button start : Added convinience','High-strength steel construction : Enhanced durability and safety','Subaru global platform : Enhannces safety,driving dynamics and overall performance','']
            white_subaru_outback = ['','Color : White','Year : 2021','Engine 2.0-liter turbocharged inline-4','Symmetrical All-Wheel drive : Enhanced traction and stability','Boxer engine : Lower the center of gravity for improved stability','X-mode : Optimizes the AWD system','Eyesight driver assist technology : Driver assistance features','Infotainment : Touchscreen infotainment system','             Smartphone intergaration','             Bluetooth connectivity','             Navigation system','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More cargo space','Power-adjustable driver seat : For comfort and convinience','Panoramic moonroof : Additional natural light','Transmission : Continous variable transmission','Rearview camera : Assist with parking and maneuvering','Keyless entry and push-button start : Added convinience','High-strength steel construction : Durability and safety','Ground clearance : Suitable for light-off-road adventures','']
            if z == 'Subaru Impreza':
                for item in white_subaru_impreza:
                    print(item)
            if z == 'Subaru Legacy':
                for item in white_subaru_legacy:
                    print(item)
            if z == 'Subaru WRX':
                for item in white_subaru_wrx:
                    print(item)
            if z == 'Subaru BRZ':
                for item in white_subaru_brz:
                    print(item)
            if z == 'Subaru Crosstrek':
                for item in white_subaru_crosstrek:
                    print(item)
            if z == 'Subaru Forester':
                for item in white_subaru_forester:
                    print(item)
            if z == 'Subaru Outback':
                for item in white_subaru_outback:
                    print(item)

        if y == 'blue':
            print("The " + x + " cars available in maroon are: ")
            maroon_subaru_list = ['Subaru Impreza','Subaru Legacy','Subaru WRX','Subaru BRZ','Subaru Forester','']
            for item in maroon_subaru_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            blue_subaru_impreza = ['','Color : Blue','Year : 2019','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Enhanced traction and stability','Boxer engine : Contributes to a lower center of gravity and improved balance','Safety : Rearview camera','         Traction control','         Stability control','         Subaru eyesight driver assist technology','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Spacious interior : Roomy interior for passengers and cargo','Subaru starlink : Multimedia system allows access to various entertainment navigation and safety features','Build quality : Durable material contributing to a solid and well-constructed vehicle','Transmission : Allowing drivers to choose based on their personal preferences','Fuel efficiency : Practical choice for daily commuting','Eyesight driver assist technology : Adaptive cruise control and other driver assist features','']
            blue_subaru_legacy = ['','Color : Blue','Year : 2020','Engine : 2.0-liter turbocharged inline-4','All-Wheel drive : Provide enhanced traction and stability','Boxer engine : Contributing to a lower center of gravity and improved balance','Safety : Subaru eyesight driver assist','         Technology with adaptive cruise control','         Lane departure warning','         Lane-keeping assist','Infotainment : Touchscreen infotainment display','             Smartphone intergration','             Bluetooth connectivity','             USB ports','Harman kardon audio system : Improved sound quality','Spacious interior : Foldable rear seats','Build quality : Quality material contribute to a solid and well-constructed sedan','CVT transmission : Continously variable transmission','Dual-zone automatic climate control : Maintain individual temperature preferences','Driver assistance features : Blind-spot monitoring','Fuel efficiency : Suitable for both highway cruising and city driving','']
            blue_subaru_wrx = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Produces a distinctive engine sound','Symmetrical All-Wheel drive : Excellent traction and handling','Suspension : Sport-tuned for improved handling and more engaging driving experience','Performance : High-perfomance braking system provides high stopping power','Sport seats : Provide additional support and comfort during high perfomance driving','Sport-tuned exhaust system : Contributing to the distinctive exhaust note and perfomance feel','SI-Drive(Subaru Intelligent Drive) : Allows the driver to select different driving modes','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Perfomance-oriented wheels and tires : Enhanced grip and handling','Driver assistance features : Adaptive cruise control and other features','Subaru starlink : Proviide access to entertainment,navigation and connectivity features','Rearview camera : Assist in parking and maneuvering','']
            blue_subaru_brz = ['','Color : Blue','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Boxer engine : Provide a lower center of gravity for improved handling','Rear-Wheel drive : More performance-oriented drining experience','Sport-tuned suspension : Provide precise handling and a responsive feel on the road','Limited-slip differential : Enhanced traction and stability during aggressive driving and cornering','Lightweight design : Contributes to agility and nimble handling','Sport seats : Provide extra support during spirited driving','Infotainment : Touchscreen infotainment system','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Performance brakes : Strong stopping power during dynamic driving','Alloy wheels : Contribute to aesthetic and performance','Vehicle stability control : Maintain vehicle stability during challenging driving conditions','Track mode : Allow drivers to optimize performance for track or spirited driving','Keyless entry and push-button start : Added convinience','LED lighting : For both headlights and taillights for visibility','Subaru starlink : With various entertainment and connectivity options','']
            blue_subaru_forester = ['','Color : Blue','Year : 2019','Engine : 2.0-liter torbocharged inline-4','Symmetrical All-wheel drive : Enhanced stability and traction','Boxer engine : Lower center of gravity for improved stability and handling','X-mode : Optimizes the AWD system engine and transmission','Eyesight driver assist technology : Driver assistance features','Infotainment : Touchscraan infotainment system','             Smartphone intergration','             Navigation system','             Bluetooth connectivity','Subaru starlink : Access to various entertainment,navigation and connectivity features','Spacious interior : Roomy interior for passengers and cargo','Roof rails : More space for cargo','Power-adjustable drivers seat : Added comfort and convinience','Panoramic moonroof : For airy feel','Transmission : Continous variable transmission','Rearview camera : Assist with parking and maneuvering','Keyless entry and push-button start : Added convinience','High-strength steel construction : Enhanced durability and safety','Subaru global platform : Enhannces safety,driving dynamics and overall performance','']
            if z == 'Subaru Impreza':
                for item in blue_subaru_impreza:
                    print(item)
            if z == 'Subaru Legacy':
                for item in blue_subaru_legacy:
                    print(item)
            if z == 'Subaru WRX':
                for item in blue_subaru_wrx:
                    print(item)
            if z == 'Subaru BRZ':
                for item in blue_subaru_brz:
                    print(item)
            if z == 'Subaru Forester':
                for item in blue_subaru_forester:
                    print(item)

    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Nissan:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view other makes available in that color")

#list containing the colors the model is available in
Chevrolet = ['black','white','silver']
if x == 'Chevrolet':
    #if the color entered is in the list the user can proceed to view the cars available
    if y in Chevrolet:
        if y == 'black':
            print("The " + x + " cars available in black are:")
            black_chevrolet_list = ['Chevrolet Spark','Chevrolet Sonic','Chevrolet Malibu','Chevrolet Camaro','Chevrolet Corvette','Chevrolet Silverado','Chevrolet Colorado','']
            for item in black_chevrolet_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            black_chevrolet_spark = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for city driving and parking in tight spaces','Fuel efficiency : Econimical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','City safety features : Safety features','Compact hatchback design : Versatile cargo space','Cost : Affordable','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Safety : Airbags','Onstar services : Provide emergency assistance,vehicle diagnostics and navigation','Compact spare tire : Backup','Fuel tank capacity : Small','Tire pressure monitoring system : Alert when pressure is low','Child safety seat anchores(LATCH) : Securing children','']
            black_chevrolet_sonic = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for urban driving and parking in tight spaces','Fuel efficiency : Economical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Available body styles : Flexibility for buyers who prefer different styles','Safety : Airbags','         Stability control','         Traction control','         Foward collision warning','Compact hatchback design : Additional cargo space','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Affordable price : Budget-friendly option','Onstar services : Offer emergency assistance,vehicle diagnostics and navigation','Rearview camera : Assist in parking and reversing','Tire pressure monitoring system : Alert when the pressure is low','Child safety seat anchors : Secure children','']
            black_chevrolet_malibu = ['','Color : black','Year : 2017','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission for smooth and efficient power delivery','Infotainment : Android auto compatibility','             Bluetooth connectivity','             Navigation system','             Voice recognition','Safety : Airbags','         Stability control','         Traction control','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Interior : Power-adjustable seats','           Leather upholstery','         Dual-zone automatic climate control','Advanced driver assistance features : Adaptive cruise control','Keyless entry and push-button start : Added convinience','Wireless charging : Available','Teen driver technology : Allow parents to set certain parameters and receive a report on their teens behavior','Onstar services : Offer emergency assistance,vehicle diagnostics and navigation','Spacious trunk : More cargo space','Fuel efficiency : Suitable for economical commuting','Sunroof : Available','Wheels : Alloy for aesthetic appeal and improved performance','']
            black_chevrolet_camaro = ['','Color : black','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Suspension : Sport-tuned suspension system','Brembo brakes : Provide superior stopping power','Magnetic ride control : Adjusts suspension damping in real time for improved handling and ride comfort','Driver modes : Allow the driver to customize performance settings based on driving conditions','Tires : High performance for enhanced grip and handling','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Wi-fi hotspot : Allow access to internet','Premium audio system : Enhanced listening experience','Performance exhaust system : Provides an aggressive engine sound','Head-up display : Project important information onto the windshield','Recaro performance seats : Additional support for performance-oriented driving','Driver assistance features','Convertible top : For airy cabin feel','']
            black_chevrolet_corvette = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged V8','Mid-engine configuration : Behing the driver for improved weight distribution and handling','Transmission : Automatic transmission with paddle shifters for  manual control of gear changes','Magnetic ride control : Adaptive suspension system that adjusts damping in real time for optimal performance','Performance exhaust system : Offer different driving modes and sound profiles to suit various driving conditions','Driver modes : Allow driver to customize performance settings','Tires : Contribute to grip and handling capabilities','Brembo brakes : Superior stopping power','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','High-resolution display : Providing customizable information and perfomance data','Wi-fi hotspot : Access to internet','Premium audio system : Enhanced listening experience','Carbon fiber components : Reduced weight and improved performance','Convertible top : Airy cabin feel','Driver assistance features','']
            black_chevrolet_silverado = ['','Color : black','Year : 2020','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Trailer sway capacity','Payload capacity : Suitable for transporting heavy loads','Truck bed : Provide flexibility for various cargo needs','Four-Wheel Drive : Available','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Driver assistance features : Such as Foward collision warning','Interior : Power-adjustable seats','           Dual-zone climate control','Trailering technology : Trailering camera system','                        Intergrated trailer brake controller','                        Trailer theft alert','Wi-fi hotspot : Internet access','Teen driver technology : Allow parents to monitor the teen driving behaviour','Off-road packages : Features like skid plates','Keyless entry and push-button start','Power tailgate : Ease of use','Safety : Airbags','         Stability control','         Traction control','']
            black_chevrolet_colorado = ['','Color : black','Year : 2021','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Features like intergrated trailer brake controller','Payload capacity : Suitable for cargo transportation','Truck bed options : Provide flexibility for different cargo needs','Four-Wheel Drive : For different driving conditions','Infotainment : Touchscreen display','             Bluetooth connectivity','             Navigation system','Off-road packages : Features like skid plates','Trailering technology : Such as trailer sway control','Wi-fi hotspot : Internet access','Teen driver technology : Allow the parents to monitor the teen driving behaviour','Keyless entry and push-button start : Added convinience','Safety : Airbags','         Stability control','         Traction controlCrew cab : Accommodate different passenger and cargo needs','Power seats : Enhanced driver comfort','Bluetooth hands-free calling : Prevent distractions while driving','']
            if z == 'Chevrolet Spark':
                for item in black_chevrolet_spark:
                    print(item)
            if z == 'Chevrolet Sonic':
                for item in black_chevrolet_sonic:
                    print(item)
            if z == 'Chevrolet Malibu':
                for item in black_chevrolet_malibu:
                    print(item)
            if z == 'Chevrolet Camaro':
                for item in black_chevrolet_camaro:
                    print(item)
            if z == 'Chevrolet Corvette':
                for item in black_chevrolet_corvette:
                    print(item)
            if z == 'Chevrolet Silverado':
                for item in black_chevrolet_silverado:
                    print(item)
            if z == 'Chevrolet Colorado':
                for item in black_chevrolet_colorado:
                    print(item)

        if y == 'white':
            print("The " + x + " cars availablein blue are: ")
            blue_chevrolet_list = ['Chevrolet Spark','Chevrolet Sonic','Chevrolet Malibu','Chevrolet Camaro','Chevrolet Corvette','Chevrolet Silverado','Chevrolet Colorado','']
            for item in blue_chevrolet_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            white_chevrolet_spark = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for city driving and parking in tight spaces','Fuel efficiency : Econimical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','City safety features : Safety features','Compact hatchback design : Versatile cargo space','Cost : Affordable','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Safety : Airbags','Onstar services : Provide emergency assistance,vehicle diagnostics and navigation','Compact spare tire : Backup','Fuel tank capacity : Small','Tire pressure monitoring system : Alert when pressure is low','Child safety seat anchores(LATCH) : Securing children','']
            white_chevrolet_sonic = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for urban driving and parking in tight spaces','Fuel efficiency : Economical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Available body styles : Flexibility for buyers who prefer different styles','Safety : Airbags','         Stability control','         Traction control','         Foward collision warning','Compact hatchback design : Additional cargo space','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Affordable price : Budget-friendly option','Onstar services : Offer emergency assistance,vehicle diagnostics and navigation','Rearview camera : Assist in parking and reversing','Tire pressure monitoring system : Alert when the pressure is low','Child safety seat anchors : Secure children','']
            white_chevrolet_malibu = ['','Color : White','Year : 2017','Engine : 2.0-liter turbocharged inline-4','Transmission : Automatic transmission for smooth and efficient power delivery','Infotainment : Android auto compatibility','             Bluetooth connectivity','             Navigation system','             Voice recognition','Safety : Airbags','         Stability control','         Traction control','         Foward collision warning','         Automatic emergency braking','         Lane departure warning','Interior : Power-adjustable seats','           Leather upholstery','         Dual-zone automatic climate control','Advanced driver assistance features : Adaptive cruise control','Keyless entry and push-button start : Added convinience','Wireless charging : Available','Teen driver technology : Allow parents to set certain parameters and receive a report on their teens behavior','Onstar services : Offer emergency assistance,vehicle diagnostics and navigation','Spacious trunk : More cargo space','Fuel efficiency : Suitable for economical commuting','Sunroof : Available','Wheels : Alloy for aesthetic appeal and improved performance','']
            white_chevrolet_camaro = ['','Color : White','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Suspension : Sport-tuned suspension system','Brembo brakes : Provide superior stopping power','Magnetic ride control : Adjusts suspension damping in real time for improved handling and ride comfort','Driver modes : Allow the driver to customize performance settings based on driving conditions','Tires : High performance for enhanced grip and handling','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Wi-fi hotspot : Allow access to internet','Premium audio system : Enhanced listening experience','Performance exhaust system : Provides an aggressive engine sound','Head-up display : Project important information onto the windshield','Recaro performance seats : Additional support for performance-oriented driving','Driver assistance features','Convertible top : For airy cabin feel','']
            white_chevrolet_corvette = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged V8','Mid-engine configuration : Behing the driver for improved weight distribution and handling','Transmission : Automatic transmission with paddle shifters for  manual control of gear changes','Magnetic ride control : Adaptive suspension system that adjusts damping in real time for optimal performance','Performance exhaust system : Offer different driving modes and sound profiles to suit various driving conditions','Driver modes : Allow driver to customize performance settings','Tires : Contribute to grip and handling capabilities','Brembo brakes : Superior stopping power','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','High-resolution display : Providing customizable information and perfomance data','Wi-fi hotspot : Access to internet','Premium audio system : Enhanced listening experience','Carbon fiber components : Reduced weight and improved performance','Convertible top : Airy cabin feel','Driver assistance features','']
            white_chevrolet_silverado = ['','Color : White','Year : 2020','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Trailer sway capacity','Payload capacity : Suitable for transporting heavy loads','Truck bed : Provide flexibility for various cargo needs','Four-Wheel Drive : Available','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Driver assistance features : Such as Foward collision warning','Interior : Power-adjustable seats','           Dual-zone climate control','Trailering technology : Trailering camera system','                        Intergrated trailer brake controller','                        Trailer theft alert','Wi-fi hotspot : Internet access','Teen driver technology : Allow parents to monitor the teen driving behaviour','Off-road packages : Features like skid plates','Keyless entry and push-button start','Power tailgate : Ease of use','Safety : Airbags','         Stability control','         Traction control','']
            white_chevrolet_colorado = ['','Color : White','Year : 2021','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Features like intergrated trailer brake controller','Payload capacity : Suitable for cargo transportation','Truck bed options : Provide flexibility for different cargo needs','Four-Wheel Drive : For different driving conditions','Infotainment : Touchscreen display','             Bluetooth connectivity','             Navigation system','Off-road packages : Features like skid plates','Trailering technology : Such as trailer sway control','Wi-fi hotspot : Internet access','Teen driver technology : Allow the parents to monitor the teen driving behaviour','Keyless entry and push-button start : Added convinience','Safety : Airbags','         Stability control','         Traction controlCrew cab : Accommodate different passenger and cargo needs','Power seats : Enhanced driver comfort','Bluetooth hands-free calling : Prevent distractions while driving','']
            if z == 'Chevrolet Spark':
                for item in white_chevrolet_spark:
                    print(item)
            if z == 'Chevrolet Sonic':
                for item in white_chevrolet_sonic:
                    print(item)
            if z == 'Chevrolet Malibu':
                for item in white_chevrolet_malibu:
                    print(item)
            if z == 'Chevrolet Camaro':
                for item in white_chevrolet_camaro:
                    print(item)
            if z == 'Chevrolet Corvette':
                for item in white_chevrolet_corvette:
                    print(item)
            if z == 'Chevrolet Silverado':
                for item in white_chevrolet_silverado:
                    print(item)
            if z == 'Chevrolet Colorado':
                for item in white_chevrolet_colorado:
                    print(item)

        if y == 'silver':
            print("The " + x + " cars available in maroon are: ")
            maroon_chevrolet_list = ['Chevrolet Spark','Chevrolet Sonic','Chevrolet Camaro','Chevrolet Corvette','Chevrolet Silverado','Chevrolet Colorado','']
            for item in maroon_chevrolet_list:
                print(item)
            print("Enter a name from the list to to view the specs: ")
            z = str(input())
            silver_chevrolet_spark = ['','Color : Silver','Year : 2019','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for city driving and parking in tight spaces','Fuel efficiency : Econimical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','City safety features : Safety features','Compact hatchback design : Versatile cargo space','Cost : Affordable','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Safety : Airbags','Onstar services : Provide emergency assistance,vehicle diagnostics and navigation','Compact spare tire : Backup','Fuel tank capacity : Small','Tire pressure monitoring system : Alert when pressure is low','Child safety seat anchores(LATCH) : Securing children','']
            silver_chevrolet_sonic = ['','Color : Silver','Year : 2021','Engine : 2.0-liter turbocharged inline-4','Compact size : Suitable for urban driving and parking in tight spaces','Fuel efficiency : Economical for daily commuting','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Available body styles : Flexibility for buyers who prefer different styles','Safety : Airbags','         Stability control','         Traction control','         Foward collision warning','Compact hatchback design : Additional cargo space','Transmission : Automatic transmission','Air conditioning : Enhance comfort','Affordable price : Budget-friendly option','Onstar services : Offer emergency assistance,vehicle diagnostics and navigation','Rearview camera : Assist in parking and reversing','Tire pressure monitoring system : Alert when the pressure is low','Child safety seat anchors : Secure children','']
            silver_chevrolet_camaro = ['','Color : Silver','Year : 2019','Engine : 2.0-liter turbocharged V6','Transmission : Automatic transmission','Suspension : Sport-tuned suspension system','Brembo brakes : Provide superior stopping power','Magnetic ride control : Adjusts suspension damping in real time for improved handling and ride comfort','Driver modes : Allow the driver to customize performance settings based on driving conditions','Tires : High performance for enhanced grip and handling','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','Wi-fi hotspot : Allow access to internet','Premium audio system : Enhanced listening experience','Performance exhaust system : Provides an aggressive engine sound','Head-up display : Project important information onto the windshield','Recaro performance seats : Additional support for performance-oriented driving','Driver assistance features','Convertible top : For airy cabin feel','']
            silver_chevrolet_corvette = ['','Color : Silver','Year : 2020','Engine : 2.0-liter turbocharged V8','Mid-engine configuration : Behing the driver for improved weight distribution and handling','Transmission : Automatic transmission with paddle shifters for  manual control of gear changes','Magnetic ride control : Adaptive suspension system that adjusts damping in real time for optimal performance','Performance exhaust system : Offer different driving modes and sound profiles to suit various driving conditions','Driver modes : Allow driver to customize performance settings','Tires : Contribute to grip and handling capabilities','Brembo brakes : Superior stopping power','Infotainment : Touchscreen display','             Smartphone intergration','             Bluetooth connectivity','             Navigation system','High-resolution display : Providing customizable information and perfomance data','Wi-fi hotspot : Access to internet','Premium audio system : Enhanced listening experience','Carbon fiber components : Reduced weight and improved performance','Convertible top : Airy cabin feel','Driver assistance features','']
            silver_chevrolet_silverado = ['','Color : Silver','Year : 2020','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Trailer sway capacity','Payload capacity : Suitable for transporting heavy loads','Truck bed : Provide flexibility for various cargo needs','Four-Wheel Drive : Available','Infotainment : Touchscreen display','             Bluetooth connectivity','             Smartphone intergration','             Navigation system','Driver assistance features : Such as Foward collision warning','Interior : Power-adjustable seats','           Dual-zone climate control','Trailering technology : Trailering camera system','                        Intergrated trailer brake controller','                        Trailer theft alert','Wi-fi hotspot : Internet access','Teen driver technology : Allow parents to monitor the teen driving behaviour','Off-road packages : Features like skid plates','Keyless entry and push-button start','Power tailgate : Ease of use','Safety : Airbags','         Stability control','         Traction control','']
            silver_chevrolet_colorado = ['','Color : Silver','Year : 2021','Engine : 2.0-liter turbocharged V8','Transmission : Automatic transmission','Towing capacity : Features like intergrated trailer brake controller','Payload capacity : Suitable for cargo transportation','Truck bed options : Provide flexibility for different cargo needs','Four-Wheel Drive : For different driving conditions','Infotainment : Touchscreen display','             Bluetooth connectivity','             Navigation system','Off-road packages : Features like skid plates','Trailering technology : Such as trailer sway control','Wi-fi hotspot : Internet access','Teen driver technology : Allow the parents to monitor the teen driving behaviour','Keyless entry and push-button start : Added convinience','Safety : Airbags','         Stability control','         Traction controlCrew cab : Accommodate different passenger and cargo needs','Power seats : Enhanced driver comfort','Bluetooth hands-free calling : Prevent distractions while driving','']
            if z == 'Chevrolet Spark':
                for item in silver_chevrolet_spark:
                    print(item)
            if z == 'Chevrolet Sonic':
                for item in silver_chevrolet_sonic:
                    print(item)
            if z == 'Chevrolet Camaro':
                for item in silver_chevrolet_camaro:
                    print(item)
            if z == 'Chevrolet Corvette':
                for item in silver_chevrolet_corvette:
                    print(item)
            if z == 'Chevrolet Silverado':
                for item in silver_chevrolet_silverado:
                    print(item)
            if z == 'Chevrolet Colorado':
                for item in silver_chevrolet_colorado:
                    print(item)

    #if the color is not available the user can enter another color or view other models with the color they entered
    if y not in Nissan:
        print("The color you entered is not available at the moment")
        print("You can enter another color or view other makes or view")
