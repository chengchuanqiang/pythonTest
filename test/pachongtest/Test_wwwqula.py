import requests
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "Exception '%s'" % e


def getBooks(url):
    urlList = []
    html = getHtmlText(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    categoryList = soup.find_all('div', class_='index_toplist mright mbottom')

    for cate in categoryList:
        name = cate.find('div', class_='toptab').span.string
        with open('d:/python/novelList.doc', 'a+', encoding='utf-8') as f:
            f.write("\n小说种类: %s\n" % name)

        generalList = cate.find(style='display: block;')
        bookList = generalList.find_all('li')
        for book in bookList:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            urlList.append(link)
            with open('d:/python/novelList.doc', 'a', encoding='utf-8') as f:
                f.write("小说名称: %s\t小说地址: %s\n" % (title, link))
    return urlList


def getTxtUrl(url):
    urlList = []
    html = getHtmlText(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    listA = soup.find_all('dd')
    txtName = soup.find('h1').text
    with open("d:/python/小说/%s.txt" % txtName, 'a+', encoding='utf-8') as f:
        f.write('小说标题:%s\n\n\n' % txtName)
    for url in listA:
        urlList.append('http://www.qu.la' + url.a['href'])
    return urlList, txtName


def getOneTxt(url, txtName):
    try:
        html = getHtmlText(url).replace('<br/>', '\n')
        soup = bs4.BeautifulSoup(html, 'lxml')
        txt = soup.find('div', id='content').text.replace('chaptererror();', '')
        title = soup.find('title').text
        with open("d:/python/小说/%s.txt" % txtName, 'a+', encoding='utf-8') as f:
            f.write(title + '\n\n')
            f.write(txt)
            print('当前小说：%s 当前章节: %s 已经下载完毕' % (txtName, title))
    except Exception as e:
        print('Exception : %s' % e)


def main():
    url = 'http://www.qu.la/paihangbang/'
    bookList = getBooks(url)
    for i in range(1):
        urlList, txtName = getTxtUrl(bookList[i])
        print(urlList)
        for j in urlList:
            getOneTxt(j, txtName)


if __name__ == '__main__':
    main()
