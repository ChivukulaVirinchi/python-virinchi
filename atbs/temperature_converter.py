# Date: 22/12/19
# This program converts the given temperature units
import re
def conversion():  
    c = input('Enter temperature in K or C or F: ')
    v = re.split('(\d+)', c)
    cv = str(v[1])
    if 'C' in c:
        f = int(cv) * (9/5) + 32
        print (str(f) + '°F')
    elif 'F' in c:
        fer = (int(cv) - 32) * (5/9) 
        print (str(fer) + '°C')
    elif 'K' in c:
        kelvin = int(cv) -273.15
        print(str(kelvin) + '°C')   
    else: print('Please Enter a valid Temperature unit')    
i = 0
while i <= 2:
    conversion()
    i = i + 1

    