import bs4

# 使用lxml进行解析
soup = bs4.BeautifulSoup(open('html/baidu.html', encoding='UTF-8'), 'lxml')
print(soup.prettify())
a = soup.find_all('a')
for link in a:
    print(link.get("href"))
