# packages
import time

# models
from player import Player
from position import Position

# functions
from squads import get_squad_options, get_squad, build_squad_relations, eval_squad_chemistry
from utils import pretty_print_squad_evaluation
from max_bipartite_matching import get_initial_player_distribution
from build_permutations import calculate_all_player_permutations

def run_algorithm(squad, players):
  # start timer
  start_time = time.time()

  # get starting squad from max assignment
  initial_player_distribution = get_initial_player_distribution(squad["positions"], players)

  # calculate permutations
  all_player_permutations = calculate_all_player_permutations(initial_player_distribution, squad)

  # print permutation build time and count
  print("--- %s permutations, build time: %s seconds ---" % (len(all_player_permutations), (time.time() - start_time)))

  # get max variables
  max_team_chemistry = 0
  team_of_max_team_chemistry = initial_player_distribution

  for permutation in all_player_permutations:
    # build squad relations
    squad_relations = build_squad_relations(squad, permutation)

    # eval current squad
    squad_evaluation = eval_squad_chemistry(squad_relations)

    if squad_evaluation["team_chemistry"] > max_team_chemistry:
      max_team_chemistry = squad_evaluation["team_chemistry"]
      team_of_max_team_chemistry = squad_evaluation

  # prety print
  pretty_print_squad_evaluation(team_of_max_team_chemistry)

  print("--- total time: %s seconds ---" % (time.time() - start_time))