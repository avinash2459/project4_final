from flask import current_app as app, render_template, request, redirect, Response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# app = Flask(__name__)

mysql = MySQL(cursorclass=DictCursor)

mysql.init_app(app)


@app.route('/edit/<int:oscar_id>', methods=['GET'])
def form_edit_get(oscar_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblOscarImport WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', oscar=result[0])


@app.route('/edit/<int:oscar_id>', methods=['POST'])
def form_update_post(oscar_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('actorName'), request.form.get('movieName'), request.form.get('sex'),
                 request.form.get('age'), request.form.get('year'), oscar_id)
    print(inputData)
    sql_update_query = """UPDATE tblOscarImport t SET t.actorName = %s, t.movieName = %s, t.sex = %s, t.age =
    %s, t.year = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/oscars/<int:oscar_id>', methods=['PUT'])
def api_edit(oscar_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp
