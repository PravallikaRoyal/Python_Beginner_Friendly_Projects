import random
import art
logo = art.logo

def card_selection():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):
    if user_score == comp_score:
        return "draw"
    elif user_score == 0:
        return "Win with a blackjack"
    elif comp_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif comp_score > 21:
        return "Opponent went over, you win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    comp_Score = -1
    user_score = -1
    
    is_game_over = False
    for i in range(2):
        user_cards.append(card_selection())
        comp_cards.append(card_selection())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_Score = calculate_score(comp_cards)
        print(f"your cards {user_cards}, current_score={user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_Score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type yes to get another card, type no to pass:")
            if user_should_deal == "yes":
                user_cards.append(card_selection())
            else:
                is_game_over = True
    
    while comp_Score != 0 and comp_Score<17:
        comp_cards.append(card_selection())
        comp_Score = calculate_score(comp_cards)
        print(f"your final cards : {user_cards}, final_score = {user_score}")
        print(f"computer's final cards: {comp_cards},final_score={comp_Score}")
        print(compare(user_score,comp_Score))
        
while input("Do you want to play a game of blackjack? Type yes or no:") == "yes":
        print("\n" *20)
        play_game()




