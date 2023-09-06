from .Token import Token
import random 

class Player:
    def __init__(self,color): #Clase de jugador que posee un color que es lo que lo distingue, 4 tokens y un atributo que es True si está jugando o False si no
        self.color = color
        self.tokens = [Token(0,"box",color) for _ in range(4)]
        

    def roll_dice(self):
        number = random.randint(1,6)
        return number
    





    
