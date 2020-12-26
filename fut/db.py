# packages
from __future__ import print_function, unicode_literals
from pg import DB

# models
from player import Player
from position import Position

def get_players_from_input(answers):
  # build output options
  output_options = []

  # connect to db
  db = DB(dbname='fut', host='localhost', port=5432, user='postgres', passwd='123')

  # query db
  query = db.query("SELECT * FROM players WHERE name LIKE '%{}%'".format(answers["player_name"]))

  # build option result
  for res in query.dictresult():
    output_options.append({
      "name": "[{}] {}, {}, {}, {}".format(
        res["position"].decode('utf8'),
        res["name"].decode('utf8'),
        res["nation"].decode('utf8'),
        res["club"].decode('utf8'),
        res["league"].decode('utf8')
      ),
      "value": Player(res["name"].decode('utf8'), res["nation"].decode('utf8'), res["league"].decode('utf8'), res["club"].decode('utf8'), Position( res["position"].decode('utf8') ) )
    })

  # return options list
  return output_options