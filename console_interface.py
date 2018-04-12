import simple_scrape, scrape_connected, use_output


def interact():
    REQS = ["title", "links", "para", "text"]
    reqs = []
    website = input("Enter the url to scrape: ")
    print("\n1. Scrape this Website\n2. Scrape this Website and Anything Linked to It")
    type = input("Enter number: ")

    if type == "1":
        for req in REQS:
            print(req, "? (Y/N)", end=" ", sep="")
            if input().lower() == "y":
                reqs.append(req)

    filename = "scrape_output/" + input("Output Filename: ")

    if type == "1":
        content = simple_scrape.scrape(website, reqs=reqs)
    elif type == "2":
        content, errors = scrape_connected.scrape_all(website, json_format=True)

    with open(filename, "w") as outfile:
        outfile.write(content)

    use_output.get(filename, type)

    print("Process Completed")


if __name__ == "__main__":
    interact()