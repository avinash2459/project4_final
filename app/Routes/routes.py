from flask import current_app as app, render_template
import simplejson as json
from flask import Flask, request, Response, redirect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# app = Flask(__name__)

mysql = MySQL(cursorclass=DictCursor)

mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Oscar Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblOscarImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, oscars=result)


@app.route('/view/<int:oscar_id>', methods=['GET'])
def record_view(oscar_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblOscarImport WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', oscar=result[0])


@app.route('/api/v1/oscars', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblOscarImport')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/oscars/<int:oscar_id>', methods=['GET'])
def api_retrieve(oscar_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblOscarImport WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


