from flask import Flask, request, render_template
import mariadb
import sys

app = Flask(__name__)

try:
    conn = mariadb.connect(
        user="frontend",
        password="test",
        host="172.18.0.1",
        port=3366,
        database="backend_database"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def mainpage(): 
    career_id = None
    if request.method == 'POST':
        career_id = request.form.get('career_id', default=None, type=str)
    query_options = "SELECT id, path FROM career_paths"
    cur.execute(query_options)
    menu_options = cur.fetchall()
    toDoList=None
    if career_id and career_id != "":
        query2 = '''SELECT certs.cert_name, certs.cert_desc
        FROM certs
        INNER JOIN path_cert ON certs.id = path_cert.cert_id
        INNER JOIN career_paths ON path_cert.path_id = career_paths.id
        WHERE career_paths.id = %s;'''
        cur.execute(query2, (career_id,))
        toDoList = cur.fetchall()
        return render_template('index.html', options=menu_options, listing=toDoList, career_id=career_id)
    else:
        return render_template('index.html', options=menu_options, career_id="")
    # menu_options = [x[1] for x in menu_options]
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
