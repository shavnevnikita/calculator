from decimal import *
from flask import Flask, render_template, request

app = Flask(__name__)

def nicify(num):
    digits = list(str(num).rstrip('0'))
    dot_pos = digits.index('.')
    if digits[-1] == '.':
        digits.pop()
    new_digits = []
    for i in range(dot_pos):
        new_digits.append(digits[i])
        if (i+1) % 3 == dot_pos % 3:
            new_digits.append(" ")
    if new_digits[-1] == " ":
        new_digits.pop()
    for i in range(dot_pos, len(digits)):
        new_digits.append(digits[i])
    return "".join(new_digits)

@app.route("/", methods=["post", "get"])
def main():
    return render_template('main.html')

@app.route("/calculate", methods=["post"])
def calculate():
    a = request.json["a"].replace(',','.').replace(' ','')
    b = request.json["b"].replace(',','.').replace(' ','')
    a = Decimal(a)
    b = Decimal(b)
    op = request.json["op"]
    answ = 0
    if op == "+":
        answ = a+b
    elif op == "-":
        answ = a-b
    elif op == "*":
        answ = a*b
    elif op == "/":
        answ = a/b
    answ = answ.quantize(Decimal('.000001'), rounding=ROUND_HALF_DOWN)
    return {"result": nicify(answ)}

app.run(
    host='0.0.0.0',
    port=8080
)
