import math
import os
import sys

import requests

def test():
    r = requests.get("http://google.com")
    test = 'Test'
print(r.status_code)
