import json
from deepgramAPI import call_api


#data_path = call_api()
data_path = "OutputData/jsonfiles/responseapi.json"
with open(data_path, "r") as read_file:
    data = json.load(read_file)


# returns a dictionary with names of non-present members as keys and empty lists as the value
# {missing members name: []} (if "attendance" key set to False)
def find_absent_members(team_mems: dict):
    absent_li = {}
    for i in team_mems:
        if not team_mems[i]["attendance"]:
            splt = team_mems[i]["fullname"].split(" ")
            absent_li.update({splt[0].lower(): []})
    return absent_li


# searches for names of missing members in API response data and returns the output dict from find_absent_members
# {missing members name: [time_stamps]}
def find_names(dict_names: dict):
    """Returns a list of lists from json output with [name: time_stamp] in seconds with a <float> at list[-1] representing the end of the input wav file in seconds"""
    wordz = data["results"]["channels"][0]["alternatives"][0]["words"]
    for i in range(len(wordz)):
        if wordz[i]["word"] in [*dict_names]:
            print(wordz[i]["word"], [*dict_names])
            dict_names[wordz[i]["word"]] += [wordz[i]["start"]]

    dict_names.update({"endclip": wordz[i]["end"]})
    return dict_names
