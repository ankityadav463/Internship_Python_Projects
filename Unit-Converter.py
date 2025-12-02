# Unit Converter
while True:
    print("=====Welcome To Unit Converter=====")
    try:
        n=int(input("1.Mm into Cm\n2.Cm into M\n3.M into Kilometer\n4.Celsius to Fahrenheit\nEnter No.:"))
        match(n):
            case(1):
                a=int(input("Enter in Mm: "))
                print(f'Mm into Cm: {a/10}')
                break
            case(2):
                a=int(input("Enter in Cm: "))
                print(f'Cm into Meter: {a/100}')
                break
            case(3):
                a=int(input("Enter in Meter: "))
                print(f'Meter into Kilometer: {a/1000}')
                break
            case(4):
                a=float(input("Enter in Celsius: "))
                f=(a*9/5)+32
                print(f'Celsius into Fahrenheit: {f}')
                break
    except:
        print("Enter Only(1 to 4) Digits...")  
