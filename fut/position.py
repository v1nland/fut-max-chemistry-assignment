class Position:
  def __init__(self, name):
    self.name = name
    self.related_positions = self.get_related_positions()
    self.unrelated_positions = self.get_unrelated_positions()

  def get_related_positions(self):
    related_positions = {
      "gk": [],
      "rb": ["rwb"],
      "cb": [],
      "lb": ["lwb"],
      "rwb": ["rb"],
      "lwb": ["lb"],
      "cdm": ["cm"],
      "cm": ["cdm", "cam"],
      "cam": ["cm"],
      "rm": ["rw"],
      "lm": ["lw"],
      "rw": ["rm", "rf"],
      "lw": ["lm", "lf"],
      "cf": ["cam", "st"],
      "rf": ["rw"],
      "lf": ["lw"],
      "st": ["cf"],
    }

    return related_positions[self.name]

  def get_unrelated_positions(self):
    unrelated_positions = {
      "gk": [],
      "rb": ["cb", "lb", "rm"],
      "cb": ["rb", "lb", "cdm"],
      "lb": ["cb", "rb", "lm"],
      "rwb": ["lwb", "rm", "rw"],
      "lwb": ["rwb", "lm", "lw"],
      "cdm": ["cb", "cam"],
      "cm": ["rm", "lm"],
      "cam": ["cdm"],
      "rm": ["rb", "rwb", "cm", "lm", "rf"],
      "lm": ["lb", "lwb", "cm", "rm", "lf"],
      "rw": ["rwb", "lw"],
      "lw": ["lwb", "rw"],
      "cf": ["rf", "lf"],
      "rf": ["cf", "lf", "st"],
      "lf": ["cf", "rf", "st"],
      "st": ["rf", "lf"],
    }

    return unrelated_positions[self.name]

  def __str__(self):
    return """{}""".format(self.name)