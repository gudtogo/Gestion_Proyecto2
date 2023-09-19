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
    game = Game()
    players = int(input("Cuántos jugadores juegan? 2-4"))
    list_players = game.define_players(players)
    tokens = [["","","",""],["","","",""],["","","",""],["","","",""]]
    for i in range(len(list_players)): 
        tokens[i]= list_players[i].tokens

    actual_player= game.check_turns(list_players)

    while True:
        # Obtener el jugador actual
        actual_player = get_player_by_color(list_players, actual_player)

        while True:
            # Obtener las listas de tokens de cada color
            Rt = list_players[0].tokens
            Bt = list_players[1].tokens
            Yt = list_players[2].tokens if len(list_players) > 2 else ["","","",""]
            Gt = Gt = list_players[3].tokens if len(list_players) > 3 else ["","","",""]          
            # Tirar el dado
            dice = actual_player.roll_dice()
            print("El jugador", actual_player.color, "tira el número:", dice)
            road = game_board.road(actual_player.color)
            # Movimiento de tokens
            if dice in (1, 6):
                token = get_available_or_boxed_token(actual_player, game_board,dice,Rt, Bt, Gt,Yt,game,list_players)
            else:
                if actual_player.available_tokens() != False:
                    token = actual_player.available_tokens()
                    move_token(token,dice,game_board,Rt,Bt,Gt,Yt,road,game,list_players)
                break



        # Cambiar al siguiente jugador
        actual_player = game.next_player(actual_player.color, list_players)
        print("Ahora le toca al jugador color:", actual_player)
       
        sleep(5)

def get_player_by_color(players, color):
    return next((p for p in players if p.color == color), None)

def get_available_or_boxed_token(player, game_board, dice,Rt, Bt, Gt,Yt,game,list_players):
    road = game_board.road(player.color)
    if not player.available_tokens():
        token = player.box_token()
        if token:
            token.exit_box(road[0])
            game_board.print_board(Rt, Bt, Gt,Yt)
    elif not player.box_token():
        token = player.available_tokens()
        if token:
            move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road,game,list_players)
    else:
        selec = random.randint(0, 1)
        if selec == 0:
            token = player.box_token()
            token.exit_box(road[0])
            game_board.print_board(Rt, Bt, Gt,Yt)
        else:
            token = player.available_tokens()
            if token:
                move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road,game,list_players)
    return token

def move_token(token, dice, game_board, Rt, Bt, Gt, Yt, road,game,list_players):
    for i in range(dice):
        token.move(road)
        os.system("cls")  # Cambiar a "clear" en Unix
        print("AVANZANDO: ", dice)
        game_board.print_board(Rt, Bt, Gt, Yt)
        sleep(1) 
    os.system("cls")
    game.check_same_position(list_players,token)
    game_board.print_board(Rt, Bt, Gt, Yt)

if __name__ == "__main__":
    main()
