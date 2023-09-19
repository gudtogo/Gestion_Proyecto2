from .Player import Player
from time import sleep
import os

box_r1 = "Rt1"
box_r2 = "Rt2"
box_r3 = "Rt3"
box_r4 = "Rt4"
box_b1 = "Bt1"
box_b2 = "Bt2"
box_b3 = "Bt3"
box_b4 = "Bt4"
box_g1 = "Gt1"
box_g2 = "Gt2"
box_g3 = "Gt3"
box_g4 = "Gt4"
box_y1 = "Yt1"
box_y2 = "Yt2"
box_y3 = "Yt3"
box_y4 = "Yt4"

start_r = 14
start_b = 27
start_g = 1
start_y = 40

red_road = [14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,1,2,3,4,5,6,7,8,9,10,11,12]
blue_road = [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
green_road = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
yellow_road = [40,41,42,43,44,45,46,47,48,49,50,51,52,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]


class Board:
    def __init__(self,table = []):
        self.table = []

    def final_road(self,color):
        if color == "red":
            return ["R1","R2","R3","R4","R5","R6"]
        elif color == "blue":
            return ["B1","B2","B3","B4","B5","B6"]
        elif color == "green":
            return ["G1","G2","G3","G4","G5","G6"]
        elif color == "yellow":
            return ["Y1","Y2","Y3","Y4","Y5","Y6"]

    def create_board(self):
        yf =["Y1","Y2","Y3","Y4","Y5","Y6"]
        rf=["R1","R2","R3","R4","R5","R6"]
        bf =["B1","B2","B3","B4","B5","B6"]
        gf =["G1","G2","G3","G4","G5","G6"]
        self.table = [["🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ,  11 , 12  , 13  , "🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ],
                      ["🟫","⬜", "⬜" , "⬜" , "⬜" , "🟫" ,  10 ,rf[0], 14  , "🟫" , "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ],
                      ["🟫", "Gt1" , "⬜" , "Gt3" , "⬜" , "🟫" ,  9  ,rf[1], 15  , "🟫" , "Rt1" , "⬜" , "Rt3" , "⬜" , "🟫" ],
                      ["🟫", "Gt2" , "⬜" , "Gt4" , "⬜" , "🟫" ,  8  ,rf[2], 16  , "🟫" , "Rt2" , "⬜" , "Rt4" , "⬜" , "🟫" ],
                      ["🟫", "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ,  7  ,rf[3], 17  , "🟫" , "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ],
                      ["🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ,  6  ,rf[4], 18  , "🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ],
                      [52 ,  1  ,  2  ,  3  ,  4  ,  5  , "⬛" ,rf[5], "⬛" ,  19 , 20  , 21  , 22 , 23   , 24  ],
                      [51 ,gf[0],gf[1],gf[2],gf[3],gf[4],gf[5], "⬛" ,bf[5],bf[4],bf[3],bf[2],bf[1],bf[0], 25  ],
                      [50 ,  49 ,  48 ,  47 ,  46 ,  45 , "⬛" ,yf[5], "⬛" , 31  , 30  , 29  , 28  , 27  , 26  ],
                      ["🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ,  44 ,yf[4], 32  , "🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ],
                      ["🟫", "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ,  43 ,yf[3], 33  , "🟫" , "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ],
                      ["🟫", "Yt2" , "⬜" , "Yt3" , "⬜" , "🟫" ,  42 ,yf[2], 34  , "🟫" , "Bt1" , "⬜" , "Bt3" , "⬜" , "🟫" ],
                      ["🟫", "Yt1" , "⬜" , "Yt4" , "⬜" , "🟫" ,  41 ,yf[1], 35  , "🟫" , "Bt2" , "⬜" , "Bt4" , "⬜" , "🟫" ],
                      ["🟫", "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ,  40 ,yf[0], 36  , "🟫" , "⬜" , "⬜" , "⬜" , "⬜" , "🟫" ],
                      ["🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ,  39 , 38  , 37  , "🟫", "🟫" , "🟫" , "🟫" , "🟫" , "🟫" ],
                      ]

    def get_player_road(self,color):
        if color == "red":
            return red_road
        if color == "yellow":
            return yellow_road
        if color == "blue":
            return blue_road
        if color == "green":
            return green_road 


    def token_in_box(self,lt,index):
        if lt[index].state == "box":
            return True
        else:
            return False


    def no_token_there(self, Rt, Bt, Yt, Gt, cell):
        # Verificar si cell no está en ninguna de las listas de posiciones
        if (cell not in [t.position for t in Rt] and
            cell not in [t.position for t in Bt] and
            cell not in [t.position for t in Yt] and
            cell not in [t.position for t in Gt]):
            return True
        else:
            return False
        
    def is_coronated(self,token):
        if "coronated" in token.state:
            print("EL TOKEN DE COLOR", token.color, "ESTA CORONADO Y ESTA BIEN EN LA FUNCIÓN BOARD")
            return True
        else:
            return False

    def return_simbol(self,token):
        if token.color == "red":
            print(token.state)
            if "2" in token.state:
                return "❤️"
            elif "3" in token.state:
                return "📕"
            elif "4" in token.state:
                return "📛"
        elif token.color == "blue":
            if "2" in token.state:
                return "💙"
            elif "3" in token.state:
                return "📘"
            elif "4" in token.state:
                return "🚹"
        elif token.color == "green":
            if "2" in token.state:
                return "💚"
            elif "3" in token.state:
                return "📗"
            elif "4" in token.state:
                return "✅"
        elif token.color == "yellow":
            if "2" in token.state:
                return "💛"
            elif "3" in token.state:
                return "📒"
            elif "4" in token.state:
                return "⚠️"


    def print_board(self, Rt, Bt, Yt, Gt):
        color_mapping = {
            "Rt1": "🔴",
            "Rt2": "🔴",
            "Rt3": "🔴",
            "Rt4": "🔴",
            "Bt1": "🔵",
            "Bt2": "🔵",
            "Bt3": "🔵",
            "Bt4": "🔵",
            "Yt1": "🟡",
            "Yt2": "🟡",
            "Yt3": "🟡",
            "Yt4": "🟡",
            "Gt1": "🟢",
            "Gt2": "🟢",
            "Gt3": "🟢",
            "Gt4": "🟢",
            "Y1" : "🟨",
            "Y2" : "🟨",
            "Y3" : "🟨",
            "Y4" : "🟨",
            "Y5" : "🟨",
            "Y6" : "🟨",
            "R1" : "🟥",
            "R2" : "🟥",
            "R3" : "🟥",
            "R4" : "🟥",
            "R5" : "🟥",
            "R6" : "🟥",
            "B1" : "🟦",
            "B2" : "🟦",
            "B3" : "🟦",
            "B4" : "🟦",
            "B5" : "🟦",
            "B6" : "🟦",
            "G1" : "🟩",
            "G2" : "🟩",
            "G3" : "🟩",
            "G4" : "🟩",
            "G5" : "🟩",
            "G6" : "🟩",
            "green_2": "💚",  #Simbolo para 2 coronados
            "red_2": "❤️",
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
        for index in range(4):
            if not self.token_in_box(Rt, index):
                color_mapping[f"Rt{index + 1}"] = "⬜"
            if not self.token_in_box(Bt, index):
                color_mapping[f"Bt{index + 1}"] = "⬜"
            if not self.token_in_box(Yt, index):
                color_mapping[f"Yt{index + 1}"] = "⬜"
            if not self.token_in_box(Gt, index):
                color_mapping[f"Gt{index + 1}"] = "⬜"

        for row in self.table:
            for cell in row:
                do = True
                token_color = None

                if isinstance(cell, int):
                    # Si la celda es un entero, se trata de una posición de inicio/fin
                    if cell == Rt[0].position:
                        token_color =  Rt[0].simbol
                        do = False
                    if cell == Rt[1].position:
                        token_color =  Rt[1].simbol
                        do = False
                    if cell == Rt[2].position:
                        token_color =  Rt[2].simbol
                        do = False
                    if cell == Rt[3].position:
                        token_color =  Rt[3].simbol
                        do = False
                    if cell == Gt[0].position:
                        token_color = Gt[0].simbol
                        do = False
                    if cell == Gt[1].position:
                        token_color = Gt[1].simbol
                        do = False
                    if cell == Gt[2].position:
                        token_color = Gt[2].simbol
                        do = False
                    if cell == Gt[3].position:
                        token_color = Gt[3].simbol
                        do = False
                    if cell == Bt[0].position:
                        token_color = Bt[0].simbol
                        do = False
                    if cell == Bt[1].position:
                        token_color = Bt[1].simbol
                        do = False
                    if cell == Bt[2].position:
                        token_color = Bt[2].simbol
                        do = False
                    if cell == Bt[3].position:
                        token_color = Bt[3].simbol
                        do = False
                    if cell == Yt[0].position:
                        token_color = Yt[0].simbol
                        do = False
                    if cell == Yt[1].position:
                        token_color = Yt[1].simbol
                        do = False
                    if cell == Yt[2].position:
                        token_color = Yt[2].simbol
                        do = False
                    if cell == Yt[3].position:
                        token_color = Yt[3].simbol
                        do = False
                    if cell == 14 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟥"
                        do = False
                    elif cell == 1 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟩"
                        do = False     
                    elif cell == 27 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟦"
                        do = False
                    elif cell == 40 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟨"
                        do = False
                    else:
                        if do:
                            token_color = "⬜"
                    if token_color is not None:
                        print(token_color, end=" ")
                else:
                    if cell in color_mapping:
                        token_color = color_mapping[cell]
                        
                    if cell == Rt[0].position:
                        token_color =  Rt[0].simbol
                        do = False
                    if cell == Rt[1].position:
                        token_color =  Rt[1].simbol
                        do = False
                    if cell == Rt[2].position:
                        token_color =  Rt[2].simbol
                        do = False
                    if cell == Rt[3].position:
                        token_color =  Rt[3].simbol
                        do = False
                    if cell == Gt[0].position:
                        token_color = Gt[0].simbol
                        do = False
                    if cell == Gt[1].position:
                        token_color = Gt[1].simbol
                        do = False
                    if cell == Gt[2].position:
                        token_color = Gt[2].simbol
                        do = False
                    if cell == Gt[3].position:
                        token_color = Gt[3].simbol
                        do = False
                    if cell == Bt[0].position:
                        token_color = Bt[0].simbol
                        do = False
                    if cell == Bt[1].position:
                        token_color = Bt[1].simbol
                        do = False
                    if cell == Bt[2].position:
                        token_color = Bt[2].simbol
                        do = False
                    if cell == Bt[3].position:
                        token_color = Bt[3].simbol
                        do = False
                    if cell == Yt[0].position:
                        token_color = Yt[0].simbol
                        do = False
                    if cell == Yt[1].position:
                        token_color = Yt[1].simbol
                        do = False
                    if cell == Yt[2].position:
                        token_color = Yt[2].simbol
                        do = False
                    if cell == Yt[3].position:
                        token_color = Yt[3].simbol
                        do = False
                    if cell == 14 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟥"
                        do = False
                    elif cell == 1 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟩"
                        do = False     
                    elif cell == 27 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟦"
                        do = False
                    elif cell == 40 and self.no_token_there(Rt,Bt,Yt,Gt,cell):
                        token_color = "🟨"
                        do = False

                    if token_color is not None:
                        print(token_color, end=" ")
                    else:
                        print(cell, end=" ")

            print()


#list_players = []

#list_players.append(Player("blue"))
#list_players.append(Player("red"))
#list_players.append(Player("yellow"))

#list_players.append(Player("green"))
#board = Board()
#board.create_board()
#board.print_board(list_players[1].tokens,list_players[0].tokens,list_players[2].tokens,list_players[3].tokens)

#sleep(3)
#list_players[0].tokens[0].state = "available"
#list_players[0].tokens[0].position = blue_road[0]
#list_players[0].tokens[0].move(5,blue_road)
#board.print_board(list_players[1].tokens,list_players[0].tokens,list_players[2].tokens,list_players[3].tokens)
#sleep(3)
#list_players[0].tokens[1].position = blue_road[0]
#list_players[0].tokens[1].state = "available"
#list_players[0].tokens[1].move(3,blue_road)

#board.print_board(list_players[1].tokens,list_players[0].tokens,list_players[2].tokens,list_players[3].tokens)
#sleep(3)
#list_players[1].tokens[1].position = red_road[0]
#list_players[1].tokens[1].state = "available"
#list_players[1].tokens[1].move(3,red_road)

#board.print_board(list_players[1].tokens,list_players[0].tokens,list_players[2].tokens,list_players[3].tokens)