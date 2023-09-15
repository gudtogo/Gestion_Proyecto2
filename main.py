from Models.Player import Player
from Models.Token import Token
from Models.Game import Game
from Models.Board import Board
from time import sleep
import random
import os

def main():
    # Inicialización de la partida
    game_board = Board()
    game_board.create_board()
    players = int(input("Cuántos jugadores juegan? 2-4"))
    game = Game(players)
    list_players = game.players
    tokens = [["","","",""],["","","",""],["","","",""],["","","",""]]
    for i in range(len(list_players)): 
        tokens[i]= list_players[i].tokens

    actual_player= game.check_turns(list_players)

    count = 0 
    while True:
        # Obtener el jugador actual
        actual_player = get_player_by_color(list_players, actual_player)
        set_of_plays = [6,6,6,6,6,6,2,6,6,6,6,6,6,6,6,6,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]
        while True:
            # Obtener las listas de tokens de cada color
            Rt = list_players[0].tokens 
            Bt = list_players[1].tokens
            Yt = list_players[2].tokens if len(list_players) > 2 else ["","","",""]
            Gt = Gt = list_players[3].tokens if len(list_players) > 3 else ["","","",""]          
            # Tirar el dado
            dice = set_of_plays[count]
            print("El jugador", actual_player.color, "tira el número:", dice)
            road = game_board.road(actual_player.color)
            # Movimiento de tokens
            
            print(f"actual player TURN!: {actual_player.turn}")
            print(f"play count: {count}")

            if dice in (1, 6):
                token = get_available_or_boxed_token(actual_player, game_board,dice,Rt, Bt, Gt,Yt, game)
            else:
                if actual_player.available_tokens() != False:
                    token = actual_player.available_tokens()
                    move_token(token,dice,game_board,Rt,Bt,Gt,Yt,road, actual_player, game)
                count += 1
                break
            count += 1
            
        # Cambiar al siguiente jugador
        actual_player = game.next_player(actual_player.color, list_players)
        print("Ahora le toca al jugador color:", actual_player)
       
        sleep(5)

def get_player_by_color(players, color):
    return next((p for p in players if p.color == color), None)

def get_available_or_boxed_token(player, game_board, dice,Rt, Bt, Gt,Yt, game):
    road = game_board.road(player.color)
    if not player.available_tokens(): # saca tokens de la caja 
        token = player.box_token()
        if token:
            token.exit_box(road[0])
            player.turn += 1
            game_board.print_board(Rt, Bt, Gt,Yt)
    elif not player.box_token():                    #si no hay tokens en la caja
        token = player.available_tokens()           # token aleatorio
        if token:
            move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road, player, game)
    else:
        selec = random.randint(0, 1)
        if selec == 0:
            token = player.box_token()
            token.exit_box(road[0])
            game_board.print_board(Rt, Bt, Gt,Yt)
        else:
            token = player.available_tokens()
            if token:
                move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road, player, game)
    return token

def move_token(token, dice, game_board, Rt, Bt, Gt, Yt, road, actual_player, game):
    for i in range(dice):
        if token.state == "coronate":
            token.move_in_group(actual_player.tokens, road, game_board, Rt, Bt, Gt, Yt)
        else:
            token.move(road)
        
        os.system("cls")  # Cambiar a "clear" en Unix
        game_board.print_board(Rt, Bt, Gt, Yt)
        sleep(1) 

    actual_player.turn += 1
    token.coronate(actual_player.tokens) # coronar tokens en la misma posición
    did_eat_something, token = token.did_eat_something(actual_player, game)
    
    if did_eat_something:
        game_board.print_board(Rt, Bt, Gt, Yt)
        sleep(1) 

if __name__ == "__main__":
    main()
