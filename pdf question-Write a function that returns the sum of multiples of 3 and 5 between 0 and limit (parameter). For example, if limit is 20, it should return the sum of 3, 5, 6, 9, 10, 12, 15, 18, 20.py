#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit
#(parameter). For example, if limit is 20, it should return the sum of 
# 3, 5, 6, 9, 10, 12, 15, 18,20.
def sum_no(limit):
    sum=0
    i=1
    while i<=a:
        if i%3==0 or i%5==0:
            sum+=i
            print(sum)
        #i+=1
        else:
            pass
        i+=1
a=int(input("enter no"))
sum_no(a)