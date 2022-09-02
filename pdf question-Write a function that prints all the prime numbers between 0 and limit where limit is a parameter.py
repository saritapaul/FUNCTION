#Write a function that prints all the prime numbers between 0 and limit where limit is a
#parameter.
def prime(limit):
    i=1
    a=2
    while i<=input//2:
        if i%a==0:
            print("it is not a prime no",a)
            break
        #i+=1
        else:
            print("it is a prime no",a)
        i+=1
input=int(input("enter no "))
prime(input