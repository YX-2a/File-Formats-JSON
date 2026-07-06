import json

with open("formats.json", "r") as kde:
    dicts = json.loads(kde.read())
print([list(i.keys())[0] for i in dicts["List"]][:41])