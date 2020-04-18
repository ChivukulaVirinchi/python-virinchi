findMax = 0
data = [10, 123, 1224324, 54645, 4564567, 879789, 67, 1]
for num in data:
    if num > findMax:
        findMax = num
print('The highest value of', data, 'is', findMax)