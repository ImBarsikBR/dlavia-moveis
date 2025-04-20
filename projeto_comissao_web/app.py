from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    comissao = None
    if request.method == "POST":
        try:
            valor = float(request.form["valor"])
            comissao = f"Comissão: R$ {valor * 0.15:.2f}"
        except ValueError:
            comissao = "Digite um número válido!"
    return render_template("index.html", comissao=comissao)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) 