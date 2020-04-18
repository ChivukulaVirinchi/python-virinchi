userInput = int(input('Enter the age of your classmate\n>>>'))
ages = []
while userInput > 0:
    ages.append(userInput)
    userInput = int(input('Enter the next age\n>>>'))
print('The ages are', sorted(ages))