def multiply(arr,num):
    for x in arr:
        print x
        x *= num
        print x
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b
