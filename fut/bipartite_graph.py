# libs
import numpy
import LAPJV

# own models
from player import Player
from position import Position

# functions
from build_bipartite_graph import build_bipartite_graph

# squads are static, they won't change
# probably is better having a JSON file
# but for testing just use and modify this array
squad_433 = [
    Position("GK"),
    Position("RB"),
    Position("CB"),
    Position("CB"),
    Position("LB"),
    Position("CM"),
    Position("CM"),
    Position("CM"),
    Position("RW"),
    Position("ST"),
    Position("LW"),
]

# players are based on input
# should connect to a rest api
# or scrap based on ID
players = [
  Player("Mauricio Isla", "Chile", "Liga do Brasil", "Flamengo", Position("CB")),
	Player("Paulo Diaz", "Chile", "Primera division de Argentina", "River Plate", Position("CB")),
	Player("Francisco Sierralta", "Chile", "Premier League", "Watford", Position("CB")),
	Player("Jean Beausejour", "Chile", "Primera division de Chile", "U. de Chile", Position("LB")),
	Player("Erick Pulgar", "Chile", "Serie A", "Fiorentina", Position("CDM")),
	Player("Arturo Vidal", "Chile", "Serie A", "Inter de Milan", Position("CAM")),
	Player("Cesar Pinares", "Chile", "Liga do Brasil", "Gremio", Position("CAM")),
	Player("Fabian Orellana", "Chile", "Liga BBVA", "Real Valladolid", Position("RF")),
	Player("Felipe Mora", "Chile", "MLS", "Portland Timbers", Position("ST")),
	Player("Alexis Sanchez", "Chile", "Serie A", "Inter de Milan", Position("CF")),
  Player("Claudio Bravo", "Chile", "Liga BBVA", "Real Betis", Position("GK")),
]

# our graph, built from both arrays
graph = build_bipartite_graph(players, squad_433)

# once the build is ready, pretty print graph
print(graph)
print("\n\n")

# then compute maximum-weighted-bipartite-matching
result = LAPJV.lap(graph)[2]

# and print it
print(result)
print("\n\n")

# print results names
print("squad", "player", "player natural position", "chemistry")
for i in range(len(result)):
    squad_position = squad_433[i]
    player = players[result[i]]
    print(
        squad_position.name,
        player.name,
        player.natural_position.name,
        player.eval_chemistry(squad_position),
    )