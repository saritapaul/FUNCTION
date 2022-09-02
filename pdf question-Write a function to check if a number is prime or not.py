#Write a function to check if a number is prime or not.
def prime_number( ):
    a=int(input("enter number "))
    i=2
    while i<a//2:
        if a%i==0:
            print("it is not a prime number",a)
            break
        i+=1
    else:
        print("it is a prime no",a)
prime_number( )