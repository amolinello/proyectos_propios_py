from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def listado():
    personas = [['Alejandro', 'Molinello', 27], ['Andres', 'Salamanca', 25]]
    return render_template("pagina.html", personas=personas)

if __name__ == '__main__':
    app.run()