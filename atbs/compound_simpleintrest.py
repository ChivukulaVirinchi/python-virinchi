# Date: 22/12/19
# This program can calculate compound and simple intrest  
import math
Name = input('Hello there please enter your name: ').lower()
print('Hello ' + Name + ' I am a simple and compound intrest calculator: ')
cors = input('So, do you want to calculate Compound or Simple Intrest: ').lower() 
principle = input('Please enter Principle Amount: ')
rate = input('Please enter Rate of Intrest: ')
time = input('Please enter Time Period: ')
if 's' in cors:      
    si = (int(principle) * int(time) * int(rate))/100
    fsi = int(principle) + int(si)
    print('In Simple Intrest, after the end of ' + str(time) + ' years, youll have to pay Rs ' + str(fsi))
elif 'c' in cors:
    ci = int(principle) * (1 + int(rate)/100) ** int(time)
    print('In Compound Intrest, after the end of ' + str(time) + ' years, youll have to pay Rs ' + str(ci))    

