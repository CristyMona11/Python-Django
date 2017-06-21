def getEven():
    for x in range (1,2001):
        if x % 2 == 0:
            print "Number is" ,x, ".This is an even number."
getEven()

def multiply():
    b = []
    a = [2,4,10,16]
    for i in a:
        b.append(i*5)
    print b
multiply()
