from flask import Flask
from flask import render_template
import pyodbc


app = Flask(__name__, static_url_path='/static')

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-QF6AULF;DATABASE=test1;Trusted_Connection=yes;')

@app.route('/')
def index():
    sql="INSERT INTO persona (nombre,apellido,ntelefono,nID) VALUES ('Martha', 'Ojeda', '300458745','3');"
    conn = connection
    cursor =conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('index.html')

@app.route('/mainPage')
def mainPage():
    return render_template('mainPage.html')

@app.route('/DatosPaciente')
def datosPaciente():
    return render_template('DatosPaciente.html')
   
@app.route('/ConsultaDatos')    
def ConsultaDatos():
    return render_template('ConsultaDatos.html')

if __name__== '__main__':
    app.run(debug=True)