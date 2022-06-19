class Player(object):

    def __init__(self, name):
        self.lives = 3
        self.level = 1
        self.score = 0
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
         self._lives = lives
        else:
            print("Lives cannot be negative.")
            self.lives = 0

    def __str__(self):
        return "Name: {0, name}"

    lives = property(_get_lives, _set_lives)