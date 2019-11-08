import json

def crud_read(inputFile):
  """
  Imports json-structured data from a json file given a filename
  """
  with open('accounts.json') as file_data:
    return json.load(file_data)

