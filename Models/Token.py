class Token:
    def __init__(self,position,state,color): #cada token le corresponde a un jugador, y cada jugador tiene 4 tokens 
        self.position = position
        self.state = state #State puede ser Box (cuando está sin salir en posición inicial), Coronate, o available
        self.color = color



    def eaten(self,initial_position):
        self.position = initial_position
        self.state = "box"

    def coronate(self):
        self.state = "coronate"


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

    