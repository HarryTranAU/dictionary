import requests
import json
from prettytable import PrettyTable

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
            # print("definition: " + def1)
            exp1 = temp[0]["meanings"][num]["definitions"][0]["example"]
            # print("example: " + exp1)
            sym1 = False
            if "synonyms" in temp[0]["meanings"][num]["definitions"][0].keys():
                sym1 = temp[0]["meanings"][num]["definitions"][0]["synonyms"]
                # print("synonyms: ", sym1)
            d = PrettyTable()
            d.field_names = ["-", "details"]
            d.add_row(["Definition", def1])
            d.add_row(["",""])
            d.add_row(["Example", exp1])
            if sym1:
                d.add_row(["Synonym", sym1])
            print(d)
    except ValueError:
        print(f"{user_word} is not a word. Try again")

