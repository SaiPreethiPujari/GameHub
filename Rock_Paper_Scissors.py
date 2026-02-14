import random

rock='''  
         ________  
_______'     ____)
          (_______)
          (_______)
          (_____)
-----.___ (____)
'''
paper ='''
       ________  
_______'     ____)_____
                _______)
                ________)
                _______)
--------.____________)

'''
scissors='''
        _________  
_______'     ____)_____
                 _______)
            ______________)
           (_____)
--------.__(____)
'''

game_image=[rock,paper,scissors]
user_choice = int(input("Enter the choice 0 for rock, 1 for paper, 2 for scissors: "))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("Computer Choice")
print(game_image[computer_choice])
if user_choice>2 or user_choice<0:
    print("Invalid choice,YOU LOSS ")
else:
    if user_choice==computer_choice:
        print("draw the game")
    elif computer_choice==0 and user_choice==2:
        print("YOU LOSS")
    elif computer_choice==2 and user_choice==0:
        print("YOU WIN")
    elif computer_choice>user_choice:
        print("YOU LOSS")
    elif computer_choice < user_choice:
        print("YOU WIN")

