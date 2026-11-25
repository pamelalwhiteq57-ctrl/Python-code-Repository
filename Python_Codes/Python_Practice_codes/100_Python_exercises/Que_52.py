# Question:52
'''
删除字符，给定两个字符串str和sub，从str中完全删除在sub中存在的字符
'''
# 法一:
def substitute(source: str, sub: str) -> str:
    table = str.maketrans("", "", sub)
    return source.translate(table)

# 法二:
def remove_chars(source:str, sub:str) -> str:
    remove_set = set(sub)
    return "".join(ch for ch in source if ch not in remove_set)
s = input("输入原字符串:")
sub = input("输入要删除字符所在字符串:")
print(substitute(s, sub))
result = remove_chars(s, sub)
print(result)