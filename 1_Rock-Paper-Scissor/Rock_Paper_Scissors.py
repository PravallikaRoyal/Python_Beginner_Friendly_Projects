import random
rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

hand_images = [rock, paper, scissors]
#input for user_choice
user_choice = int(input('''Enter your choice:
                        If you want to chose Rock enter 0
                        If you want to chose Paper enter 1
                        If you want to chose Scissprs enter 2 \n'''))
print(hand_images[user_choice])

#input for computer choice:
comp_choice = random.randint(0,2)
print(hand_images[comp_choice])

#main logic of the game:
if user_choice>=3:
    print("You have entered invalid choice.. You lose!")
elif user_choice == 2 and comp_choice == 0:
    print("You win!")
elif comp_choice == 2 and user_choice == 0:
    print("You lose.. Computer win!")
elif user_choice > comp_choice:
    print("You win!")
elif comp_choice > user_choice:
    print("You lose.. Computer win!")
elif comp_choice == user_choice:
    print("It's a Draw")