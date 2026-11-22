# '''
# 0:
# 导入requests, moviepy.editor模块(用*法导入所有)
# ①:
# 进入待处理的视频界面, F12打开edge开发者界面, 上面的栏目选网络,
# 网路栏目下选择fethc/XHR, 然后刷新网页以刷新数据
# ②:
# 在栏目中的大量数据中, 通过文件大小正倒序的方式来排查文件, 找到最大的, 那个就是视频文件,
# 注意格式是.m4s
# ③:
# 选中这个文件, 会弹出相应它的页面, 选择标头, 标头里有三个大项, 找到常规,
# 把其中的'请求URL'全部复制, 并粘贴保存在代码中(字符串形式)
# ④:
# 使用requests模块的.get方法, 并把url变量作为参数, 将结果存放到一个新变量如res里,
# 把参数headers设为第⑤步中的那个变量(如headers)
# ⑤:
# 命名一个字典变量为headers, 并在其中构建两个键值对(都以字符串形式),
# ⑥:
# 回到标头页面, 在请求标头这一栏里,
# 找到'user-agent'这个键(也就是设备信息),
# 把这个键和它对应的值完整粘贴进入headers的第一对键值对中;
# 再找到'referer'这个键,
# 把对应的键值对粘贴入headers的第二个键值对中
# ⑦:
# 使用print(res.status_code), 运行查看其是否能被抓取
# 结果表为:
# 403(禁止访问)
# 404(页面未找到)
# 500(服务器内部错误)
# 401(未授权访问)
# 400(错误请求)
# 503(服务不可用)
# 200(允许访问)
# 只有出现200时, 才可继续访问
# ⑧:
# 用open("name.mp4", "wb").write(res.content)的方式以二进制把视频数据写入文件中
# with open() as 的形式更好 
# ⑨:
# 获取音频,
# 先回到网络的Fetch/XHR页面, 在刚刚的正序文件大小排序方式下, 找到文件名为30232,m4s?e=...开头的文件,
# 进入其标头里, 复制其常规里的请求URL, 粘贴到变量里
# ⑩:
# 把第⑧步中的文件名结尾格式改为.mp3即可, 发送请求的部分只需改一下变量名即可
# ⑩①:
# 合并处理视频音频,
# 设俩文件名分别为video1和audio1
# 用VideoFileClip("video1")和AudioFileClip("audio1")处理文件, 并赋给新的变量,
# 设这俩的新的变量分别为v, a
# ⑩②:
# 使用v.set_audio(a)的方式, 将它们合并, 赋给新的变量如sp
# ⑩③；
# 以sp.write_videofile("name.mp4")的形式, 导出最终视频, 结果仍需赋给一个变量
# '''
'''
这是修改正确路径的部分
'''
from pathlib import Path
bASE = Path(__file__).parent
print(bASE)
'''
以下为获取音频的模板
'''
import requests
url = ""
headers = {"user-agent":"",
           "referer":""}
res = requests.get(url, headers=headers)
print(res.status_code)
with open(bASE/" name.mp3", "wb") as f:
    f.write(res.content)