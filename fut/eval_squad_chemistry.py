from bipartite_graph import get_initial_squad
from neighbors_by_squad import get_squad, build_squad_relations

# get squad from repo
squad = get_squad("433")
# get starting squad from max assignment
starting_squad = get_initial_squad()
# build squad relations
squad_relations = build_squad_relations(squad, starting_squad)

def pretty (relations):
  pretty = []

  for r in relations:
    pretty.append({ "player": r["player"].name, "position": r["position"].name })

  return pretty

for elem in squad_relations:
  player = elem["player"]
  position = elem["position"]
  relations = elem["relations"]

  pr = pretty(relations)
  player_chemistry = player.eval_chemistry_for_squad(position, relations)
  print(player.name, position.name, player_chemistry, pr)
