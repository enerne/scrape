import json, time

schema = ["title", "description", "category"]


def get(filename, type="1"):
    data = {}

    with open(filename, "r") as file:
        file_dict = json.loads(file.read())

    if type == "1":
        name = file_dict["title"]
        data["title"] = file_dict["title"]

        para = file_dict["paragraphs"]
        s = ""
        for p in para:
            if p != " " and p != "":
                s += p
        data["description"] = s

    elif type == "2":
        dict_array = []
        for k in file_dict.keys():
            obj = file_dict[k]
            temp_dict = {"title": obj["title"]}
            para = obj["paragraphs"]
            para = "".join(para)
            temp_dict["description"] = para.rstrip()
            dict_array.append(temp_dict)
        name = dict_array[0]["title"]

    timestamp = str(time.time())
    timestamp = timestamp.split(".")[1]
    timestamp = timestamp[:len(timestamp)//2]

    name = name.lower().split(" ")
    name = "".join(name[:len(name)//2])

    name = "our_output/" + timestamp + name + ".json"
    with open(name, "w") as file:
        if type == "1":
            file.write(json.dumps(data, indent="\t"))
        elif type == "2":
            file.write(json.dumps(dict_array, indent="\t"))