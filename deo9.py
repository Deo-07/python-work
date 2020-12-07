def Function():

 number=int(input("Enter Your First prime Number:"))

 while True:
   number+=1
   for i in range(2,number):

        if number%i==0:
            break

   else:

    print("Your Next Prime Number is:"+str(number))
    break 
 


Function()
