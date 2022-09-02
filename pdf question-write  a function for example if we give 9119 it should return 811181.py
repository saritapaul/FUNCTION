#write a function for example if we give 9119 it should return 811181.
def square(b):
    i=0
    sum=" "
    while i <len(a):
        num=int(a[i])**2
        sum=sum+str(num)
        i+=1
    return sum
a=input("enter no ")
print(square(a))