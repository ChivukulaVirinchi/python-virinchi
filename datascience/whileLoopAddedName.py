count = 0
Names = []
name = str(input('Enter the names of people in the classroom\n>>>'))
while name != 'n':
    count +=1
    Names.append(name)
    print(f'{name} has been added\n>>>')
    name = str(input('Next name\n>>>'))
print(f'There are {count} people in the class. They are {Names}' )