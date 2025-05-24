from flask import Flask, render_template, request, redirect, url_for, send_file
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


def adicionar(nome, senha):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logins (nome, senha) VALUES (?, ?)", (nome, senha, ))

    conn.commit()
    conn.close()


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']
        adicionar(nome, senha)
        return redirect(url_for('index'))
    
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, senha FROM logins")
    logins = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", logins=logins)


if __name__ == "__main__":
    tabelas()  
    app.run(debug=True)
