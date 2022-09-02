#Kids drink toddy.
#Teens drink coke.
#Young adults drink beer.
#Adults drink whisky.
#Make a function that receive age, and return what they drink.
#Rules:-Children under 14 old.
def children(age):
    if age <14:
     return "drink toddy"
    elif age<18:
     return "drink coke"
    elif age<21:
     return "drink beer"
    else:
     return "drink whisky"
age1=int(input("enter number:-"))
print(children(age1))