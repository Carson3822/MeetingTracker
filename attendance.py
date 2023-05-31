team_members = {
    "E01": {"fullname": "Mark Hammond", "Email": em, "attendance": False},
    "E02": {"fullname": "Anthony Clark", "Email": em, "attendance": False},
    "E03": {"fullname": "Katie Smith", "Email": em, "attendance": False},
    "E04": {"fullname": "Tim Smith", "Email": em, "attendance": False}
}


def sign_in_main_device(eID):
    """ takes team_member employee id (E#) as argument and updates team_member attendance to True"""
    team_members[f"{eID}"].update({"attendance": True})
    return team_members[f"{eID}"]["attendance"]


def sign_in_personal_device():
    """ allow team members to sign in for meeting on their own devices"""
    pass


# at very end of meeting and program running we want to reset all team_members[eID]['attendance'] to False again
def auto_sign_out(team_ms):
    for i in team_ms.keys():
        team_ms[i].update({"attendance": False})
    return None


if __name__ == '__main__':
    sign_in_main_device("E01")
    sign_in_main_device("E02")
    print(team_members)
    auto_sign_out(team_members)
    print(team_members)
