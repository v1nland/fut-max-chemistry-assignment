# player needs all player attributes to evaluate it's chemistry later
# the first attribute we gonna use is natural_position to run maximum-weighted-bipartite-matching
class Player:
  def __init__(self, name, nationality, league, club, natural_position):
    self.name = name
    self.nationality = nationality
    self.league = league
    self.club = club
    self.natural_position = natural_position

  def position_in_squad(self, squad_position):
    if squad_position.name == self.natural_position.name:
      return "natural"
    elif squad_position.name in self.natural_position.related_positions:
      return "related"
    elif squad_position.name in self.natural_position.unrelated_positions:
      return "unrelated"
    else:
      return "wrong"

  def eval_chemistry_for_max_assignment(self, squad_position):
    if self.position_in_squad(squad_position) == "natural":
      return 0
    elif self.position_in_squad(squad_position) == "related":
      return 1
    elif self.position_in_squad(squad_position) == "unrelated":
      return 2
    else:
      return 3
  
  def eval_chemistry_for_squad(self, squad_position, neighbor_players):
    sum_links_value = 0.0

    for p in neighbor_players:
      current_neighbor = p["player"]

      if self.nationality == current_neighbor.nationality and self.league == current_neighbor.league and self.club == current_neighbor.club:
        sum_links_value = sum_links_value + 3
      elif self.nationality == current_neighbor.nationality and self.league == current_neighbor.league and self.club != current_neighbor.club:
        sum_links_value = sum_links_value + 2
      elif self.nationality != current_neighbor.nationality and self.league == current_neighbor.league and self.club == current_neighbor.club:
        sum_links_value = sum_links_value + 2
      elif self.nationality != current_neighbor.nationality and self.league == current_neighbor.league and self.club != current_neighbor.club:
        sum_links_value = sum_links_value + 1
      elif self.nationality == current_neighbor.nationality and self.league != current_neighbor.league and self.club != current_neighbor.club:
        sum_links_value = sum_links_value + 1
      elif self.nationality != current_neighbor.nationality and self.league != current_neighbor.league and self.club != current_neighbor.club:
        sum_links_value = sum_links_value + 0

    # calculate L factor
    l_factor = sum_links_value/len(neighbor_players)

    # eval chemistry based on l factor
    return self.chemistry_from_l(l_factor, squad_position)
  
  def chemistry_from_l(self, l_factor, squad_position):
    position_in_squad = self.position_in_squad(squad_position)

    if position_in_squad == "natural":
      if l_factor < 0.3:
        return 3
      elif l_factor >= 0.3 and l_factor < 1.0:
        return 6
      elif l_factor >= 1.0 and l_factor < 1.6:
        return 9
      elif l_factor >= 1.6:
        return 10
    elif position_in_squad == "related":
      if l_factor < 0.3:
        return 2
      elif l_factor >= 0.3 and l_factor < 1.0:
        return 5
      elif l_factor >= 1.0 and l_factor < 1.6:
        return 8
      elif l_factor >= 1.6:
        return 9
    elif position_in_squad == "unrelated":
      if l_factor < 0.3:
        return 1
      elif l_factor >= 0.3 and l_factor < 1.0:
        return 3
      elif l_factor >= 1.0 and l_factor < 1.6:
        return 5
      elif l_factor >= 1.6:
        return 5
    elif position_in_squad == "wrong":
      if l_factor < 0.3:
        return 0
      elif l_factor >= 0.3 and l_factor < 1.0:
        return 1
      elif l_factor >= 1.0 and l_factor < 1.6:
        return 2
      elif l_factor >= 1.6:
        return 2

  def __str__(self):
    return """name: {}, natural_position: {}, nationality: {}, league: {}, club: {}""".format(self.name, self.natural_position, self.nationality, self.league, self.club)