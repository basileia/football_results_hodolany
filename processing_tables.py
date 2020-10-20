import json
import datetime


def load_json(file_name):
    """
    Loads given json file and return pair of two teams. The first one is
    home team and the second is away team.
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def get_info(number):
    """
    Get information about a football match by table number, returns list
    """
    wanted_team = "FC Sigma Hodolany (2)"
    results = load_json("table" + str(number) + ".json")

    for num, i in zip(results["hosté"], results["domácí"]):
        if wanted_team in results["hosté"][num]:
            info = [results["datum a čas"][num], results["domácí"][num],
                    wanted_team, results["skóre"][num]]

        if wanted_team in results["domácí"][i]:
            info = [results["datum a čas"][i], wanted_team,
                    results["hosté"][i], results["skóre"][i]]
    return info


def time_formatting(date_time):
    """
    Returns reformatting date and time
    """
    return datetime.datetime.strptime(date_time, '%d.%m.%Y %H:%M')


list_result = get_info(1)
print(time_formatting(list_result[0]))
