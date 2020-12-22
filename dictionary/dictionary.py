"""
Uses prepopulated dictionary data to implement a basic dictionary with input validation.
Uses a similarity ratio to offer alternatives for certain invalid inputs
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinitions(word):
    """returns a list of the definition(s) of a word"""

    # VALIDATE INPUT

    # common nouns are stored in lowercase
    word = word.lower()
    if word.lower() in data:
        return data[word.lower()]

    # proper nouns
    elif word.title() in data:
        return data[word.title()]

    # acronyms
    elif word.upper() in data:
        return data[word.upper()]
    
    # match with similarity ratio >= 0.6 exists
    elif len(get_close_matches(word, data.keys())) > 1:
        
        # offer and give definition of alternative at user's request
        close_match = get_close_matches(word, data.keys())[0]
        response = input("Did you mean %s? [y/n] " % close_match)
        response = response.lower()
        if response == "y":
            return data[close_match]
        elif response == "n":
            return "Invalid entry. Please enter a new word."
        else:
            return "Invalid entry."

    else:
        return "Invalid entry. Please enter a new word."
    

def main():

    # get input and definitions
    word = input("Enter a word: ")
    output = getDefinitions(word)

    # format output according to return type
    if isinstance(output, list):
        for definition in output:
            print(definition)
    else:                       # there was an error
        print(output)


if __name__ == '__main__':
    main()