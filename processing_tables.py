import json


def load_json(file_name):
    """
    Loads given json file
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = json.load(json_file)
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


def create_html_table_headers(headers):
    """
    Creates headers and css style for html table
    """
    table = """
    <style>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
    th, td { padding: 5px; }
    </style>
    """
    table += '<table style="width:80%">\n'
    table += "  <tr>\n"
    for column in headers:
        table += "    <th>{0}</th>\n".format(column.strip())
    table += "  </tr>\n"
    return table


def create_html_table(results, headers):
    """
    Creates html table from list of match results
    """
    table = create_html_table_headers(headers)
    for i in range(len(results)):
        table += "  <tr>\n"
        for result in results[i]:
            if result == results[i][-1]:
                table += '  <td style="text-align:center">{0}</td>\n'.format(result.strip())
            else:
                table += "    <td>{0}</td>\n".format(result.strip())
        table += "  </tr>\n"
    return table


def create_html_file(table):
    with open("html_table.html", "w") as fileout:
        fileout.writelines(table)


headers = ["datum a čas", "domácí", "hosté", "skóre"]
table = create_html_table(get_info(), headers)
create_html_file(table)
