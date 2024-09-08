# Exceptional Weather Forecast

'''
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error mesages.
'''

# Task 1: Begin asking the user to enter the temperature in Fahrenheit.
def forecast_weather():

    while True:
        try:

            fahrenheit_temperature = float(input("What is the current Temperature in Fahrenheit?:"))



# Task 2: Temperature Conversion: Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit -32) *5/9.
            fahrenheit_temperature 
            celsius = (fahrenheit_temperature - 32) * 5/9
            celsius_rounded = round(celsius,2)
           
        except ValueError:
            print("That's not a valid temperature, please Try again using numbers.")




# Task 3: User Experience Implement an else Block that prints the converted temperature in a user-friendly format
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."


        else:
            print(f"Your temperture converted form Fahrenheit to Ceslisus is:{celsius_rounded}.")
            break




# Task 4: Finally add a 'finally' block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

        finally:
            print("Thank you for using my Forecast converter!")
            break

forecast_weather()