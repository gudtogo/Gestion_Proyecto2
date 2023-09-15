import os
from time import sleep
class Token:
    def __init__(self,position,state,color, id): #cada token le corresponde a un jugador, y cada jugador tiene 4 tokens 
        self.position = position
        self.state = state #State puede ser Box (cuando está sin salir en posición inicial), Coronate, o available
        self.color = color
        self.id = id



    def eaten(self,initial_position):
        self.position = initial_position
        self.state = "box"

    def did_eat_something(self, actual_player, game):
        eat_count = 0 
        tokens_eated = []

        for player in game.players:

            tokens_to_check = [obj for obj in player.tokens if obj.id != self.id] # no incluir a si mismo en las fichas que checkear
            
            for token in tokens_to_check:
                if self.position == token.position:
                    token.eaten(0)
                    tokens_eated.append(token)
                    eat_count +=1

        return True, tokens_eated if eat_count > 0 else False

    def coronate(self, player_tokens):
        #Marcar como coronados los tokens en la misma posición
        for token in [obj for obj in player_tokens if obj.id != self.id]:
            if self.position == token.position and (self.position != 0 and token.position != 0):
                token.state = "coronate"
                self.state = "coronate"

    def move_in_group(self, player_tokens, road, game_board, Rt, Bt, Gt, Yt):
        tokens_to_move = [self]

        tokens_to_detect = [obj for obj in player_tokens if obj.id != self.id]
        # Detectar tokens que mover en conjunto
        for player_token in tokens_to_detect:
            if self.position == player_token.position:
                tokens_to_move.append(player_token)

        print(f"tokens_to_detect: {tokens_to_detect}")
        # Mover uno a uno los tokens en conjunto
        for token in tokens_to_move:
            token.move(road)

        print(f"token_to_move togh: {tokens_to_move}")
        game_board.print_board(Rt, Bt, Gt, Yt)
        sleep(1) 


    def move(self,road):
        actual_advance = road.index(self.position)
        actual_advance+= 1
        if actual_advance > len(road):
            print("invalid move")
        else:
            self.position = road[actual_advance]
            


    #def move(self,dice,final_position, initial_position):
    #    if final_position < initial_position:
    #        final_position = final_position*-1
    #    if self.state == "final":
    #        if self.position + dice >= 6:
         #       self.state = "won"

        #elif self.state == "available":
       #     new_position = self.position + dice
      #      if new_position> 52:
     #           new_position -= 52
     #       elif new_position > final_position:
     #           self.state = "final"
     #           new_position = final_position
     #       self.position = new_position
     #   else:
     #       pass
     #   print("se movió al: ", self.position)

    def exit_box(self,initial_position):
        self.state = "available"
        self.position = initial_position
        print("El jugador saca un token, empieza en posición",self.position)

    