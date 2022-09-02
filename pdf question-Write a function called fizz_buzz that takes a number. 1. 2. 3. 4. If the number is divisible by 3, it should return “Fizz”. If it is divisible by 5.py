#Write a function called fizz_buzz that takes a number.
#1.If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return "fizzbuzz"
    elif num%3==0:
        return "fizz"
    elif num%5==0:
        return "buzz"
    else:
        return num
num1=int(input("enter no"))
print(fizz_buzz(num1))
