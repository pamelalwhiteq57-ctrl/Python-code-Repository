import requests
import pathlib
base = pathlib.Path(__file__).parent
url = ""
headers = {"user-agent":"",
           "referer":""}
res = requests.get(url, headers=headers)
print(res.status_code)
with open(base/"name.mp3", "wb") as f:
    f.write(res.content)