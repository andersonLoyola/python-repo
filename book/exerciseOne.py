# Write a program that asks the user to enter a integer and prints two integers, root and pwr, such that 0 < pwr < 6 amd root**pwr is equals to the integer entered by the user
number  = int(input("Write some number: "))
auxNumber = 1
found = False
while auxNumber < number and found == False:
  auxPower=0
  while auxNumber**auxPower <= number and auxPower < number and found == False:
    if auxNumber**auxPower == number:
      found = True
    else:
      auxPower+=1
    print(auxNumber, "-", auxPower)
  if(not found):
    auxNumber+=1
if found == True:
  print("number", auxNumber, "power", auxPower)
else:
  print("not found")
