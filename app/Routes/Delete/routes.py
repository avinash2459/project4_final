from flask import current_app as app, render_template, redirect, Response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# app = Flask(__name__)

mysql = MySQL(cursorclass=DictCursor)

mysql.init_app(app)


@app.route('/delete/<int:oscar_id>', methods=['POST'])
def form_delete_post(oscar_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblOscarImport WHERE id = %s """
    cursor.execute(sql_delete_query, oscar_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/oscars/<int:oscar_id>', methods=['DELETE'])
def api_delete(oscar_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp

