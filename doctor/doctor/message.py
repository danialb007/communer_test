from typing import Union

import requests

from user.user.models import User


def send(from_: User, to: User, data: Union[bytes, str]):
    requests.post(
        "MESSAGINGSERVICE/send_message",
        data={
            "to": to,
            "data": data,
        },
    )
