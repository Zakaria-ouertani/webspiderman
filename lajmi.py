from bs4 import BeautifulSoup
from urllib import request

def get_links(html_page_link):
	html_content = request.urlopen(html_page_link).read()
	chorba = BeautifulSoup(html_content, 'html.parser')
	a_tags = chorba.find_all('a')
	links = []
	for link in a_tags:
		links.append(link.get('href'))
	return links


links = get_links('https://en.wikipedia.org/wiki/Main_Page')
for link in links:
	print(link)