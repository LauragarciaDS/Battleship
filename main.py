import random
from game_logic import Game_Logic
from player import Player
from machine_player import  Machine_player


welcome = """\
    \n
Welcome to the game of Battleship!

You will get a board with your ships placed randomly,
and an empty one with your opponent's HIDDEN ships, also randomly placed.
You will have to enter coordinates, such as: B3
to try to sink all the opponent's ships.
If you hit, you will have a chance to roll again.
If you miss, the turn will pass to your enemy, who will shot at your ships to try and sink them.
To win you have to sink all his ships before he sinks yours.

If you want to quit the game,
You will have to select option 3.

Good luck!
"""


print(welcome)

#* Esta variable pregunta por el nombre del jugador
player_name = input("Please enter your name : ")

player_1 = Player("normal",player_name)
pc_player = Machine_player("normal",player_1)
game = Game_Logic(player_1,pc_player)

game.create_turns()
game.place_ship_board()
game.print_boards()
game.game_running() #<------ metodo que corre el juego con el while





