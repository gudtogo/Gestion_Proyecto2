from Models.Player import Player
from Models.Token import Token
from Models.Game import Game
from Models.Board import Board
from time import sleep
def main():
#-----SE DEFINEN PARAMETROS COMO JUGADOES Y QUIÉN EMPIEZA ---------
    game_board = Board()
    game = Game()
    players = int(input("Cuántos jugadores juegan? 2-4"))
    list_players = game.define_players(players)
    actual_player= game.check_turns(list_players)
    
#-----------INICIO DE LA PARTIDA-------------------

    print("Comienza jugando el jugador color: ", actual_player) 
    while True:
        for p in list_players:
            if p.color == actual_player:
                actual_player = p
                break
        
        while True:
            dice = actual_player.roll_dice()
            print("El jugador tira el número: ", dice)

            if dice == 1 or dice == 6:
                if actual_player.available_tokens() == False: #Si no hay tokens disponibles para avanzar
                    token = actual_player.box_token()       #Saca uno del tablero
                    token.exit_box(game_board.initial_position(actual_player.color))
                else:
                    token = actual_player.available_tokens()    #Si hay tokens disponibles para avanzar
                    token.move(dice, game_board.final_position(actual_player.color)) #Lo hace avanzar
            else:
                break
        token = actual_player.available_tokens()
        if token != False:
            token.move(dice, game_board.final_position(actual_player.color)) #Lo hace avanzar


        actual_player= game.next_player(actual_player.color,list_players)     
        print("Ahora le toca el jugador color: ", actual_player)
        sleep(5)


if __name__ == "__main__":
    main()