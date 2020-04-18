n = 20
def fib(n):
    '''Calculates and returns the nth fibonocci function'''
    a = 0
    b = 1
    for i in range(n):
        a,b =  b, a + b
    return a
fib(n)

fib_num = fib(n)
print(fib_num)

for i in range(n):
    print(fib(i))

    
y = fib(1000)
print(y)