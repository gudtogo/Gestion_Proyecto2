from Models.Player import Player
from Models.Token import Token
from Models.Game import Game
from Models.Board import Board

def main():
    game_board = Board()
    game = Game()
    players = int(input("Cuántos jugadores juegan? 2-4"))
    list_players = game.define_players(players)
    starting_player = game.check_turns(list_players)
    print("Comienza jugando el jugador: ", starting_player)




if __name__ == "__main__":
    main()