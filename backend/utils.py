# 辞書型の値が空のキーをすべて取り除く関数
def remove_empty_keys(dict):
    return {k: v for k, v in dict.items() if v}
