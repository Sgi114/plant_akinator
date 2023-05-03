from flask import Flask, render_template, request, jsonify
import random


def akinator(db):
    data = request.get_json()
    answer = data['answer']
    # db =  ここでデータベースに接続する

    if 'question' not in data:
        first_question = '茎の形態は無茎種である。'
        question = first_question
    else:
        question = data['question']


    
    if answer == 'Yes':
        db.execute("UPDATE flowers SET active = 1 WHERE question = %s", (question,))
    
    elif answer == 'No':
        db.execute("UPDATE flowers SET active = 0 WHERE question = %s", (question,))

    result = akinator_search(db,question)
    return jsonify(result=result , question=question)


def akinator_seach(db,question):
    question = db.execute("SELECT * FROM flowers ORDER BY RAND() LIMIT 0 OFFSET FLoor(RAND() * 6)rows")[0]
    if answer == 'Yes':
        cursor.execute("create view Akinator as select * from flowers where like %s", ('%'+question+'%',))
    elif answer == 'No':
         cursor.execute("create view Akinator as select * from flowers where not like %s", ('%'+question+'%',))
    result = cursor.fetchall()
  

    if len(result) > 1:
         result = akinator_seach(db,question)
     # 結果が0件の場合は見つからなかった旨のメッセージを返す
    elif len(result) == 0:
         result =  '植物は見つかりませんでした。'
     # 結果が1件の場合は結果を表示するテンプレートを返す
    elif len(result) == 1:
         return result
         

    return result
