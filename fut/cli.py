# packages
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator

# models
from player import Player
from position import Position

# functions
from db import get_players_from_input
from squads import get_squad_options, get_squad, build_squad_relations, eval_squad_chemistry
from run_algorithm import run_algorithm

# cli questions
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

# get squad from squad list
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

run_algorithm(squad, players)