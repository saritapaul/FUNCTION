#Write a Python function to sum all the numbers in a list.
#numbers=(8, 2, 3, 0,7)
def sum(number):
    sum1=0
    i=0
    while i<len(number):
        sum1+=number[i]
        i+=1
    return sum1
print(sum((8,2,3,0,7)))


