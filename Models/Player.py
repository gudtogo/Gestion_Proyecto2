from .Token import Token
import random 

class Player:
    def __init__(self,color,play = False): #Clase de jugador que posee un color que es lo que lo distingue, 4 tokens y un atributo que es True si está jugando o False si no
        self.color = color
        self.tokens = [Token(0,"box",color) for _ in range(4)]
        self.play = play
        
        
    def roll_dice(self):
        number = random.randint(1,6)
        return number
    
    def box_token(self):
        for i in self.tokens:
            if i.state == "box":
                return i
                break
        return False
            

    def available_tokens(self):
        for i in self.tokens:
            if i.state == "available":
                return i
                break
        return False


    
