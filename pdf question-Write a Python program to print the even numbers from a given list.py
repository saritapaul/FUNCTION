#Write a Python program to print the even numbers from a given list.
#list=[1,2,3,4,5,6,7,8,9] output=[2,4,6,8]
def even(list):
    list1=[ ]
    i=0
    while i<len(list):
        if list[i]%2==0:
            list1.append(list[i])
        i+=1
    return list1
print(even([1,2,3,4,5,6,7,8,9]))