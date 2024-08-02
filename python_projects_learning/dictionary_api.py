
import requests
from pprint import pprint

user_input = input("Enter a word: ")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + user_input.lower()

#Returns a list about the information about the word entered
result = requests.get( url).text
print(result)