from bs4 import BeautifulSoup
import requests

url = "https://www.ourpower.co.za/areas/jhb-city-power/blocks"

result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")
# only_text = answer.get_text()

#returns html code with <a></a> tags and the text in the tags
a_tags_html = soup.find_all('a')

block_numbers = [ "Block "+ str(i) for i in range(1,18) ]
cities = []

for i in a_tags_html:
    text_in_tag = i.get_text()
    if "Customer" in text_in_tag:
        quit()
    elif "View The Loadshedding Schedule For Jhb City Power" != text_in_tag:
        cities.append(str(i.get_text()))

print(len(cities))


