from bs4 import BeautifulSoup
import grequests 
import time

def get_urls():
    urls = []
    for x in range(1, 5):
        urls.append(f"https://priceoye.pk/mobiles?page={x}")
    return urls

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp


def parse_data(resp):
    for r in resp:
        sp = BeautifulSoup(r.text, "lxml")
        data = sp.select('div.productBox')

        for item in data:
            name = item.select_one('div.p-title').text.strip()
            price = item.select_one("div.price-box").text.replace('Rs.','').strip()
            print(name, price)

    return

if __name__ == '__main__':
    start = time.perf_counter()
    urls = get_urls()
    resp = get_data(urls)
    parse_data(resp)
    finish = time.perf_counter() - start
    print(finish)
        
