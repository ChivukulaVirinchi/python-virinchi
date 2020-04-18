def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
         return fib2(n-1) + fib2(n-2)

x = fib2(20)
# #Should not be used for large numbers. The computer's memory will fill up
print(x)
