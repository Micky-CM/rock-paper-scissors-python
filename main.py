import random

print("🤖 Welcome to Rock, Paper, Scissors! 🪨 📃✂️")
print("-" * 33)

def choose_options():
    options = ('rock', 'paper', 'scissors')
    user_option = input("Select an option: rock, paper or scissors: ").lower().strip()

    if not user_option in options:
        print("Invalid option")
        return None, None

    computer_option = random.choice(options)

    print(f"You chose: {user_option}")
    print(f"Computer chose: {computer_option}")
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Tie!")
    elif user_option == "rock" and computer_option == "scissors" or user_option == "paper" and computer_option == "rock" or user_option == "scissors" and computer_option == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    if user_wins == 2:
        print("User wins the game!")
        exit()
    if computer_wins == 2:
        print("Computer wins the game!")
        exit()

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print("ROUND", rounds)
        print("*" * 8)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)

        print("User wins: ", user_wins)
        print("Computer wins: ", computer_wins)
        print("=" * 50)

run_game()