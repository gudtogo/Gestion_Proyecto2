from .Player import Player
import random

class Game:

    def define_players(self,num_players):
        colors = ["red","blue","green","yellow"]
        players_list = []
        for i in range(num_players):
            player = Player(colors[i])
            players_list.append(player)
        return players_list
    

    def checks_higher(self,dic):
        sorted_results = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        highest_result = sorted_results[0][1]
        tied_players = [player for player, result in sorted_results if result == highest_result]
       
        return tied_players

    def define_turns(self,players):
        dice_results = {}
        for player in players:
            number = player.roll_dice()
            print("Jugador ",player.color," saca: ", number)
            dice_results[player] = number

        higher_players = self.checks_higher(dice_results)
       
        return higher_players
            
            
    def check_turns(self, players):
        while len(players)>1:
            if len(players) > 1:
                players = self.define_turns(players)
        return players[0].color

    def next_player(self, actual_player):
        clockwise = ["green", "red", "blue", "yellow"]
        actual_index = clockwise.index(actual_player)
        next_index = (actual_index+ 1) % len(clockwise)
        return clockwise[next_index]
        
           
