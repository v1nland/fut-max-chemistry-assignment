# libs
import numpy
import LAPJV

# own models
from player import Player
from position import Position

# functions
from build_bipartite_graph import build_bipartite_graph
from neighbors_by_squad import get_squad

def get_initial_squad():
  # squads are static, they won't change
  # probably is better having a JSON file
  # but for testing just use and modify this array
  squad = get_squad("433")["positions"]

  # players are based on input
  # should connect to a rest api
  # or scrap based on ID
  players = [
    Player("Claudio Bravo", "Chile", "Liga BBVA", "Real Betis", Position("GK")),
    Player("Francisco Sierralta", "Chile", "Premier League", "Watford", Position("RB")),
    Player("Guillermo Maripan", "Chile", "Ligue 1", "Monaco", Position("CB")),
  	Player("Paulo Diaz", "Chile", "Primera division de Argentina", "River Plate", Position("CB")),
  	Player("Lionel Messi", "Argentina", "Liga BBVA", "Barcelona", Position("RW")),
  	Player("Erick Pulgar", "Chile", "Serie A", "Fiorentina", Position("CM")),
  	Player("Arturo Vidal", "Chile", "Serie A", "Inter de Milan", Position("CM")),
  	Player("Cesar Pinares", "Chile", "Primera division de Chile", "U. Catolica", Position("CAM")),
  	Player("Fabian Orellana", "Chile", "Liga BBVA", "Real Valladolid", Position("RW")),
  	Player("Felipe Mora", "Chile", "MLS", "Portland Timbers", Position("ST")),
  	Player("Alexis Sanchez", "Chile", "Serie A", "Inter de Milan", Position("LW")),
  ]

  # our graph, built from both arrays
  graph = build_bipartite_graph(players, squad)

  # once the build is ready, pretty print graph
  # print(graph)
  # print("\n\n")

  # then compute maximum-weighted-bipartite-matching
  result = LAPJV.lap(graph)[2]

  # and print it
  # print(result)
  # print("\n\n")

  players_array = []
  # print results names
  # print("squad", "player", "player natural position", "chemistry")
  for i in range(len(result)):
    squad_position = squad[i]
    player = players[result[i]]
    players_array.append(player)
    # print(
    #   squad_position.name,
    #   player.name,
    #   player.natural_position.name,
    #   player.eval_chemistry_for_max_assignment(squad_position),
    # )

  return players_array