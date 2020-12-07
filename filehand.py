#Let's Create a New File


# file=open("filehand.txt","x")


#Let's write something in my file using append 

# file=open("filehand.txt","a")
# file.write("This is My first line of which is Written By Append mode")
# file.write("This is secound Line'\n")
# file.close()

# _______________________________________

#Let's write Something By using Write mode in file Handling

# file=open("filehand.txt","w")
# file.write("This is a write mood and It will Overwrite on your all text")
# file.close()


# __________________________________________


#In the last of of Code Let's See About Reading Mood Therer is many ways to do that 


#1 Way

# file=open("filehand.txt","r")
# a= file.read()
# print(a)
#file.close()


#2 way
file=open("filehand.txt","r")
for line in file:
file.readline()
 print(b)




