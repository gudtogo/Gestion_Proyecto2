from Models.Player import Player
from Models.Token import Token
from Models.Game import Game
from Models.Board import Board
from time import sleep
def main():
    game_board = Board()
    game = Game()
    players = int(input("Cuántos jugadores juegan? 2-4"))
    list_players = game.define_players(players)
    actual_player= game.check_turns(list_players)
    print("Comienza jugando el jugador: ", actual_player)

    while True:
        actual_player= game.next_player(actual_player)
        print("Ahora le toca a: ", actual_player)
        sleep(5)


if __name__ == "__main__":
    main()