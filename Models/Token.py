class Token:
    def __init__(self,position,state): #cada token le corresponde a un jugador, y cada jugador tiene 4 tokens 
        self.position = position
        self.state = state #State puede ser Box (cuando está sin salir en posición inicial), Coronate, o normal



    def eaten(self,initial_position):
        self.position = initial_position
        self.state = "box"

    def coronate(self):
        self.state = "coronate"

    def move(self,dice,final_position):
   
        if self.state == "final":
            if self.position + dice >= 6:
                self.state = "won"

        elif self.position + dice < final_position: #Ver si llegó a la recta final
            self.state = "final"
            additional_steps = self.position + dice - final_position
            self.position = additional_steps*-1
            print("CASO 2")

        else:
            if self.position +dice>51:
                additional_steps = self.position + dice - 52 #restante
                self.position = additional_steps - 1
          
            else:
                self.position +=dice
        
        print(self.position)

    def exit_box(self,initial_position):
        self.state = "available"
        self.position = initial_position
        print("El jugador saca un token, empieza en posición",self.position)

    