'''
Build a temperature converter that can convert the temperature in celsius to fahrenheit
'''

def convert_temperature(temp_c):
    temp_f = temp_c * (9 / 5) + 32
    return temp_f

temp_c = float(input("Enter the temperature in celcius: "))
temp_f = convert_temperature(temp_c)
print("The temperature in Farenheit: ", temp_f,"F")