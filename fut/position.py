class Position:
  def __init__(self, name):
    self.name = name
    self.related_positions = self.get_related_positions()
    self.unrelated_positions = self.get_unrelated_positions()

  def get_related_positions(self):
    related_positions = {
      "GK": [],
      "RB": ["RWB"],
      "CB": [],
      "LB": ["LWB"],
      "RWB": ["RB"],
      "LWB": ["LB"],
      "CDM": ["CM"],
      "CM": ["CDM", "CAM"],
      "CAM": ["CM"],
      "RM": ["RW"],
      "LM": ["LW"],
      "RW": ["RM", "RF"],
      "LW": ["LM", "LF"],
      "CF": ["CAM", "ST"],
      "RF": ["RW"],
      "LF": ["LW"],
      "ST": ["CF"],
    }

    return related_positions[self.name]

  def get_unrelated_positions(self):
    unrelated_positions = {
      "GK": [],
      "RB": ["CB", "LB", "RM"],
      "CB": ["RB", "LB", "CDM"],
      "LB": ["CB", "RB", "LM"],
      "RWB": ["LWB", "RM", "RW"],
      "LWB": ["RWB", "LM", "LW"],
      "CDM": ["CB", "CAM"],
      "CM": ["RM", "LM"],
      "CAM": ["CDM"],
      "RM": ["RB", "RWB", "CM", "LM", "RF"],
      "LM": ["LB", "LWB", "CM", "RM", "LF"],
      "RW": ["RWB", "LW"],
      "LW": ["LWB", "RW"],
      "CF": ["RF", "LF"],
      "RF": ["CF", "LF", "ST"],
      "LF": ["CF", "RF", "ST"],
      "ST": ["RF", "LF"],
    }

    return unrelated_positions[self.name]
