import random

options = ('rock', 'paper', 'scissors')
user_wins = 0
computer_wins = 0
rounds = 1

print("Welcome to Rock, Paper, Scissors!")
print("-" * 33)
while True:
  print("ROUND", rounds)
  print("*" * 8)

  user_option = input("Select an option: rock, paper or scissors: ").lower().strip()
  computer_option = random.choice(options)

  if not user_option in options:
    print("Invalid option")
    continue

  print(f"You chose: {user_option}")
  print(f"Computer chose: {computer_option}")

  if user_option == computer_option:
    print("Tie!")
  elif user_option == "rock" and computer_option == "scissors" or user_option == "paper" and computer_option == "rock" or user_option == "scissors" and computer_option == "paper":
    print("You win!")
    user_wins += 1
  else:
    print("You lose!")
    computer_wins += 1

  print("User wins: ", user_wins)
  print("Computer wins: ", computer_wins)
  print("=" * 50)

  if user_wins == 2:
    print("User wins the game!")
    break
  if computer_wins == 2:
    print("Computer wins the game!")
    break

  rounds += 1