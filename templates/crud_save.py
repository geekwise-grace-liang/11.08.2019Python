import json

def crud_save(accounts):
  with open('target.json', 'w') as target_file:
    json.dump(accounts, target_file)
  