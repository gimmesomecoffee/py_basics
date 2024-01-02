import random

def user_random_cards():
    return random.sample(cards, 2)

def draw_card(hand):
    card = random.choice(cards)
    hand.append(card)
    return card

def computer_random_cards():
    return random.sample(cards, 1)

def display_game_status(user_hand, cp_hand):
    print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
    print(f"Computer cards: {cp_hand}, Computer score: {sum(cp_hand)}")

# There are no jokers, Jack/Queen/King = 10, the Ace can be counted as 11 or 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = user_random_cards()
cp_hand = computer_random_cards()
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play.lower() == "y":
    display_game_status(user_hand, cp_hand)

    while sum(user_hand) < 21:
        get_card = input("Type 'y' to get another card, 'n' to pass: ")
        if get_card.lower() == 'y':
            new_card = draw_card(user_hand)
            cp_new_card = draw_card(cp_hand)
            print(f"New card for you: {new_card}")
            print(f"Updated cards for you: {user_hand}, current score: {sum(user_hand)}")
            print(f"New computer card: {cp_new_card}")
            print(f"Updated cards for computer: {cp_hand}, Computer score: {sum(cp_hand)}")
        else:
            break

    if sum(user_hand) == 21 or (sum(user_hand) > sum(cp_hand) and sum(user_hand) <= 21):
        print("Congratulations! You won!")
    else:
        print("You lost.")

    print("Final hand for you:", user_hand)
    print("Final score for you:", sum(user_hand))
    print("Final score for computer:", sum(cp_hand))

else:
    print("Bye")