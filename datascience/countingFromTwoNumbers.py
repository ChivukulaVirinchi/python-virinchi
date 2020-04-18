num1 = int(input('Enter the first number\n>>>'))
num2 = int(input('Enter the second number\n>>>'))
i = num1
if num1 > num2:
    for i in range(num1, num2 + 1):
        print(i, end=' ')
while i < num2:
    i = i + 1
    print(i, end=' ')

