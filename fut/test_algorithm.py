# packages
from __future__ import print_function, unicode_literals

# models
from player import Player
from position import Position

# functions
from squads import get_squad
from run_algorithm import run_algorithm

# testing squad
squad = get_squad("433")

# testing players array
players = [
  Player("Claudio Bravo", "Chile", "Liga BBVA", "Real Betis", Position("gk")),
  Player("Francisco Sierralta", "Chile", "Premier League", "Watford", Position("rb")),
  Player("Guillermo Maripan", "Chile", "Ligue 1", "Monaco", Position("cb")),
	Player("Paulo Diaz", "Chile", "Libertadores", "River Plate", Position("cb")),
	Player("Lionel Messi", "Argentina", "Liga BBVA", "Barcelona", Position("rw")),
	Player("Erick Pulgar", "Chile", "Serie A", "Fiorentina", Position("cdm")),
	Player("Arturo Vidal", "Chile", "Serie A", "Inter de Milan", Position("cm")),
	Player("Cesar Pinares", "Chile", "Libertadores", "U. Catolica", Position("cam")),
	Player("Fabian Orellana", "Chile", "Liga BBVA", "Real Valladolid", Position("rm")),
	Player("Felipe Mora", "Chile", "MLS", "Portland Timbers", Position("st")),
	Player("Alexis Sanchez", "Chile", "Serie A", "Inter de Milan", Position("lw")),
]

run_algorithm(squad, players)