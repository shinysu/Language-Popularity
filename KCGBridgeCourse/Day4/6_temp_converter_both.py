'''
temperature converter - converts the temperatue in celcius to farenheit and farenheit to celcius
Write a temperature converter that can get the temperature and units and convert it to the other metric.
'''

def convert_temperature(temp, unit):
    if unit == 'c':
        temp_new = temp * (9 / 5) + 32
        unit = 'F'
    elif unit == 'f':
        temp_new = (temp - 32) * 5 / 9
        unit = 'C'
    return temp_new, unit

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit: ")
temp_converted, unit = convert_temperature(temp, unit)
print("The temperature in Farenheit: ", temp_converted, unit)