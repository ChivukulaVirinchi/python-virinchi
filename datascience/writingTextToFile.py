userInput = str(input('What do you want to append to the file?'))
f = open('test1.py', 'a')
f.write('\n' + userInput)
f.close()

with open('test1.py', 'r') as f:
    for line in f.readlines():
        print(line, end=' ')