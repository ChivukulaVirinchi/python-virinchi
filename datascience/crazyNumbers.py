num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))

if num1 and num2 > 15:
    print(num1 * num2)
elif num1 > 15:
    print(num1 + num2)
else: print(0)