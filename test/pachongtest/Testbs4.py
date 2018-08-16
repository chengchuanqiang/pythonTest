import requests
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "Exception '%s'" % e


html = getHtmlText("http://www.baidu.com")
# 使用 html.parser 进行解析
soup = BeautifulSoup(html, "html.parser")
htmlDom = soup.prettify()
print(htmlDom)
print(soup.title)
print(soup.title.parent.name)
print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

