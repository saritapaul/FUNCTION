def calculator(num_x,num_y,operator):
	if operator=="+":
     x=num_x+num_y
     return x
    elif operator=="-":
	    y= num_x-num_y
	       return y
    elif operator=="*":
	    z= num_x*num_y
	        return z
	elif operator=="/":
	     p= num_x/num_y
	      return p
num_x=int(input("enter no"))
num_y=int(input("enter 2 nd no"))
operator=input("enter operator")
print(calculator(num_x,num_y,operator))
