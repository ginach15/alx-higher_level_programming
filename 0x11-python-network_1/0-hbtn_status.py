#!/usr/bin/python3

""" Python script that fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
<<<<<<< HEAD
        print('\t- utf8 content: {}'.format(html.decode("utf-8"))
=======
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
>>>>>>> dbf89040f0d8a9cd56e5262e217f80a6cd195218
