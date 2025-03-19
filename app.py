from flask import Flask,request, jsonify
# importamos a classe FLask do modulo flask para criar nosso aplicativo web

# O parâmetro __name__ é passado para o Flask para que ele consiga identificar o arquivo principal da aplicação
app = Flask(__name__)

import sqlite3

# Aqui estamos criando uma rota para o endpoint "/pagar"
# Ou seja, quando acessarmos http://127.0.0.1:5000/pagar no navegador, a função abaixo será executada
@app.route("/pagar")
def exibir_mensagem():
# Retorna um texto formatado em HTML para ser exibido na página da rota "/pagar"
    return "<h1>Pagar as pessoas, faz bem as pessoas!!!</h1>"

# Criamos outra rota para o endpoint "/femandaopix"
# Quando acessarmos http://127.0.0.1:5000/femandaopix, a função será chamada automaticamente
@app.route("/femandaopix")
def manda_o_pix():
# Retorna um texto formatado em HTML que será exibido no navegador
    return "<h2>Se a tela apagou ta devendo</h2>"
# Criamos uma terceira rota para o endpoint "/comida"
# Sempre que o usuário acessar http://127.0.0.1:5000/comida, essa função será executada
@app.route("/comida")
def comida():
# Retorna um texto formatado em HTML com uma mensagem sobre comida
    return "<h2>Tomato à milanesa</h2>"

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo


#estrutura banco de dados

def init_db():
    # sqlite3 crie o arquivo database.db e se conecte com a variavel conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     image_url TEXT NOT NULL
                     )
    """)
init_db()

@app.route("/doar", methods =["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 401

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO LIVROS (titulo,categoria,autor,image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")

""")
        conn.commit()

        return jsonify({"mensagem":"Livro cadastrado com sucesso"}), 201

if __name__ == "__main__":
    app.run(debug=True)