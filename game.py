from deck import Deck
from hand import Hand

class Game:
  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games would you like to play? "))
      except:
        print("You must enter a number.")

    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle()

      player = Hand()
      dealer = Hand(dealer=True)

      for _ in range(2):
        player.add_card(deck.deal(1))
        dealer.add_card(deck.deal(1))

      print()
      print('*' * 30)
      print(f"Game {game_number} of {games_to_play}")
      player.display()
      dealer.display()

      if self.check_winner(player, dealer):
        continue

      choice = ""
      while player.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please choose 'Hit' or 'Stand': ").lower()
        print()
        while choice not in ["s", "h", "hit", "stand"]:
          choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
          print()
        if choice in ["hit", "h"]:
          player.add_card(deck.deal())
          player.display()

      if self.check_winner(player, dealer):
        continue

      player_value = player.get_value()
      dealer_value = dealer.get_value()

      while dealer_value <= 17:
        dealer.add_card(deck.deal())
        dealer_value = dealer.get_value()

      dealer.display(show_all_dealer_cards=True)

      if self.check_winner(player, dealer):
        continue

      print("Final Results:")
      print("\tYour hand: ", player_value)
      print("\tDealer's hand: ", dealer_value)

      self.check_winner(player, dealer, game_over=True)

    print("\nThanks for playing!")

  def check_winner(self, player, dealer, game_over=False):
    if not game_over:
      if player.get_value() > 21:
        print("You're bust! Dealer wins! 😭")
        return True
      elif dealer.get_value() > 21:
        print("Dealer's bust! You wins! 😀")
        return True
      elif player.is_blackjack() and dealer.is_blackjack():
        print("Both player's have blackjack. Tie! 😑")
        return True
      elif player.is_blackjack():
        print("You got a blackjack, congrats! 😀")
        return True
      elif dealer.is_blackjack():
        print("Dealer got a blackjack, better luck next time! 😭")
        return True
    else:
      if player.get_value() > dealer.get_value():
        print("You win! 😀")
      elif player.get_value() == dealer.get_value():
        print("It's a Tie! 😑")
      else:
        print("Dealer wins! 😭")
      return True
    return False
