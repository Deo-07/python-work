#Pyhon IF , Else  and Elif statements


age=int(input("Enter Your Age:"))




if(age>28):
 print("Yes U can Drink Alcohol")

elif( age>15):
 print("You can take Only soft Drinks")

else:
 print("You can only drink Water")


#Sort Hand If OR Else it is Also known as ternary operaters




if(12>6):print("hello ")




#Nested IF Statements

x=50


if(x>40):
 print("Above Ten")
 if(x>30):
  print("and also  greater than 30")
 
  if(x>20):
   print("also greater than 20")

  else:
    print("But not above than 20")



#The Pass Statements - If statements can not be empty its only happen when u use pass statatements

if(2>4):
 pass