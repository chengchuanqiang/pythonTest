import requests
import bs4


# http://dianying.2345.com/top/

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except Exception as e:
        return "Exception '%s'" % e


def getContent(url):
    html = getHtmlText(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    movies = soup.find('ul', class_='picList clearfix')
    movieList = movies.find_all('li')
    for movie in movieList:
        imgUrl = 'http:' + movie.find('img')['src']
        name = movie.find('a', class_='aPlayBtn')['title']

        try:
            time = movie.find('span', class_='sIntro').text
        except Exception as e:
            time = "暂未上映"
        actors = movie.find('p', class_='pActor')
        actor = ''
        for act in actors:
            actor += act.string + "  "

        intro = movie.find('p', class_='pTxt pIntroShow').text

        print("片名：{}\t{}\n{}\n{} \n \n ".format(name, time, actor, intro))

        # 下载图片
        with open('d:/python/电影图片/' + name + '.png', 'wb+') as f:
            f.write(requests.get(imgUrl).content)

    print("获取的电影总数：%s" % len(movies))


def main():
    url = 'http://dianying.2345.com/top/'
    getContent(url)


if __name__ == '__main__':
    main()
