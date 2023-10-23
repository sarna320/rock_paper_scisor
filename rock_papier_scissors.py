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
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

tab=[rock,paper,scissors]

choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choose_PC=random.randint(0,2)
print(f"Player1:{tab[choose]}\nPlayer2:{tab[choose_PC]}")

if(choose==choose_PC):
    print("Tie")
elif(choose==0):
    if(choose_PC==1):
        print("Player2 won")
    else:
        print("Player1 won")
elif(choose==1):
    if(choose_PC==2):
        print("Player2 won")
    else:
        print("Player1 won")
elif(choose==2):
    if(choose_PC==0):
        print("Player2 won")
    else:
        print("Player1 won")

