from flask import Flask, render_template,request


def akinator(db):
    first_question = '茎の形態は無茎種である。'
    answer = request.args.get("answer")
    # MySQLのクエリを生成して絞り込み
    if answer == 'Yes':
        # 無茎種として絞り込み
        db.execute("create view akinator as SELECT * FROM flowers WHERE stem_type = '無茎種'")
    elif answer == 'No':
        # 有茎種として絞り込み
        result=db.execute("create view akinator as SELECT * FROM flowers WHERE stem_type = '有茎種'")

# FIXME: 使い方不明
# def akinator_seach(db):
#     # sqlから要素をランダムに1つ取得
#     question=db.execute("SELECT * FROM flowers ORDER BY RAND() LIMIT 0 OFFSET FLoor(RAND() * 6)rows")[0]
#     if answer == 'Yes':
#         cursor.execute("create view Akinator as select * from flowers where like %s", ('%'+question+'%',))
#     elif answer == 'No':
#         cursor.execute("create view Akinator as select * from flowers where not like %s", ('%'+question+'%',))
#     result = cursor.fetchall()
#     return result

#     if len(result) > 1:
#         result = akinator_seach()
#     # 結果が0件の場合は見つからなかった旨のメッセージを返す
#     elif len(result) == 0:
#         result =  '植物は見つかりませんでした。'
#     # 結果が1件の場合は結果を表示するテンプレートを返す
#     elif len(result) == 1:
#         result = cursor.fetchone()
#         return result
#     return render_template('Akinator.html',first_question=first_question,question 
#                             =question,result=result)
