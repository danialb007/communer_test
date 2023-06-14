import requests


def send_obesity_notification(user):
    title = "Fat"
    desc = "You are gettibg fat :|"
    requests.post(
        "NOTIFICATIONSERVICE/send_general",
        data={"user": user, "title": title, "desc": desc},
    )
