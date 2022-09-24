import os
from flask import Flask, render_template, request, json
from flask_cors import CORS
from flaskext.mysql import MySQL


app = Flask(__name__, template_folder='view')
CORS(app)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def main():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/gravar', methods=['POST'])
def storeData():
    try:
        coon = mysql.connect()
        cursor = coon.cursor()

        _nome = request.form['nome']
        _preco = request.form['preco']
        _categoria = request.form['categoria']
    
        if _nome and _preco and _categoria:
            print("Dados para inserir: " + _nome + _preco + _categoria)
            cursor.execute('insert into tbl_user (user_name, user_preco, user_categoria) VALUES (%s, %s, %s)', (_nome,_preco,_categoria))
            coon.commit()
            print("Dados inseridos!")
        return render_template('index.html')
        
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()

@app.route('/listar',methods=['POST','GET'])

def listar():
    try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select user_name, user_preco, user_categoria from tbl_user')
            data = cursor.fetchall()
            print(data);

            conn.commit()
            return render_template('list.html', datas=data)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)