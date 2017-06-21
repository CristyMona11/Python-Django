
my_string = "If monkeys like bananas, then I must be a monkey!"
print my_string.find("monkey")
print my_string.replace("monkey", "alligator")


x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[:1]
print x[7:]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
c = x[:len(x)/2]
d = x[len(x)/2:]
print c
print d
d.insert(0,c)
print d        
