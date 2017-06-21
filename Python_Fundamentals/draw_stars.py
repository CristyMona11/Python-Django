
x = [4, 6, 1, 3, 5, 7, 25]
def stars(number):
    for num in number:
        output = ''
        for i in range(num):
            output += '*' #this means output=output + *
        print output
stars(x)


y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith', 'AlexP']
def stars(names):
    for item in names:
        output = ''
        if type(item) is int: #if item is an integer...
            for i in range(item):
                output += '*'   #you will output value of integer in amount of stars.
        elif type(item) is str: #if the item is a string
            f_letter = item[0].lower()
            for i in range(len(item)):
                output += f_letter #the output is the first letter
        print output
stars(y)
