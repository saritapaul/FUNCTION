#Write a Python program to generate and print a list of first and last 5 elements where
#the values are square of numbers between 1 and 30 (both included).
#Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def square(list,list2):
    l=[ ]
    l2=[ ]
    i=0
    while i<len(list):
      a=list[i]*list[i]
      b=list2[i]*list2[i]
      i+=1
      l.append(a)
      l2.append(b)
    print(l,l2)
square([1,2,3,4,5,],[26,27,28,29,30] )
    