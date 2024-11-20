import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Urls
ApiUrl = "/api/v2"
Hosts = "http://app.zeelo.co"


Urls = {
    "checkUsers": f"{Hosts}{ApiUrl}/users/check",
    "login": f"{Hosts}{ApiUrl}/login",
    "zeelo": f"{Hosts}/my-zeelo",
}

Payload = {
    "email": "kayphaz007@gmail.com",
    "password": "S0mt0l0v3.",
    "request_sign": "a70c93c6425160a1a5a64c8d02bc87c0",
    "scope": "REGULAR_USER,JOURNEY_VEHICLE_TRACKING,ME_SHOW,ME_UPDATE,USER_SHOW",
    "client_id": 2,
    # "client_secret": "v2ypGh7xl1909tFV6feO5d5yP2wZbcO10fSeRD3p",
    "client_secret": "v2ypGh7xl1909tFV6feO5d5yP2wZbcO10fSeRD3p",
    "grant_type": "password",
    "authentication_provider": "ZEELO",
}

Headers = {
    "Origin": Hosts,
    "Referer": Urls["zeelo"],
    "Marketid": "7625e92d-b080-4d71-9b1f-2e24c0fb8cba",
}


def runMain() -> None:
    s = requests.session()
    s.get(Urls["zeelo"])
    disp_headers = s.headers
    # check user
    r = s.post(
        Urls["login"],
        data={
            "username": Payload["email"],
            "password": Payload["password"],
            "scope": Payload["scope"],
            "client_id": Payload["client_id"],
            "grant_type": Payload["grant_type"],
            "authentication_provider": Payload["authentication_provider"],
        },
        headers=Headers,
    )

    disp_headers = r.headers
    s.get(Urls["zeelo"])
    disp_headers = s.headers

    outputHtml = BeautifulSoup(r.text, "html.parser")

    print(s)


if __name__ == "__main__":
    runMain()
