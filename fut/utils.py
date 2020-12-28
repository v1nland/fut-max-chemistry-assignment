def pretty_print_squad_evaluation (squad_evaluation):
  squad_distribution = squad_evaluation["distribution"]
  team_chemistry = squad_evaluation["team_chemistry"]
  print ( 'distribution has {} team chemistry'.format(team_chemistry) )
  
  for position in squad_distribution:
    player = position["player"]
    position_in_squad = position["position_in_squad"]
    chemistry = position["chemistry"]

    print (player.name, position_in_squad.name, chemistry)