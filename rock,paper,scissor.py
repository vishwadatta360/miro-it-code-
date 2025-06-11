import random

def play_rock_paper_scissors():
    user_wins = 0
    computer_wins = 0
    ties = 0
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play.")
    print("Enter 'quit' to stop the game.")

    while True:
        print(f"\n--- Current Score: You: {user_wins} | Computer: {computer_wins} | Ties: {ties} ---")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

    print("\n--- Game Over! ---")
    print(f"Final Score: You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")

    if user_wins > computer_wins:
        print("Congratulations! You won the game overall!")
    elif computer_wins > user_wins:
        print("Better luck next time! The computer won the game overall.")
    else:
        print("The game ended in a tie overall!")

if __name__ == "__main__":
    play_rock_paper_scissors()
