
#Ponto de entrada da aplicacao web.
from flask import Flask, render_template

from database import DrakeNestBD


app = Flask(__name__)


#Mostrar a primeira pagina do painel.
@app.route("/")
def pagina_inicial():
 
    return render_template("index.html")


if __name__ == "__main__":
    DrakeNestBD()
    app.run(debug=True)
