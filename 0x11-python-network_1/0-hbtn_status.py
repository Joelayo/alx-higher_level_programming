#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request as request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        if response.readable():
            html = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(data.decode("utf-8")))
