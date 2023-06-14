from typing import Union

import requests

from user.user.models import User


def send_notification(from_: User, to: User, data: Union[bytes, str]):
    is_file = False
    if isinstance(data, bytes):
        is_file = True
    requests.post(
        "NOTIFICATIONSERVICE/send_message",
        data={
            "title": f"New message from {from_.firstname}",
            "desc": "File!!!" if is_file else data,
        },
    )
