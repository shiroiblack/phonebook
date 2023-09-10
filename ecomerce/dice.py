
class Dice:
    
    
    
    def roll(self):
        import random
        
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        return dice1,dice2
        
        
        
play = Dice()
print(play.roll())
    
    