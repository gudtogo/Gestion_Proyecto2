from .Player import Player
import random
from .Token import Token
class Game:

    def define_players(self, num_players):
        colors = ["red", "blue", "green", "yellow"]
        players_list = []
        for i in range(len(colors)):
            if i < num_players:
                player = Player(colors[i], True)
            else:
                player = Player(colors[i], False)
            players_list.append(player)
        return players_list

    

    def checks_higher(self,dic):
        sorted_results = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        highest_result = sorted_results[0][1]
        tied_players = [player for player, result in sorted_results if result == highest_result]
       
        return tied_players

    def define_turns(self, players):
        dice_results = {}
        active_players = [player for player in players if player.play]
        
        for player in active_players:
            number = player.roll_dice()
            print("Jugador", player.color, "saca:", number)
            dice_results[player] = number

        higher_players = self.checks_higher(dice_results)

        return higher_players

    def check_turns(self, players):
        active_players = [player for player in players if player.play]

        while len(active_players) > 1:
            if len(active_players) > 1:
                active_players = self.define_turns(active_players)
        
        return active_players[0].color

    def next_player(self, actual_player, players):
        clockwise = ["green", "red", "blue", "yellow"]
        actual_index = clockwise.index(actual_player)
        available_colors = [player.color for player in players if player.play]

        while True:
            actual_index = (actual_index + 1) % len(clockwise)
            next_color = clockwise[actual_index]
            if next_color in available_colors:
                return next_color

    def check_same_position(self,players,actual_token):
        tokens = []
        for player in players:
            tokens.extend(player.tokens)
        for i, token1 in enumerate(tokens):
            for j, token2 in enumerate(tokens):
                if i != j and token1.position == token2.position and token2!= actual_token:
                    token2.state = "box"
                    token2.position = 0
        return False
