# packages
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator

# models
from player import Player
from position import Position

# functions
from db import get_players_from_input
from max_bipartite_matching import get_initial_squad
from squads_list import get_squad_options, get_squad, build_squad_relations

questions = [
    {
        'type': 'list',
        'name': 'squad',
        'message': 'Choose the squad you want to get max chemistry for',
        'choices': get_squad_options
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_01',
        'message': 'Select one of the results for the player 01',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_02',
        'message': 'Select one of the results for the player 02',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_03',
        'message': 'Select one of the results for the player 03',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_04',
        'message': 'Select one of the results for the player 04',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_05',
        'message': 'Select one of the results for the player 05',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_06',
        'message': 'Select one of the results for the player 06',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_07',
        'message': 'Select one of the results for the player 07',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_08',
        'message': 'Select one of the results for the player 08',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_09',
        'message': 'Select one of the results for the player 09',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_10',
        'message': 'Select one of the results for the player 10',
        'choices': get_players_from_input,
    },
    {
        'type': 'input',
        'name': 'player_name',
        'message': 'Type the name of a player you want to look for',
    },
    {
        'type': 'list',
        'name': 'picked_player_11',
        'message': 'Select one of the results for the player 11',
        'choices': get_players_from_input,
    },
]

# read user answers
answers = prompt(questions)

# get squad from repo
squad = get_squad(answers["squad"])

# build players array
players = [
  answers["picked_player_01"],
  answers["picked_player_02"],
  answers["picked_player_03"],
  answers["picked_player_04"],
  answers["picked_player_05"],
  answers["picked_player_06"],
  answers["picked_player_07"],
  answers["picked_player_08"],
  answers["picked_player_09"],
  answers["picked_player_10"],
  answers["picked_player_11"],
]

# squad = get_squad("433")

# players = [
#   Player("Claudio Bravo", "Chile", "Liga BBVA", "Real Betis", Position("gk")),
#   Player("Francisco Sierralta", "Chile", "Premier League", "Watford", Position("rb")),
#   Player("Guillermo Maripan", "Chile", "Ligue 1", "Monaco", Position("cb")),
# 	Player("Paulo Diaz", "Chile", "Primera division de Argentina", "River Plate", Position("cb")),
# 	Player("Lionel Messi", "Argentina", "Liga BBVA", "Barcelona", Position("rw")),
# 	Player("Erick Pulgar", "Chile", "Serie A", "Fiorentina", Position("cm")),
# 	Player("Arturo Vidal", "Chile", "Serie A", "Inter de Milan", Position("cm")),
# 	Player("Cesar Pinares", "Chile", "Primera division de Chile", "U. Catolica", Position("cam")),
# 	Player("Fabian Orellana", "Chile", "Liga BBVA", "Real Valladolid", Position("rw")),
# 	Player("Felipe Mora", "Chile", "MLS", "Portland Timbers", Position("st")),
# 	Player("Alexis Sanchez", "Chile", "Serie A", "Inter de Milan", Position("lw")),
# ]

# get starting squad from max assignment
starting_squad = get_initial_squad(squad["positions"], players)

# build squad relations
squad_relations = build_squad_relations(squad, starting_squad)

for elem in squad_relations:
  player = elem["player"]
  position = elem["position"]
  relations = elem["relations"]

  player_chemistry = player.eval_chemistry_for_squad(position, relations)
  print(player.name, position.name, player_chemistry)
