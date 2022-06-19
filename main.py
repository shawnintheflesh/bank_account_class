class Player(object):

    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
        self.score = 0

tim = Player("Tim")

print(tim.name)
print(tim.lives)
print(tim.level)
tim.lives -= 1

