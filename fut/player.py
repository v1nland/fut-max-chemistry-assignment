# player needs all player attributes to evaluate it's chemistry later
# the first attribute we gonna use is natural_position to run maximum-weighted-bipartite-matching
class Player:
    def __init__(self, name, nationality, league, club, natural_position):
        self.name = name
        self.nationality = nationality
        self.league = league
        self.club = club
        self.natural_position = natural_position

    def eval_chemistry(self, squad_position):
        if self.natural_position.name == squad_position.name:
            return 0
        else:
            return 9999