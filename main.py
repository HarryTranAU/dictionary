import requests
import json
from prettytable import PrettyTable
from textwrap3 import wrap

def get_definition(word):
    link = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(link)

    return response.text

while True:
    user_word = input("please enter a word (--exit to quit): ")

    if user_word == "--exit":
        break

    definition = get_definition(user_word)
    temp = json.loads(definition)

    try:
        for num in range(len(temp[0]["meanings"])):
            def1 = temp[0]["meanings"][num]["definitions"][0]["definition"]
            exp1 = temp[0]["meanings"][num]["definitions"][0]["example"]
            sym1 = False
            if "synonyms" in temp[0]["meanings"][num]["definitions"][0].keys():
                sym1 = temp[0]["meanings"][num]["definitions"][0]["synonyms"]
            d = PrettyTable()
            d.field_names = ["", user_word]
            d.add_row(["Definition", ""])
            for section in wrap(def1, 60):
                d.add_row(["", section])
            d.add_row(["",""])
            d.add_row(["Example", ""])
            d.add_row(["", exp1])
            if sym1:
                d.add_row(["Synonym", sym1])
            print(d)
    except KeyError:
        print(f"{user_word} is not a word. Try again")
