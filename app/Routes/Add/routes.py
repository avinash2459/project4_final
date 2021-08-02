from flask import current_app as app, render_template, request, redirect, Response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# app = Flask(__name__)

mysql = MySQL(cursorclass=DictCursor)

mysql.init_app(app)


@app.route('/oscars/new', methods=['GET'])
def form_insert_get():
    return render_template('add.html', title='New Oscar Form')


@app.route('/oscars/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('actorName'), request.form.get('movieName'), request.form.get('sex'),
                 request.form.get('age'), request.form.get('year'))
    sql_insert_query = """INSERT INTO tblOscarImport (actorName,movieName,sex,age,year) VALUES (%s, %s,%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/oscars/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp
