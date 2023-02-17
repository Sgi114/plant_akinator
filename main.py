from plant_akinator import app
from flask import render_template
import test_scraping
import mysql-connector-python

cnx = MySQLdb.connect(
    host='localhost',
    user='root',
    password='password',
    db='dbname'
)
cursor = cnx.cursor()

table = 'plant'
cursor.execute("DROP TABLE IF EXISTS `%s`;", table)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS violas (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    botanical_name VARCHAR(255),
    common_name VARCHAR(255),
    flower_color VARCHAR(255),
    blooming_period VARCHAR(255),
    leaf_shape VARCHAR(255),
    leaf_edge VARCHAR(255),
    leaf_arrangement VARCHAR(255),
    leaf_surface VARCHAR(255),
    leaf_texture VARCHAR(255),
    height VARCHAR(255),
    habitat VARCHAR(255),
    distribution VARCHAR(255),
    description TEXT)
    """, table)

# test_scraping.scraping()

for viola in viola_list:
    cursor.execute("INSERT INTO plant (name,botanical_name,common_name,flower_color,blooming_period ,leaf_shape,leaf_edge,leaf_arrangement ,leaf_surface,leaf_texture height ,habitat ,distribution ) VALUES (%s, %s)", (viola['名前'], viola['説明']))
conn.commit()

@app.route('/') # はじめの処理
def index():
    return render_template('index.html') 


if __name__ == '__main__': # debugを行う
    app.debug = True
    app.run(host='localhost')


@app.route('/Akinator')
def Akinator():
    question = questions[0]
    return render_template('Akinator.html',question=question)

# 回答を受け取って、次の質問を表示
@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']

    # ここで、回答に応じて次の質問を選択し、または絞り込んだ結果を表示するロジックを実装する
    # また、データベースから絞り込んだ結果を取得する
    cursor.execute("SELECT * FROM flowers WHERE {} = %s".format(column), (answer,))
    result = cursor.fetchall()

    if len(result) == 0:
        return "この花は見つかりませんでした"
    elif len(result) == 1:
        return render_template('result.html', result=result)
    else:
        question_index = questions.index(
            {'question': question, 
            'answers': [answer],
            next_question = questions[question_index + 1]}
            )
    @app.route('/Search_name')
def Search_name():
    return render_template(
        'Search_name.html'
    )

@app.route('/Add_plant')
def Add_plant():
    return render_template(
        'Add_plant.html'
    )


