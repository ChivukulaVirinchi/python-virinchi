def calculator_mean (first, * remainder):
    '''This calculates the mean of numbers'''
    mean = (first + sum(remainder))//(1 + len(remainder))
    return mean
print(calculator_mean(23, 43, 56, 76, 45))