#Find Next Prime Number


deo=int(input("Enter Your First Prime"))


while True:
 deo+=1
 for x in range(2,deo):
  if(deo%x==0):
    break

 else:
   print("Next prime Number is " +str(deo))
   break

 

 

