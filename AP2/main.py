from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':

        numeroEscrito = int(request.form['numero']) 
        Resultado = numeroEscrito + 2
        sentence = f'{numeroEscrito} + 2 = {Resultado}'

        return render_template('index.html', sentence=sentence)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=8080)
