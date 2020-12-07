#Guess Random Numebr Game

import random
random_number=random.randrange(1,10)
ran=int(input("Hey Try to guess Random Number:"))

while True:
 if(ran==random_number):
  print("heY You Got The Number")
  break
 elif(ran<random_number):
  print("Too Low")
  break
 elif(ran>random_number):
  print("Too High")
  break

                                                                                                                                 