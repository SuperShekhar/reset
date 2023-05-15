import random
number = random.randint(1,30)

maxguess=5
numguess=0
 
print('i am thinking a number between 1 to 30 you have 6 chances to guess it')

while numguess<maxguess:
    

   guess=int(input("guess a number "))
   numguess += 1
    
   
   if  guess == number:
        print('congrats you have a guess a correct number ,yes it is',number)
        print('you have guessed it in ',numguess,"attempt")
        break
   elif guess>number:
        print("your number is high")
   else:
        print('your number is low')

else:
    print("sorry you couldn't give the correct number . the number was",number)
    