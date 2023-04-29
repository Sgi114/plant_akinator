import os
import json


PYTHON_DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # pyファイルが置かれているパス

# JSONファイルのパス
FILE_PATH_JSON = "violas.json"

# 出力先ファイルのパス
FILE_PATH_SQL = "violas.sql"


result_sql_list = ["USE `plant_akinator`;",
                   "SET CHARSET UTF8;",
                   "SET CHARACTER_SET_CLIENT = utf8;",
                   "SET CHARACTER_SET_CONNECTION = utf8;",
                   "\n\n"]

# jsonファイルを読み込む
with open(os.path.join(PYTHON_DIR_PATH, FILE_PATH_JSON), encoding="utf-8") as f:
    json_data = json.load(f)

# CREATE TABLE文を作成
result_current_sql_list = [
    "CREATE TABLE IF NOT EXISTS `plant_akinator`.`violas` ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"]
column_name_list = []  # 列名リスト
for data in json_data:
    for data_key in data.keys():
        if(data_key in column_name_list):
            continue
        column_name_list.append(data_key)

column_sql_list = []
for column_name in column_name_list:
    sql = ("`"+column_name+"` TEXT").replace("\n", "")
    column_sql_list.append(sql)

result_current_sql_list.append(", ".join(column_sql_list))
result_current_sql_list.append(");")
result_sql_list.append("".join(result_current_sql_list))
result_sql_list.append("\n\n")

# INSERT文を作成
for data in json_data:
    result_current_sql_list = ["INSERT INTO `violas` ("]
    column_sql_list = []
    for data_key in data.keys():
        column_sql_list.append("`"+data_key+"`")
    result_current_sql_list.append(", ".join(column_sql_list))
    result_current_sql_list.append(") VALUES (")
    column_sql_list = []
    for data_key in data.keys():
        if(data_key == "image_list"):
            # data[data_key]をjson文字列化
            json_str = json.dumps(data[data_key], ensure_ascii=False)
            column_sql_list.append('`'+json_str+'`')
            continue
        column_sql_list.append('`'+data[data_key].replace("\n", "\\n")+'`')
    result_current_sql_list.append(", ".join(column_sql_list))
    result_sql_list.append(" ".join(result_current_sql_list))
    result_sql_list.append(");")
    result_sql_list.append("\n\n")

# 結果を保存
result_sql = " ".join(result_sql_list)
with open(os.path.join(PYTHON_DIR_PATH, FILE_PATH_SQL), mode="w", encoding="utf-8") as f:
    f.write(result_sql)

print("✅ SQLファイルの作成が完了しました")
print("作成先: "+os.path.join(PYTHON_DIR_PATH, FILE_PATH_SQL))
