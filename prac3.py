#Find Factororial of your Number
number=int(input("Enter Your Number"))
if(number<0):
 print("Try Another Numebr")
elif(number==0):
 print("Try Another One")
else:
 print("okk Let's Find your remnder")
 for x in range(1,number):
  number=number*x
 print("The fact is",number)  