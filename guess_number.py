"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random

random_num=random.randint(1,20)
count=1
while count <= 5:
    num=int(input("Guess number between 1 and 20: "))
    if num >= 1 and num <=20:
        if num < random_num:
            print("TOO LOW")
        elif num > random_num:
            print("TOO HIGH")
        else:
            print(num,"YOU GUESSED RIGHT!")
            break
    else:
        print("Input number within range")
    count+=1
if count > 5:
    print("GAME OVER")
