n = 100
for n in range(1, n+1):
    if n % 3 == 0 and n % 5 != 0:
        print(n, 'Fizz')
    elif n % 3 != 0 and n % 5 == 0:
        print(n, 'Buzz')
    elif n % 3 == 0 and n % 5 == 0:
        print(n, 'FizzBuzz') 
    else: print(n)