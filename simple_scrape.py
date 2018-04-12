import regular_site, json


def scrape(url, json_format=True, reqs=["title", "links", "para", "text"]):
    site = regular_site.sift_from_url(url, reqs)
    if json_format:
        return json.dumps(site, indent="\t")
    return site


if __name__ == "__main__":
    website = "https://www.cancer.org/"
    print(scrape(website))

