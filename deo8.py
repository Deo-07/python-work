#Find a Prime Numebr

n=int(input("Enter Your Numebr:"))


if n<2:

 print("It is not a prime Number:")

else:

 for i in range(2,n):
   if n%i==0:
    print("Not a Prime")
 
    break

 else:
     print("Number is Prime") 

