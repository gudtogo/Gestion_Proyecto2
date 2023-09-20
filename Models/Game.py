from .Player import Player
import random

from time import sleep
class Game:
    def __init__(self):
        self.winners = 0

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

    def tokens_same_position(self, players, actual_token):
        color_mapping = {
            "green_2": "💚",  #Simbolo para 2 coronados
            "red_2": "❤️ ",
            "yellow_2": "💛",
            "blue_2": "💙",
            "green_3": "📗",  #Simbolo para 3 coronados
            "red_3": "📕",
            "yellow_3": "📒",
            "blue_3": "📘",
            "green_4": "✅", #Simbolo para 4 coronados
            "red_4": "📛",
            "yellow_4": "⚠️",
            "blue_4": "🚹",             
        }
        var = False
        same_color_tokens = []

        # Obtener todos los tokens de todos los jugadores
        all_tokens = [actual_token]
        for player in players:
            all_tokens.extend(player.tokens)

        # Buscar tokens en la misma posición y del mismo color
        token_igual = False
        for token2 in all_tokens:
            if token2 != actual_token:
                if token2.position == actual_token.position:
                    if token2.color == actual_token.color:
                        if token2 not in same_color_tokens:
                            same_color_tokens.append(token2)
                        if actual_token not in same_color_tokens:
                            same_color_tokens.append(actual_token)
                    else:
                        token2.state = "box"
                        token2.position = 0
                        token2.simbol = token2.define_simbol(token2.color)
                    var = True
                    print(token2.color,actual_token.color)

        total = len(same_color_tokens)
        for t in range(len(same_color_tokens)):
            same_color_tokens[t].state = "coronate"+str(total)

        for t in same_color_tokens:
            if t.color == "red" and "2" in t.state:
                t.simbol = color_mapping["red_2"]
            if t.color == "red" and "3" in t.state:
                t.simbol = color_mapping["red_3"]
            if t.color == "red" and "4" in t.state:
                t.simbol = color_mapping["red_4"]
            if t.color == "blue" and "2" in t.state:
                t.simbol = color_mapping["blue_2"]
            if t.color == "blue" and "3" in t.state:
                t.simbol = color_mapping["blue_3"]
            if t.color == "blue" and "4" in t.state:
                t.simbol = color_mapping["blue_4"]
            if t.color == "yellow" and "2" in t.state:
                t.simbol = color_mapping["yellow_2"]
            if t.color == "yellow" and "3" in t.state:
                t.simbol = color_mapping["yellow_3"]
            if t.color == "yellow" and "4" in t.state:
                t.simbol = color_mapping["yellow_4"]
            if t.color == "green" and "2" in t.state:
                t.simbol = color_mapping["green_2"]
            if t.color == "green" and "3" in t.state:
                t.simbol = color_mapping["green_3"]
            if t.color == "green" and "4" in t.state:
                t.simbol = color_mapping["green_4"]
        return same_color_tokens

    def get_coronated_tokens(self,token,Rt,Bt,Gt,Yt):
        var = False
        coronated_tokens = []
        if token in Rt:
            tokens = Rt
        elif token in Bt:
            tokens = Bt
        elif token in Gt:
            tokens = Gt
        elif token in Yt:
            tokens = Yt
        for t in tokens: #ve si el jugador tiene tokens coronados
            if token.state == t.state:
                coronated_tokens.append(t)
        return coronated_tokens
    
