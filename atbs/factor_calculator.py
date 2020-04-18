# Date: 23/12/19
# This program is a factor calculator
n = input('Which number do you wish to calculate the factors of? ')
num = int(n)
i = 1
while i <= num:
    if num % i ==0:
        print(i)
    i += 1

