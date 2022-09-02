#Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting of 18).
def voting(age):
    if age >=18:
        print("eligible for voting")
    else:
        print("not eligible for voting")
age=int(input("enter age:-"))
voting(age)