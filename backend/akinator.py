from flask import Flask, render_template, request, jsonify
import random

def akinator(db):
    data = request.get_json()
    answer = data['answer']
    if 'question' not in data:
        first_question = '茎の形態は無茎種である。'
        question = first_question
        db.execute("CREATE TEMPORARY TABLE temp_akinator SELECT * FROM flowers")
    else:
        question = data['question']

    if answer == 'Yes':
        db.execute("DELETE FROM temp_akinator WHERE steam_type = '有茎種'")
    
    elif answer == 'No':
        db.execute("DELETE FROM temp_akinator WHERE steam_type = '無茎種'")

    result = refine_search(db,question)
    return jsonify(result=result , question=question)


def refine_search(db,question):
    next_question = db.execute("SELECT * FROM temp_akinator ORDER BY RAND() LIMIT 0 OFFSET FLoor(RAND() * 6)rows")[0]
    if answer == 'Yes':
        cursor.execute("DELETE FROM temp_akinator WHERE NOT LIKE %s", ('%'+question+'%',))
    elif answer == 'No':
         cursor.execute("DELETE FROM temp_akinator WHERE LIKE %s", ('%'+question+'%',))
    result = cursor.fetchall()
  

    if len(result) > 1:
         result = refine_search(db,question)
     # 結果が0件の場合は見つからなかった旨のメッセージを返す
    elif len(result) == 0:
         result =  '植物は見つかりませんでした。'
     # 結果が1件の場合は結果を表示するテンプレートを返す
    elif len(result) == 1:
         return result
         

    return result
