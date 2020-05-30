import json
import difflib

with open('data.json') as json_file:
    data = json.load(json_file)
    formatedData = {k.lower(): v for k, v in data.items()}


def findWord(word):
    fWord = word.lower()
    if fWord in formatedData:
        result = formatedData.get(fWord)
        str = " "
        return str.join(result)
    else:
        result = difflib.get_close_matches(fWord, formatedData.keys())
        str = " "
        response =  input(f"Did you mean these words - {str.join(result)} - instead? "
                          f"\n Enter Y for Yes and N for No. "
                          f"\n")
        if response == "Y":
            userNewInput = input("Enter the word again ")
            return findWord(userNewInput)
        else:
            return "GoodBye"


userInput = input("Enter your word: ")
result = findWord(userInput)
print(result)
