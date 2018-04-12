import simple_scrape, json, urllib.error


def scrape_all(website, json_format=True, reqs=["title", "links", "para", "text"]):
    errors = 0
    main_page = simple_scrape.scrape(website, False, reqs)

    pages = {"main": main_page}

    links = main_page["links"]

    # Formats the link correctly, with website url in the beginning if necessary
    for i in range(len(links)):
        if "https" not in links[i]:
            links[i] = website + links[i]

    for i in range(len(links)):
        try:
            temp_page = simple_scrape.scrape(links[i], False)
            title = "page" + str(i)
            pages[title] = temp_page
        except urllib.error.HTTPError:
            errors += 1
        except urllib.error.URLError:
            errors += 1
        except UnicodeEncodeError:
            errors += 1
        except UnicodeDecodeError:
            errors += 1

    print("Errors:", errors)
    if json_format:
        return json.dumps(pages, indent="\t"), errors
    return pages, errors


if __name__ == '__main__':
    pages, errors = scrape_all("https://www.cancer.org/")
    with open("test.json", "w") as test:
        test.write(pages)