
import random

class Player():
    moves=("P", "R", "S")

    def __init__(self, name):
        self.name=name
        self.quit=False
        self.wincount=0

    def playit(self):
        legal=False
        while not legal:
            self.play = input("Enter play (P, R, S): ").upper()
            if self.play=="Q":
                self.quit=True

            legal=self.play in Player.moves or self.quit

    def countWin(self):
        self.wincount+=1


class AutoPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def playit(self):
        
        playval=random.randint(0,2)
        self.play=Player.moves[playval]
        print(self.name + " selects " + self.play)

class Winner():
    
    game= {"RS": "rock breaks scissors",
       "SP": "scissors cuts paper",
       "PR": "paper covers rock"
       }

      
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2



    def checkWin(self, p1, p2):
        match1=p1.play + p2.play
        match2=p2.play + p1.play

        msg=Winner.game.get(match1)
        if msg!=None:
            p1.countWin()
            outcome=p1.name +" Win -- " + msg
        else:
            msg=Winner.game.get(match2)
            p2.countWin()
            outcome=p2.name + " Win -- " + msg
        return outcome

    def findWin(self):
        if self.p1.play == self.p2.play:
            return "Tie, no winner"
        else:
            return self.checkWin(self.p1, self.p2)        
   

player1=Player("YOU")
player2=AutoPlayer("AUTO")
while not player1.quit:
    player1.playit()
    if not player1.quit:
        player2.playit()
        winner = Winner(player1, player2)
        print(winner.findWin())



print(player1.name, player1.wincount)
print(player2.name, player2.wincount)



    







    