import random

# Greeting message
print('***********************************************\n'
      '\tWELCOME TO THE Lucky Rolls Game\n'
      '***********************************************\n')

# Function to display game rules
def display_game_rules():
    """
    This function prints the rules of the Rolling Dice Game.
    """
    print("\nGAME RULES:\n"
      "1. Each player takes turns rolling a six-sided dice.\n"
      "2. On your turn, you can roll the dice as many times as you want to accumulate points.\n"
      "3. If you roll a '1':\n"
      "   - Your turn ends immediately.\n"
      "   - You lose all points earned during that turn.\n"
      "   - Your total score remains unchanged.\n"
      "4. If you roll a number other than '1':\n"
      "   - Add that number to your turn's score.\n"
      "   - You can choose to roll again or save your turn score.\n"
      "5. To save your score:\n"
      "   - End your turn and add the turn score to your total score.\n"
      "6. The first player to reach or exceed the target score (e.g., 20) wins the game.\n"
      "7. Players can choose to skip their turn without rolling.\n"
      "8. Have fun and good luck!\n")
    
def roll_dice():
    """Simulate rolling a six-sided dice and return a value between 1 and 6."""
    return random.randint(1, 6)

def playgame():
    # Input: Number of players
    while True:
        num_players = input('How many players want to play? (Enter a number between 2 and 4): ')
        if num_players.isdigit():
            num_players = int(num_players)
            if 2 <= num_players <= 4:
                break
            else:
                print('Error: The number of players must be between 2 and 4.\n') 
        else:
            print('Error: Please enter a valid number.\n')

    # Initialize players and their scores
    player_scores = {}  # Dictionary to store players' names and their scores
    max_score_limit = 20  # Maximum score to win the game

    # Input: Player names
    for player_num in range(1, num_players + 1):
        player_name = input(f'Enter Player {player_num} Name: ').strip()
        player_scores[player_name] = 0

    # Game loop
    while max(player_scores.values()) < max_score_limit:
        for player_name, current_score in player_scores.items():
            turn_score = 0  # Points scored in the current turn

            # Ask if the player wants to play their turn
            play_turn = input(f"\n{player_name}, do you want to play this turn? (Yes/No): ").strip().lower()

            if play_turn in ['yes', 'y']:
                while True:
                    dice_roll = roll_dice()

                    # If the dice roll is 1, end the turn without adding points
                    if dice_roll == 1:
                        print(f"You rolled a 1! Turn over. No points added.")
                        turn_score = 0
                        break
                    else:
                        print(f"You rolled a {dice_roll}.")
                        turn_score += dice_roll
                        print(f"Your turn score so far: {turn_score}")

                        # Ask if the player wants to roll again or save their score
                        next_action = input(f"Do you want to roll again or save your score, {player_name}? (Roll/Save): ").strip().lower()
                        if next_action in ['save', 's']:
                            print("Turn ended. Your score has been saved.")
                            break

                # Update the player's total score
                player_scores[player_name] += turn_score
                print(f"{player_name}'s total score is now {player_scores[player_name]}.\n")

                # Check if the player has won
                if player_scores[player_name] >= max_score_limit:
                    print(f"\nCongratulations, {player_name}! You have won the game with a score of {player_scores[player_name]}!")
                    break

            elif play_turn in ['no', 'n']:
                print(f"{player_name} chose to skip this turn.")
            else:
                print("Invalid input. Turn skipped.")

        else:
            # Continue the game if no player has reached the maximum score
            continue
        break

    # Display final scores
    print("\nFinal Scores:")
    for name, score in player_scores.items():
        print(f'{name}: {score}')

# Main menu     
while True:
    # Asking user to Play Game, Check Game Rules or Exit the Game
    choice = input('\n1. Press P to Play Game (or press 1)\n'
                   '2. Press R to Read Game Rules (or press 2)\n'
                   '3. Press E to Exit the Game (or press 3)\n\n'
                   'Enter your choice (P/R/E or 1/2/3): ').lower()
    
    
    if choice in ['r', '2']:
        display_game_rules()
    elif choice in ['p', '1']:
        playgame()
    elif choice in ['e', '3']:
        print('You have exited the game. See you next time!\nTHANK YOU :)')
        break
    else:
        print('Invalid input. Please enter a valid option.\n')