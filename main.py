import random

# Constants for better readability
# Note: For a more realistic game, you'd have actual card values (J, Q, K as 10, Ace as 1/11)
CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Represents cards 2-10, J, Q, K (Ace handled separately if needed)
DEALER_HIT_STAND_THRESHOLD = 17

def draw_card():
    """Returns a random card value (1-10, simplifying face cards as 10)."""
    # For a simple 1-10 game, can use randint. If using CARD_VALUES, use random.choice.
    # return random.randint(1, 10) # Original logic
    return random.choice(CARD_VALUES) # More realistic for 10s

def calculate_score(cards):
    """Calculates the score of a hand, handling Aces as 1 or 11."""
    score = sum(cards)
    num_aces = cards.count(1) # Assuming 1 represents an Ace initially

    # If there's an Ace and the score is low enough, count it as 11
    while num_aces > 0 and score <= 11: # A common rule for Ace (1 or 11)
        score += 10 # Change one Ace from 1 to 11
        num_aces -= 1
    return score

def deal_initial_cards():
    """Deals two cards to both player and computer."""
    player_cards = []
    comp_cards = []

    for _ in range(2):
        player_cards.append(draw_card())
        comp_cards.append(draw_card())
    
    return player_cards, comp_cards

def player_turn(player_cards):
    """Handles the player's turn to hit or stand."""
    while True:
        player_score = calculate_score(player_cards)
        print(f"Your cards: {player_cards}, Current score: {player_score}")

        if player_score > 21:
            print("You busted!")
            return "Bust" # Player busts
        
        hit_choice = input("Do you want to hit? (y/n): ").lower()
        if hit_choice == "y":
            new_card = draw_card()
            player_cards.append(new_card)
            print(f"You drew a {new_card}.")
        elif hit_choice == "n":
            return "Stand" # Player stands
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def comp_turn(comp_cards):
    """Handles the computer's turn to hit or stand."""
    print(f"\nComputer's turn. Initial cards: {comp_cards}")
    while calculate_score(comp_cards) < DEALER_HIT_STAND_THRESHOLD:
        new_card = draw_card()
        comp_cards.append(new_card)
        print(f"Computer hits and draws a {new_card}.")
        print(f"Computer's cards: {comp_cards}")
    
    comp_score = calculate_score(comp_cards)
    print(f"Computer's final cards: {comp_cards}, Final score: {comp_score}")
    if comp_score > 21:
        print("Computer busted!")
        return "Bust"
    else:
        return "Stand"

def determine_winner(player_cards, comp_cards):
    """Determines the winner of the round."""
    player_score = calculate_score(player_cards)
    comp_score = calculate_score(comp_cards)

    print(f"\n--- Final Results ---")
    print(f"Your hand: {player_cards}, Score: {player_score}")
    print(f"Computer's hand: {comp_cards}, Score: {comp_score}")

    if player_score > 21:
        return "You Busted! You Lose."
    elif comp_score > 21:
        return "Computer Busted! You Win!"
    elif player_score == comp_score:
        return "It's a Push (Tie)!"
    elif player_score > comp_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_blackjack():
    """Main function to run the Blackjack game."""
    print("Welcome to Blackjack!")
    
    while True:
        play_choice = input("Do you want to play a game of Blackjack? (y/n): ").lower()
        if play_choice == "n":
            print("Thanks for playing!")
            break
        elif play_choice == "y":
            player_cards, comp_cards = deal_initial_cards()
            
            print(f"\nYour cards: {player_cards}, Current score: {calculate_score(player_cards)}")
            print(f"Computer's first card: [{comp_cards[0]}, _]") # Only show one of computer's cards

            # Check for initial Blackjacks
            player_score_initial = calculate_score(player_cards)
            comp_score_initial = calculate_score(comp_cards)

            if player_score_initial == 21 and comp_score_initial == 21:
                print("Both have Blackjack! It's a Push (Tie)!")
            elif player_score_initial == 21:
                print("You have Blackjack! You Win!")
            elif comp_score_initial == 21:
                print("Computer has Blackjack! You Lose!")
            else:
                # Player's turn
                player_status = player_turn(player_cards)
                
                # If player busts, game ends, no computer turn needed
                if player_status == "Bust":
                    print(determine_winner(player_cards, comp_cards))
                    continue # Skip to next game loop iteration

                # Computer's turn
                comp_status = comp_turn(comp_cards)

                # Determine final winner
                print(determine_winner(player_cards, comp_cards))

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Start the game
if __name__ == "__main__":
    play_blackjack()