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


def print_result(url):
    soup = bs4.BeautifulSoup(getHtmlText(url), 'lxml')
    print(soup.prettify())


def main():
    url = 'http://www.qu.la/book/168/'
    print_result(url)


if __name__ == '__main__':
    main()
