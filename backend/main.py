from flask import Flask, render_template,request
import backend.test_scraping as test_scraping
import MySQLdb
from backend import app
import akinator
import mysql

cnx,cursor=mysql.setup()

# app = Flask(__name__)

# table = 'plant'
# cursor.execute("DROP TABLE IF EXISTS `%s`;", table)
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS violas (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     classification VARCHAR(255),
#     basic_specie VARCHAR(255),
#     mutation VARCHAR(255),
#     alias VARCHAR(255),
#     origin VARCHAR(255),
#     foreign_generic_name VARCHAR(255),
#     stem_morphology VARCHAR(255),
#     distribution_japan  VARCHAR(255),
#     distribution_foreign VARCHAR(255),
#     distribution_supplement VARCHAR(255),
#     flower_shape VARCHAR(255),
#     flower_color VARCHAR(255),
#     flower_distance VARCHAR(255),
#     flower_season VARCHAR(255),
#     flower_style VARCHAR(255),
#     flower_supplement VARCHAR(255),
#     leaf_shape VARCHAR(255),
#     leaf_color VARCHAR(255),
#     leaf_supplement VARCHAR(255),
#     seed_shape VARCHAR(255),
#     seed_color VARCHAR(255),
#     seed_supplement VARCHAR(255),
#     root_features VARCHAR(255),
#     endangered_species VARCHAR(255),
#     reference_sample VARCHAR(255),
#     description TEXT)
#     """, table)

# violas = test_scraping.scraping()

# for viola in violas:
#     cursor.execute("INSERT INTO plant (classification, basic_specie, mutation, alias, origin, foreign_generic_name, stem_morphology, distribution_japan, distribution_foreign, distribution_supplement, flower_shape, flower_color, flower_distance,  flower_season, flower_style, flower_supplement, leaf_shape, leaf_color, leaf_supplement, seed_shape, seed_color, seed_supplement, root_features, endangered_species, reference_sample, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)", 
#     (viola['分類'], viola['基本種'], viola['変種'],viola['品種'],viola['異名'],viola['由来'],viola['外語一般名'],viola['茎の形態'] , viola['国内'], viola['海外'], viola['補足'], viola['形状'], viola['色'], viola['距'], viola['花期'], viola['花柱'], viola['補足'], viola['形状'], viola['色'], viola['補足'], viola['形状'], viola['色'], viola['補足'], viola['根の特徴'], viola['絶滅危惧種'], viola['基準標本'], viola['その他']))
# cnx.commit()

@app.route('/') # はじめの処理
def index():
    return render_template('index.html') 

if __name__ == '__main__': # debugを行う
    app.debug = True
    app.run(host='localhost')

@app.route('/akinator')
def flask_akinator():
    akinator.akinator()
    return 

@app.route('/Search_name')
def Search_name():
    return render_template(
        'Search_name.html',
    )

@app.route('/Add_plant')
def Add_plant():
    return render_template(
        'Add_plant.html'
    )

@app.route('/Search_name', methods=['POST'])
def Search_name():
    name = request.form['name']
    cursor.execute("SELECT * FROM flowers WHERE name = %s", (name,))
    result = cursor.fetchall()
    return render_template('result.html', result=result)
