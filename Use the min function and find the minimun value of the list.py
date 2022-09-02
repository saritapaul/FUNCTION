#Use the min function and find the minimun value of the list.
def min():
    list = [8, 6, 4, 8, 4, 50, 2, 7]
    i=0
    list1=list[i]
    while i<len(list):
        if list[i]<list1:
            list1=list[i]
        i+=1
    print(list1)
min()