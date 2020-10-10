"""
  BLACKJACK GAME with OOP Python
Basic Blackjack Rules:

The goal of blackjack is to beat the dealer's hand without going over 21.
Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
Each player starts with two cards, one of the dealer's cards is hidden until the end.
To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
If you are dealt 21 from the start (Ace & 10), you got a blackjack.
Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
Dealer will hit until his/her cards total 17 or higher.
Doubling is like a hit, only the bet is doubled and you only get one more card.
Split can be done when you have two of the same card - the pair is split into two hands.
Splitting also doubles the bet, because each new hand is worth the original bet.
You can only double/split on the first move, or first move of a hand created by a split.
You cannot play on two aces after they are split.
You can double on a hand resulting from a split, tripling or quadrupling you bet.

"""

from random import shuffle


class Dealer:
    def __init__(self):
        self.hand = []
        self.total = 0

    def get_total(self):
        self.total = 0
        for card in self.hand:
            self.total += card['value']

        if self.total == 21:
            self.is_blackjack = True

    def draw_card(self, card):
        self.hand.append(card)

    def show_hands(self):
        print(f'\nDealer Hand: \n\t{self.hand[0]["name"]} \n\tUnknown Card')

    def draw_two_cards(self, cards):
        self.hand = cards


class Player(Dealer):
    def __init__(self, chips):
        Dealer.__init__(self)
        self.bet = 0
        self.chips = chips
        self.is_blackjack = False

    def bet_chips(self):
        while True:
            print(f'\n\nCurrent Chip:${self.chips}')
            print('Only amounts divisible by 100 are valid\n')
            amount = int(input(f'Please enter your bet: '))

            if(amount % 100 == 0 and amount <= self.chips):
                break
            else:
                print('Enter a valid amount!')

        self.bet = amount

    def manage_chips(self, has_won):
        if has_won:
            self.chips += self.bet
        else:
            self.chips -= self.bet

    def show_hands(self):
        print('Your Hand: ')
        for card in self.hand:
            print(f'\t{card["name"]}')
        print(f'total:{self.total}')

    def reset_bet(self):
        self.bet = 0


class Deck:
    card_types = ['Diamond', 'Heart', 'Spade', 'Flower']
    card_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card_faces = ['Jack', 'Queen', 'King']

    # create deck of cards
    def __init__(self):
        self.deck = []

        self.build_deck()

    def build_deck(self):
        for type in self.card_types:
            for num in self.card_numbers:
                name = f'{num} of {type}s'
                value = num

                if num == 1:
                    name = f'Ace of {type}s'
                    value = 11
                elif(num > 10):
                    name = f'{self.card_faces[num - 11]} of {type}s'
                    value = 10
                # create card
                self.deck.append({
                    'name': name,
                    'value': value
                })
        # print(self.deck)
        # print(len(self.deck))

    def shuffle_deck(self):
        shuffle(self.deck)
        # for card in self.deck:
        #     print(card)

    def draw_two_cards(self):
        card_one = self.deck.pop(0)
        card_two = self.deck.pop(0)
        # print(len(self.deck))
        return [card_one, card_two]

    def draw_card(self):
        return self.deck.pop(0)


class Game:
    def __init__(self):
        self.is_playing = True
        print("""
        |============================================|
        |                                            |
        |  Welcome to Blackjack!                     |
        |  Enter 'exit' if you want to quit the game!|
        |                                            |
        |============================================|
        """)

    def get_player_response(self):
        print('Enter any other number to quit game')
        response = input('\n[0]HIT or [1]STAND:(0 or 1): ')
        return response


# Initialize Game
blackjack = Game()
deck = Deck()
# shuffle deck
deck.shuffle_deck()
# initialize players
player = Player(2000)
dealer = Dealer()

while player.chips > 0:
    # player bet
    if player.bet == 0:
        player.bet_chips()
        deck.shuffle_deck()
        # Draw new cards
        player.draw_two_cards(deck.draw_two_cards())
        dealer.draw_two_cards(deck.draw_two_cards())

    # check if player is blackjack

    if player.is_blackjack:
        print('You Win! It\'s a BLACKJACK')
        player.manage_chips(True)

    # GET TOTAL

    player.get_total()
    dealer.get_total()

    player.show_hands()
    dealer.show_hands()

    player_answer = blackjack.get_player_response()

    # HIT get another card for the player
    if(player_answer == '0'):
        player.draw_card(deck.draw_card())
        player.get_total()
    # STAND compare value
    elif player_answer == '1':
        if len(player.hand) > len(dealer.hand):
            # add card equivalent to drawn cards
            difference = len(player.hand) - len(dealer.hand)

            for _ in difference:
                dealer.draw_card(deck.draw_card())

            dealer.get_total()

        # compare cards
        if(player.total > dealer.total):
            print('\n============================\n')
            print('You Win!')
            print(f'Player: {player.total} vs Dealer: {dealer.total}')
            player.manage_chips(True)
            print('\n============================\n')
        else:
            print('\n============================\n')
            print('Dealer Wins!')
            print(f'Player: {player.total} vs Dealer: {dealer.total}')
            player.manage_chips(False)
            print('\n============================\n')

        player.reset_bet()
    elif player.total > 21:
        print('\n============================\n')
        print('Dealer Wins!')
        print('Player exceeds 21')
        print('\n============================\n')

    else:
        print('EXIT GAME!')
        break


print('GAME ENDED')
# Create a card
# Create a deck of cards
# shuffle a card
# Place a bet
# Create a players hand and dealer's hand
# two cards each , one seen for dealer
# ask if hit or stand
# if hit, add one card to players hand
# stand, end turn
# add number of cards added to player to dealer's hands
# Compare dealer and player , higher wins
# if current card value is over 21 , dealer wins
# if value is 21 , then blackjack , check once the game starts
#
