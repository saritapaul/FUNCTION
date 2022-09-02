#write a function bmi that calculate body mass index.weight/height2
def bmi():
    a=int(input("enter weight "))
    b=float(input("enter height "))
    c=a/b**2
    if c<=18.5:
        return "underweight "
    elif c<=25.0:
        return "normal"
    elif c<=30.0:
        return "overweight"
    elif c>30:
        return "obese"
print(bmi())