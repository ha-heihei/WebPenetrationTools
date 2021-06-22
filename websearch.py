from pyquery import PyQuery as pq
import requests
import re
from urllib.parse import urlparse

comp = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

    'Cache-Control': 'max-age=0',

    'Connection': 'keep-alive',

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 '
                  'Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400 '
}


def getAllUrl(baseUrl):
    urls = []
    res = requests.get(baseUrl,headers=headers)
    if res.status_code != 200:
        return []
    urlparsed = urlparse(baseUrl)
    baseUrl = f"{urlparsed.scheme}://{urlparsed.netloc}/"
    html = pq(res.text)
    for a in html.find("a"):
        url = str(pq(a).attr("href"))
        if not url.__contains__("http"):
            url = baseUrl + url
        urls.append({
            "url": url,
            "type": "超链接"
        })
    for img in html.find("img"):
        url = str(pq(img).attr("src"))
        if not url.__contains__("http"):
            url = baseUrl + url
        urls.append({
            "url": url,
            "type": "图片"
        })
    for sci in html.find("script"):
        url = str(pq(sci).attr("src"))
        if pq(sci).attr("src"):
            if not url.__contains__("http"):
                url = baseUrl + url
            urls.append({
                "url": url,
                "type": "脚本文件"
            })
    for link in html.find("link"):
        url = str(pq(link).attr("href"))
        if not url.__contains__("http"):
            url = baseUrl + url
        urls.append({
            "url": url,
            "type": "CSS文件"
        })
    urls.extend([{"url": url, "type": "其他"} for url in comp.findall(str(html))])
    new_urls = []  # 存储去重后的数据
    for x in urls:  # 根据字典列表的resource_id做去重操作
        if any(str(d.get('url', None)).lower() == str(x['url']).lower() for d in new_urls):
            pass
        else:
            new_urls.append(x)
    return new_urls


if __name__ == '__main__':
    print(getAllUrl("https://blog.csdn.net/sinat_38682860/article/details/103540366"))
    # from urllib.parse import urlparse

    # rs = urlparse("https://blog.csdn.net/sinat_38682860/article/details/103540366")
    # print(rs)
    # print(rs.scheme)
    # print(rs.netloc)
