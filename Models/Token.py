
class Token:
    def __init__(self,position,state,color): #cada token le corresponde a un jugador, y cada jugador tiene 4 tokens 
        self.position = position
        self.state = state #State puede ser Box (cuando está sin salir en posición inicial), Coronate, o available
        self.color = color
        self.simbol = self.define_simbol(color) 



    def define_simbol(self,color):
        if color == "red":
            return "🔴"
        elif color == "blue":
            return "🔵"
        elif color == "green":
            return "🟢"
        elif color == "yellow":
            return "🟡"

    def eaten(self,initial_position):
        self.position = initial_position
        self.state = "box"

    def coronate(self):
        self.state = "coronate"

    def move_final_road(self,board):
        final_road = board.final_road(self.color)
        if self.position in final_road:
            advanced = final_road.index(self.position)
            if advanced+1 <6:
                self.position = final_road[advanced+1]
            else:
                self.state = "won"

    def move(self,road,board):
        if self.position not in road:
            self.move_final_road(board)
        else:
            actual_advance = road.index(self.position)
            actual_advance+= 1
            if actual_advance > len(road)-1:
                self.position = board.final_road(self.color)[0]
            else:
                self.position = road[actual_advance]
            return True
                


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

    