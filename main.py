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

    actual_player= game.check_turns(list_players)

    while True:
        
        actual_player = get_player_by_color(list_players, actual_player)
        
        input("Presiona Enter para pasar al siguiente turno...")
        while True:
            # Obtener las listas de tokens de cada color
            Rt = list_players[0].tokens
            Bt = list_players[1].tokens
            Yt = list_players[2].tokens if len(list_players) > 2 else ["","","",""]
            Gt = list_players[3].tokens if len(list_players) > 3 else ["","","",""]  
           
            # Tirar el dado
            dice = actual_player.roll_dice()
            print("El jugador", actual_player.color, "tira el número:", dice)
            
            road = game_board.get_player_road(actual_player.color) #Se obtiene el camino que sigue el jugador actual
            
            # Movimiento de tokens
            if dice in (1, 6):
                token = get_available_or_boxed_token(road,actual_player, game_board,dice,Rt, Bt, Gt,Yt,game,list_players)
            else:
                if actual_player.available_tokens() != False:
                    token = actual_player.available_tokens()
                    move_token(token,dice,game_board,Rt,Bt,Gt,Yt,road,game,list_players)
                break



        # Cambiar al siguiente jugador
        if not token_data(actual_player):
            print("El juego ha terminado")
            print("Gana el jugador: ",actual_player.color)
            break
        actual_player = game.next_player(actual_player.color, list_players)
        print("Ahora le toca al jugador color:", actual_player)
       


def get_player_by_color(players, color):
    return next((p for p in players if p.color == color), None)


def get_available_or_boxed_token(road,player, game_board, dice,Rt, Bt, Gt,Yt,game,list_players):
    if not player.available_tokens(): #Si no hay tokens fuera de la caja
        token = player.box_token()
        token.exit_box(road[0])
        game_board.print_board(Rt, Bt, Gt,Yt)

    elif not player.box_token():  #Si no hay tokes dentro de la caja
        token = player.available_tokens()
        if token:
            move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road,game,list_players)
    else:                            #Si hay tokens dentro de la caja pero también hay tokens fuera
        selec = random.randint(0, 1) #Se elije una opción al azar
        if selec == 0:
            token = player.box_token()
            token.exit_box(road[0])
            game_board.print_board(Rt, Bt, Gt,Yt)
        else:
            token = player.available_tokens()
            if token:
                move_token(token,dice,game_board,Rt, Bt, Gt,Yt,road,game,list_players)
    return token


def move_coronated_token(list_players,actual_token,Rt,Bt,Gt,Yt,dice,road,game,game_board):
    coronated_tokens = game.get_coronated_tokens(actual_token,Rt,Bt,Gt,Yt)   
    for step in range(dice):
        for token in coronated_tokens:
            token.move(road,game_board)
        os.system("cls")
        print("AVANZANDO tokens coronados: ", dice)
        game_board.print_board(Rt, Bt, Gt, Yt)
        sleep(1)
    if game.tokens_same_position(list_players,token):
            os.system("cls")
            print(token.state)
            game_board.print_board(Rt, Bt, Gt, Yt)

def move_token(token, dice, game_board, Rt, Bt, Gt, Yt, road,game,list_players):
    if "coronate" in token.state:
        move_coronated_token(list_players,token,Rt,Bt,Gt,Yt,dice,road,game,game_board)
        
    else:
        for i in range(dice):
            token.move(road,game_board)
            os.system("cls")  # Cambiar a "clear" en Unix
            print("AVANZANDO: ", dice)
            game_board.print_board(Rt, Bt, Gt, Yt)
            sleep(1) 

        if game.tokens_same_position(list_players,token):
            sleep(2)
            os.system("cls")
            print(token.state)
            game_board.print_board(Rt, Bt, Gt, Yt)
           
            

def token_data(actual_player):
    count = 1
    winner = 0
    print("JUGADOR : ",actual_player.color)
    for p in actual_player.tokens:
        print("Token ",count," = ",p.state,p.position)
        count+=1
        if isinstance(p.position,str):
            if "6" in p.position:
                winner += 1
    if winner == 4:
        return False
    return True
 


if __name__ == "__main__":
    main()
