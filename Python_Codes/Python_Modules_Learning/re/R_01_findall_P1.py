import re
text = "身高: 179, 体重: 145, 学号:2026501796, 密码:2600123456x123456"
print(re.findall(r"123456", text))
print(re.findall(r"[0-9]", text))
print(re.findall(r"\d+", text))
print(re.findall(r"\w", text))
print(re.findall(r"\d{4,7}", text))