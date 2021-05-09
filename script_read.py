import json
from pprint import pprint

with open("text.json", "r", encoding='utf8') as read_file:
    data = json.load(read_file)
