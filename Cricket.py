print("\t!!!!!*****CRICKET PLAYER'S!!!!!*****\n")
class player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(player):
    def play(self):
        print("The batsman is batting.\n\n")

class Bowler(player):
    def play(self):
        print("The bowler is bowling.")


batsman = Batsman()
bowler = Bowler()

# Calling the function name with object 
batsman.play()
bowler.play()
