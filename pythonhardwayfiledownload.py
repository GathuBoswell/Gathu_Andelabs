"""Code to download all the pages in the http://learnpythonthehardway.org/book/ table of contents"""
import requests
from lxml import html

base_url = "http://learnpythonthehardway.org/book/"
url = base_url + "ex1.html"
request = requests.get(url)
tree = html.fromstring(request.content)
print(tree)

#f = open('page1.html', 'w')
#f.write(request)
#f.close
