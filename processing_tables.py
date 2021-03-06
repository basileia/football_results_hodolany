from json import load
from jinja2 import FileSystemLoader, select_autoescape, Environment


def load_json(file_name):
    """
    Loads given json file
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = load(json_file)
    return data


def get_info():
    """
    Gets information about football matches, returns list with:
    date, home team, away team and score
    """
    wanted_team = "FC Sigma Hodolany (2)"
    matches_info = []

    results = load_json("tables.json")

    for j in range(1, len(results)):

        for num, i in zip(results[j]["hosté"], results[j]["domácí"]):
            if wanted_team in results[j]["hosté"][num]:
                matches_info.append([results[j]["datum a čas"][num],
                                    results[j]["domácí"][num],
                                    wanted_team, results[j]["skóre"][num]])

            if wanted_team in results[j]["domácí"][i]:
                matches_info.append([results[j]["datum a čas"][i],
                                    wanted_team, results[j]["hosté"][i],
                                    results[j]["skóre"][i]])
    return remove_pk_zero(matches_info)


def remove_pk_zero(matches_info):
    """
    Removes zero penalty kicks from results
    """
    for i in range(len(matches_info)):
        matches_info[i][3] = matches_info[i][3].replace(" (PK:0:0)", "")
    return matches_info


def fill_template():
    """
    Fills template with FC Hodolany match results
    """
    results = get_info()
    headers = ["datum a čas", "domácí", "hosté", "skóre"]
    env = Environment(loader=FileSystemLoader("./"),
                      autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template("table.tpl")
    return template.render(headers=headers, results=results)


def create_html_file():
    """
    Creates html_file
    """
    data = fill_template()
    with open("html_table.html", "w", encoding="utf-8") as file:
        file.writelines(data)


create_html_file()
