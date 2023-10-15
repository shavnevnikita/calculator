from decimal import *
from flask import Flask, render_template, request

app = Flask(__name__)
getcontext().prec = 4

@app.route("/", methods=["post", "get"])
def main():
    return render_template('main.html')

@app.route("/calculate", methods=["post"])
def calculate():
    a = request.json["a"].replace(',','.')
    b = request.json["b"].replace(',','.')
    a = Decimal(a)
    b = Decimal(b)
    answ = 0
    if request.json["op"] == "+":
        answ = a+b
    else:
        answ = a-b
    return {"result": answ}

if __name__ == "__main__":
  app.run(
    host='0.0.0.0',
    port=8080
  )
