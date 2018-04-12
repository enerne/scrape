from urllib.request import urlopen, Request
import urllib.error


def get_page(url, decode=True):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()


    if decode:
        return page.decode("utf-8")
    return page


if __name__ == "__main__":
    url1 = input("Enter url: ")
    print(get_page(url1))