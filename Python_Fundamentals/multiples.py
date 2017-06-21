for count in range (1,1000):
    if (count % 2 != 0):
        print count

for count in range (5,1000000):
    if (count % 5 == 0):
        print count

a = [1, 2, 5, 10, 255, 3]
#variable where I am storing the sum.
sum = 0
#variable to store the average
avg = 0
#adding all the values to create a new sum
for val in a:
    sum = sum + val
    avg = sum/6
#output is the answer, total sum of numbers, 276.
print ("The sum is",sum)
print ("The avg is",avg)
