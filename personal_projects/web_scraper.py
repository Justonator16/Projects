from bs4 import BeautifulSoup
import requests


url = "https://www.ourpower.co.za/areas/jhb-city-power/blocks"

result = requests.get(url)

answer = BeautifulSoup(result.text, "html.parser")
only_text = answer.get_text()

#Phase one is extracting specific text related to blocks and the surburbs 
phase_one = []
for i in range(len(only_text)):
    #Check for "Block 1" text in paragraph
    if only_text[i] == "B" and only_text[i+1] == "l" \
        and only_text[i+2] == "o" and only_text[i+1] == "c" \
            and only_text[i+2] == "k" and only_text[i+3] == "" and only_text[i+4] == "1":
        phase_one.append(only_text[i:])
print(phase_one)