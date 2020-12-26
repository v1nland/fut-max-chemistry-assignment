import numpy

def build_bipartite_graph(players, squad):
  graph = []

  for player in players:
    player_chems = []

    # we want to evaluate its chemistry with each position in the squad
    # so we push to our graph the list of chemistries
    for squad_position in squad:
      chem = player.eval_chemistry_for_max_assignment(squad_position)
      player_chems.append(chem)

    # once it's evaluated, we push it into the graph
    graph.append(player_chems)

  return numpy.array(graph)
