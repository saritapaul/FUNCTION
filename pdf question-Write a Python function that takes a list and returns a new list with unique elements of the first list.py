#.Write a Python function that takes a list and returns a new list with unique elements of the
#first list.Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5].
def unique(list):
    list1=[]
    i=0
    while i<len(list):
        if list[i] not in list1:
            list1.append(list[i])
        i+=1
    return list1
print(unique([1,2,3,3,3,3,4,5,]))