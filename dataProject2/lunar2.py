from bs4 import BeautifulSoup
import urllib.request as req


def get_lunar(year, month):
    url="https://astro.kasi.re.kr/life/pageView/5?search_year={:04d}&search_month={:02d}&search_check=G".format(year, month)
    res = req.urlopen(url)
    # BeautifulSoup으로 분석하기
    soup = BeautifulSoup(res, "html.parser")
    lunar_list = []
    for tr in soup.select("div table tbody tr"):
        td = tr.select("td")
        lunar_dict = {"s" : td[0].string, "l" : td[1].string, "g" :td[2].string}
        # print(lunar_dict)
        lunar_list.append(lunar_dict)
    return lunar_list

print(get_lunar(2022,11))
