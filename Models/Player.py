from .Token import Token
import random 

class Player:
    def __init__(self,color,play = False): #Clase de jugador que posee un color que es lo que lo distingue, 4 tokens y un atributo que es True si está jugando o False si no
        self.color = color
        self.tokens = [Token(0,"box",color) for _ in range(4)]
        self.play = play
        self.final_advance = 0
        
    def roll_dice(self):
        number = random.randint(1,6)
        return number
    
    def box_token(self):
        for i in self.tokens:
            if i.state == "box":
                return i
        return False
            

    def available_tokens(self):
        tokens = []
        for i in self.tokens:
            if i.state == "available" or "coronate" in i.state:
                if isinstance(i.position, str):
                        if "6" in i.position:
                            continue
                tokens.append(i)
        if len(tokens) > 0:
            return random.choice(tokens)
        return False


    
    def win(self):
        won = 0
        for t in self.tokens:
            if isinstance(t.position, str):
                if "6" in t.position:
                    won += 1
        if won == 4:
            return True
        else:
            return False
        
