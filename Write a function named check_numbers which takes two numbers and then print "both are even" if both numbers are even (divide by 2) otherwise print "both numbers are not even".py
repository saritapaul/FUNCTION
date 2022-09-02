#Write a function named check_numbers which takes two numbers and then print "both are even"
# if both numbers are even (divide by 2) otherwise print "both numbers are not even".
def check_numbers(num,num1):
    if num%2==0 and num1%2==0:
        print("both are even ")
    else:
        print("both are not even")
check_numbers(2,4)
