import regular_site, json


def scrape(url, json_format=True):
    site = regular_site.sift_from_url(url, ["title", "links", "para", "text"])
    if json_format:
        return json.dumps(site, indent="\t")
    return site


if __name__ == "__main__":
    website = "https://www.cancer.org/"
    print(scrape(website))