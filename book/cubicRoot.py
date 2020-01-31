## Simple program that finds if a given number has a cubic root
number = int(input("Write a number:\n"))
iterator = 0
found = False
while iterator<number and found==False:
  if(iterator**3 == number):
    print("The number has a cubic root:", iterator)
    found= True
  iterator+=1
if(not found):
    print("The number doesn't has a cubic root")