#Given a list of numbers, write a Python program to count positive and negative numbers in a List using
#function.Example:list1 = [2, -7, 5, -64, -14]
def numbers(list ):
  #list=[2,-7,5,-64]
  i=0
  count=0
  count1=0
  while i<len(list):
    if list[i]<0:
      count+=1
    else:
      count1+=1
    i+=1
  print(count,count1)
numbers([2,-7,5,-64,-14])