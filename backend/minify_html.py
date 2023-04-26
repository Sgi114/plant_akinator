import re


def minify(s0):
    s1 = "".join([s.strip() for s in s0])  # 各行の前後の空白を削除
    s9 = re.sub('<!--.*?-->', '', s1)  # コメントの削除
    return s9
