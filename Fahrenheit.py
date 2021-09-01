def main():
    printC(formeln(typeHere()))

def typeHere():
    global Fahrenheit
    try:
        Fahrenheit = int(input("Hi! Enter Fahrenheit value, and get it in Celsius!n"))
    except ValueError:
        print ("nYour insertion was not a digit!")
        print ("We've put your Fahrenheit value to 50!")
        Fahrenheit = 50
    return Fahrenheit

def formeln(c):
    Celsius = (Fahrenheit - 32.00) * 5.00/9.00
    return Celsius

def printC(answer):
    answer = str(round(answer, 2))
    print ("nYour Celsius value is " + answer + " C.n")



main()
