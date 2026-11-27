import re
text = "barbar carcar harhal"
text1 = "<a><b>"
print(re.findall(r"<.+?>", text1), re.findall(r"<.+>", text1))
print(re.findall(r"(\w{3})(\1)", text))  # \1在()内，会创建新分组
print(re.findall(r"(?P<name>\w{3})(?P=name)", text))  # (?P=...)不算新分组，除非再加()