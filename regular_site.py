from bs4 import BeautifulSoup
from read_page import get_page
import re


# sift_from_url() returns a dictionary of requested info using the source code
# gotten from the url
# parameters:
#   url: the url of the website to scrape
#   reqs: list of requests for the parser
# returns: Dictionary of data gotten from sift()
def sift_from_url(url, reqs):
    return sift(get_page(url), reqs)


# sift() returns a dictionary of requested info from the passed source code
# parameters:
#   source: source code of site
#   reqs: list of requests for the parser
# returns: Dictionary of data
def sift(source, reqs):
    soup = BeautifulSoup(source, "html.parser")
    return_data = {}

    # ======= FOR LOOP ===========
    # This for loop runs through requests and gets links, title, paragraphs,
    # and all text, if included in reqs argument
    for req in reqs:
        if req == "links":
            return_data["links"] = get_links(soup)

        elif req == "title":
            return_data["title"] = get_title(soup)

        elif req == "text":
            return_data["text"] = get_text(soup)

        elif req == "para":
            return_data["paragraphs"] = get_para(soup)

    return return_data


# get links returns a list of links, starting at "href=" if possible, from the passed BeautifulSoup object
# parameters:
#   soup: BeautifulSoup object with the source code from the site
# returns: a list of links from the source
def get_links(soup):
    links = soup.find_all("a")
    for i in range(len(links)):
        links[i] = str(links[i]).replace("  ", "").replace("\n", "")
        if "href" in links[i]:
            links[i] = links[i][links[i].index("href") + 6:links[i].index(">")-1]

    return links


# get title of the web page
# parameters:
#   soup: BeautifulSoup object with source code from the site
# returns: string of title
def get_title(soup):
    return str(soup.title.getText())


# get all the text on the web page
# parameters:
#   soup: BeautifulSoup object with source code from the site
# returns: string of all text in site
def get_text(soup):
    return str(soup.getText())


# get text from paragraphs in web page
# parameters:
#   soup: BeautifulSoup object with source code from the site
# returns: list of all text in paragraph elements
def get_para(soup):
    paragraphs = soup.find_all("p")
    for i in range(len(paragraphs)):
        paragraphs[i] = str(paragraphs[i].getText()).replace("  ", "").replace("\n", "").replace(u"\xa0", " ").encode("utf-8").decode("utf-8")

    return paragraphs


if __name__ == "__main__":
    print(sift_from_url("https://www.cancer.org/", ["", "", "para", ""]))
