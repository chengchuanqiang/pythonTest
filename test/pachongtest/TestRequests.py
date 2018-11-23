import requests

r = requests.get("http://www.baidu.com")

print(r.text)
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)
print(r.content)


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "Exception '%s'" % e


print(getHtmlText("http://www.baidu.com"))
