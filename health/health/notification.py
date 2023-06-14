import requests


def send_ideal_bmi_notification(user):
    title = "bmi"
    desc = "you have an ideal bmi, goodjob."
    requests.post(
        "NOTIFICATIONSERVICE/send_general",
        data={"user": user, "title": title, "desc": desc},
    )
