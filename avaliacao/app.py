from flask import Flask, render_template, request, redirect
import urllib.parse
import sqlite3

app = Flask(__name__)

# CRIAR BANCO
def init_db():

    conn = sqlite3.connect("database.db")
    
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
                    nome TEXT,
                   
                    nota INTEGER,
                   
                    comentario TEXT
                     )
                """)
    
    conn.commit()

    conn.close()


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/avaliar", methods=["POST"])
def avaliar():

    nome = request.form["nome"]

    nota = request.form["nota"]

    comentario = request.form["comentario"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO
avaliacoes (nome, nota, comentario)
                   VALUES (?, ?, ?)
    """, (nome, nota, comentario))

    conn.commit()
    conn.close()

    rating = request.form.get("rating")

    mensagem = f"""
    NOVA AVALIAÇÃO !

    Nome: {nome}

    Nota: {rating}/5

    Comentário: {comentario}
    """

    mensagem = urllib.parse.quote(mensagem)
    numero = "5598981820442"
    link_whatsapp = (f"https://wa.me/{numero}?text={mensagem}")

    return redirect(link_whatsapp)

@app.route("/admin")
def admin():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM avaliacoes ORDER BY id DESC")

    avaliacoes = cursor.fetchall()

    conn.close()

    return render_template(
        "admin.html", avaliacoes=avaliacoes
    )

init_db()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

