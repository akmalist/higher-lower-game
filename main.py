
from replit import clear
import random 
from art import logo,vs
print(logo)
from game_data import data

gameOn= True 
score = 0
account_b = random.choice(data)

#10 keep repating until user selects a wrong asnwer and return the result
while gameOn:
#1 generate two random accounts  
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    #2 take those two numers and pull the information from the game data file (with their data.length)

    def printableNames(account):
        account_name=account['name']
        description = account['description']
        country = account['country']
        return (f'{account_name}, {description}, from {country}')
                
    print("Compare A: ", printableNames(account_a))
    print(vs)
    print("Against B: ", printableNames(account_b))


#3 compare one information vs another .  
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong."""
    def check_answer(guess, acount1, acount2):
        if acount1>acount2:
            return guess == 'a'
        else:
            return guess =='b'
 
#4 ask the user for their input (A or B)
    userInput =  input("Who has more followers? Type 'A' or 'B':\n").lower()

    account_follower_1= account_a['follower_count']
    account_follower_2= account_b['follower_count']
    

    corect_answer = check_answer(userInput,account_follower_1, account_follower_2)

#clears the screen and prints the logo each time for the loop
    clear()
    print(logo) 

    #6 compare if the user selects A and it's value greater than b then increase the "Points" variable
    #7if the user selects B and it is greater than A then also increase the Points variable
    #8if the user selects B and it is smaller than B then return the final "Points" and tell the user they are wrong
    #9if the user Selects A and it is smaller than A then return the final "Points" and tell the user they are wrong
 
    if corect_answer:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"OOOPS!You lost and your score is {score}")
        gameOn=False


    # if userInput == 'a' and account_follower_1>account_follower_2:
    #     score+=1
    #     clear()
        # print(f"You're right! Current score: {score}.")
        
    # elif userInput == 'b' and account_follower_1<account_follower_2:
    #     score+=1
    #     clear()
    #     print(f"You're right! Current score: {score}.")
       
    # else:
    #     clear()
    #     print(f"OOOPS You lost and your score is {score}")
    #     gameOn=False







