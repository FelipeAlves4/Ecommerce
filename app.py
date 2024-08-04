#importando blibioteca
from flask import Flask


#instancia do flask(padrão)
app = Flask(__name__)

#Definir uma rota raiz (Pagina inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_word():
    return "Hello World"


#Executar o servidor
if __name__ == "__main__":
    app.run(debug=True)