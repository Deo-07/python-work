#Find a Prime Number in python 

a=int(input("Enter a Number:"))

if a>1:
  for x in range(2,a):
    if a%x==0:
      print("Not prime")
      break

    else:
       print("it is a prime  number")   
       break

else:
  print("This is Not a prime Number")