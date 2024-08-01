import random, temperatureConverter

#Convert fahrenheit to celcius

#List of color based temperatures
#<90 Degrees and up: red> <75 - 89 Degrees: yellow> <64 - 74 Degrees: green> <63 and Below: blue>

#print temperature in both fahrenheit and celcsius, print in the color assigned to the temperature
#User input to take in temperature


#----------REFINEMENT--------REFINEMENT-------------------REFINEMENT---------------REFINEMENT-----------REFINEMENT----------
#Format Celsius to show only one place after the decimal
# i.e., 22.8888888888 --> 22.8


#---------------------Code Setup------------------------
#1. Import random
#2. from colorama import Fore
#3. 5 variables that hold the colors
    #i.e.,, red = Fore.RED

#4. def temperatureConverter(user_input):
    #5. FAHRENHEIT_TO_CELSIUS = This variable is to do conversion from Fahrenheit to Celsius
    #6. Conditional if/elif/else: total of 4 statements
        #6a. print statements that print Fahrenheit and temperature in color associated
        #i.e., print("Fahrenheit:   ", red, temperature, black)
        #i.e., print("Celsius:  ", red, temperature, black)

#Call function and pass parameters to function

#-----------------ACTUAL CODE---------------------
import random, temperatureConverter
from colorama import Fore

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

def temperatureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * (5/9)
    #i.e., SQUARE_ANY_NUM = num * num
   
    if(user_input >= 90):
        print("Fahrenheit:  ", red, "{0:4.1f}".format  (user_input), black)
        print("Celsius: ", red, "{0:4.1f}".format (FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 75) & (user_input <= 89):
        print("Fahrenheit:  ", yellow, "{0:4.1f}".format (user_input), black)
        print("Celsius ", yellow, "{0:4.1f}".format  (FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 64) & (user_input <= 74):
        print("Fahrenheit: ",green, "{0:4.1f}".format (user_input), black)
        print("Celsius ", green, "{0:4.1f}".format (FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input <=63):
        print("Fahrenheit: ", blue, "{0:4.1f}".format (user_input), black)
        print("Celsius ", blue, "{0:4.1f}".format (FAHRENHEIT_TO_CELSIUS), black)
user=float(input("Enter a temperature in Fahrenheit to convert to Celsius: "))


for x in range(5):
    temperatureConverter(user)
    user=float(input("Enter a temperature in Fahrenheit to convert to Celsius: "))


        
