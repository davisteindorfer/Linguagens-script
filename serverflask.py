from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    return 'Insira o numero apos a barra no link para obter sua soma com 2, como em http://localhost:8080/100'

@app.route('/<num>')
def soma_dois(num):
    return f'{num} + 2 = {int(num) + 2}'

if __name__ == "__main__":
    app.run(host='localhost', port=8080)
