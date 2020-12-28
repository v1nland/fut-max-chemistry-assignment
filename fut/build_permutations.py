def calculate_all_player_permutations(players, squad):
  all_permutations = []

  permute (all_permutations, players, squad, 0, len(players) - 1)

  return all_permutations

def permute(all_permutations, players, squad, l, r):
  if l == r:
    new_permutation = tuple( [p for p in players] )

    if new_permutation not in all_permutations:
      all_permutations.append( new_permutation )
  else:
    for i in xrange(l, r + 1):
      if len(players[l].natural_position.related_positions) == 0 and squad["positions"][i].name != players[l].natural_position.name:
        permute(all_permutations, players, squad, r, r) # r to r to avoid unnecesary swapping
      elif squad["positions"][i].name == players[l].natural_position.name:
        players[l], players[i] = players[i], players[l]
        permute(all_permutations, players, squad, l+1, r)
        players[l], players[i] = players[i], players[l]
      elif squad["positions"][i].name in players[l].natural_position.related_positions:
        players[l], players[i] = players[i], players[l]
        permute(all_permutations, players, squad, l+1, r)
        players[l], players[i] = players[i], players[l]
      elif squad["positions"][i].name in players[l].natural_position.unrelated_positions:
        players[l], players[i] = players[i], players[l]
        permute(all_permutations, players, squad, l+1, r)
        players[l], players[i] = players[i], players[l]
      else:
        permute(all_permutations, players, squad, r, r) # r to r to avoid unnecesary swapping
