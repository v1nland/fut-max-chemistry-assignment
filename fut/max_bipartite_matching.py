# libs
import numpy
import LAPJV

# models
from player import Player
from position import Position

# functions
from build_bipartite_graph import build_bipartite_graph
from squads_list import get_squad

def get_initial_squad(squad, players):
  # our graph, built from both arrays
  graph = build_bipartite_graph(players, squad)

  # compute maximum-weighted-bipartite-matching
  result = LAPJV.lap(graph)[2]

  # return final squad
  return [players[i] for i in result]