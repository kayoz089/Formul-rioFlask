from flask import Flask, render_template, request
import sqlite3


def tabelas():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
''')
    
    conn.commit()
    conn.close()


# adicionando logins
def adicionar(nome, senha):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logins (nome, senha) VALUES (?, ?)", (nome, senha, ))

    conn.commit()
    conn.close()


# iniciando o flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']
        adicionar(nome, senha)
    
    return render_template("index.html")

if __name__ == "__main__":
    tabelas()  
    app.run(debug=True)