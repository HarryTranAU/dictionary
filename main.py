import requests
import json

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
            print("definition: " + temp[0]["meanings"][num]["definitions"][0]["definition"])
            print("example: " + temp[0]["meanings"][num]["definitions"][0]["example"])
            if "synonyms" in temp[0]["meanings"][num]["definitions"][0].keys():
                print("synonyms: ", temp[0]["meanings"][num]["definitions"][0]["synonyms"])
            print("*********")
    except ValueError:
        print(f"{user_word} is not a word. Try again")
