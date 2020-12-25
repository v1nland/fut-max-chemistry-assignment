import * from './data-source/position_relations' as relations

# player needs all player attributes to evaluate it's chemistry later
# the first attribute we gonna use is natural_position to run maximum-weighted-bipartite-matching
class Player:
  def __init__(self, name, nationality, league, club, natural_position, related_positions, unrelated_positions):
    self.name = name
    self.nationality = nationality
    self.league = league
    self.club = club
    self.natural_position = natural_position

  def eval_chemistry_for_max_assignment(self, squad_position):
    if squad_position.name == self.natural_position.name:
      return 0
    elif squad_position.name in self.natural_position.related_positions:
      return 1
    elif squad_position.name in self.unrelated_positions:
      return 2
    else:
      return 3
