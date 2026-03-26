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

list = [rock, paper, scissors]

choice1 = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
print("you choose",list[choice1])

choice2= random.randint(a=0,b=2)
print(f"computer choose {choice2}",list[choice2])

if choice1 == 0 and choice2 == 2 :
    print("You won")
elif choice2 ==0 and choice1 == 2 :
    print("computer won")
elif choice1 == 2 and choice2 == 1 :
    print("You won")
elif choice2 == 2 and choice1 == 1 :
    print("computer won")
elif choice1 == 1 and choice2 == 0 :
    print("you won")
elif choice2 == 1 and choice1 == 0 :
    print("computer won")
elif choice1== choice2 :
    print("It's a draw")
else :
    print("It's invalid choice")

