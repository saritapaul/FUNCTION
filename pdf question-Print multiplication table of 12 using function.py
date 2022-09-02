#Print multiplication table of 12 using function.
from re import I


def multiplication( ):
    a=int(input("enter number"))
    i=1
    while i<=10:
        b=a*i                                                           
        print(b)
        i+=1
multiplication( )