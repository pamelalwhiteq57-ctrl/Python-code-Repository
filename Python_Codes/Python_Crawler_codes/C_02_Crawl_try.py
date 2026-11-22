import requests
from pathlib import Path
bASE = Path(__file__).parent
url = "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/36/86/32699518636/32699518636-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&og=hw&deadline=1795367625&oi=0x2408846930803c5b11af21d7156261b0&trid=2139898cc0674b82b1b22d43b7a68bau&nbs=1&uipk=5&mid=516495843&os=hwbv&platform=pc&gen=playurlv3&upsig=f151cb146d7fba1f3272a0c77703c186&uparams=e,og,deadline,oi,trid,nbs,uipk,mid,os,platform,gen&bvc=vod&nettype=0&bw=104367&lrs=15&V=v3.1.2&f=u_0_0&qn_dyeid=34c6a6b8f0de5e1b00d089dc6b0306a9&agrr=0&buvid=1770F824-0A1A-F254-4869-C26731046E4C14912infoc&build=0&dl=0&orderid=0,3"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36 Edg/158.0.0.0",
           "referer":"https://www.bilibili.com/video/BV1bEndzgEfN/?spm_id_from=333.1387.favlist.content.click&vd_source=6e96dbcccbd2447caeb24da75f9d6f3c"}
res = requests.get(url, headers=headers)
print(res.status_code)
with open(bASE/"Berry浆果.mp3", "wb") as f:
    f.write(res.content)