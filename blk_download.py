fo = open('/Users/jwshin/Downloads/asteriskspace/practice/download.xml')

if __name__ == "__main__":
    pass

from bs4 import BeautifulSoup

soup = BeautifulSoup(fo)
titles = soup.findAll('article-title')
titles = [i.text for i in titles]
# pass
# print(titles)

import subprocess

for title in titles:
    subprocess.call(['python', 'sopaper.py', title])