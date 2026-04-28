from bs4 import BeautifulSoup
import requests

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# accessing html structure
# print(soup.prettify())

# accessing tags
# print(soup.title, '\n')
# print(soup.title.string)
print(soup.p.b, '\n')

# accessing class metadata
print(soup.p['class'], '\n')

#accessing href metadata
print(soup.a['href'], '\n')
print(soup.find(href="http://example.com/elsie"), '\n')

print(soup.find(class_='story')) # display all the content with class story
a_tags = soup.find_all('a')
print(a_tags, '\n') # display all the <a> tags, in a list format
print(a_tags[2], '\n') # display the 3rd <a> tag

a_title_tags = soup.find_all(['a', 'title']) # display all the <a> AND <title> tags, in a list format
print(a_title_tags, '\n')

p = soup.find(class_ = 'story')
# contents sort all children 
print(p.contents, '\n') # display the content of the <p> tag with class story, in a list format.

body = soup.find('body')
print(list(body.descendants), '\n') # display all the children of the <body> tag, in a list format.
print(len(list(body.descendants)), '\n') # display the number of children of the <body> tag.

# find parent
# print(soup.a.parent, '\n') # display the parent of the first <a> tag.
for p in soup.a.parents: # display all the parents of the first <a> tag, in a list format.
    print(p.name) # display the name of all parent tags.

print('\n')

# Wikipedia request
#-> "Please set a user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119."

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          "AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/140.0.0.0 Safari/537.36" }

response = requests.get('https://en.wikipedia.org/wiki/Attentat_de_Manchester_de_1996', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.h1.text)
print(len(soup.find_all('h2')))
print(soup.a['href'])
