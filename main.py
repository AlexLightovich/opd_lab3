from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

def calcSin(deg, radordeg, accuracy):
    if type(deg) == str:
        return "error"
    if accuracy != None:
        if accuracy < 0 or type(accuracy) != int:
            return "error"
    else:
        return "error"
    if radordeg != "deg" and radordeg != "rad":
        return "error"
    if radordeg == "deg":
        deg = (deg * math.pi) / 180
    numerator, denominator = math.sin(deg).as_integer_ratio()
    return format(numerator / denominator, f".{accuracy}f")
def calcCos(deg, radordeg, accuracy):
    if type(deg) == str or deg == None:
        return "error"
    if accuracy != None:
        if accuracy < 0 or type(accuracy) != int:
            return "error"
    else:
        return "error"
    if radordeg != "deg" and radordeg != "rad" or type(radordeg) != str:
        return "error"
    if radordeg == "deg":
        deg = (deg * math.pi) / 180
    numerator, denominator = math.cos(deg).as_integer_ratio()
    return format(numerator / denominator, f".{accuracy}f")

def calcTan(deg, radordeg, accuracy):
    if type(deg) == str:
        return "error"
    if accuracy != None:
        if accuracy < 0 or type(accuracy) != int:
            return "error"
    else:
        return "error"
    if radordeg != "deg" and radordeg != "rad":
        return "error"
    if radordeg == "deg":
        deg = (deg * math.pi) / 180
    numerator, denominator = math.tan(deg).as_integer_ratio()
    return format(numerator / denominator, f".{accuracy}f")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        funct = request.form.get('functions')
        deg = (request.form.get('deg'))
        radordeg = request.form.get('radordeg')
        accuracy = int(request.form.get('accuracy'))
        if funct == "sin":
            result = calcSin(float(deg), radordeg, int(accuracy))

        if funct == "cos":
            result = calcCos(float(deg), radordeg, int(accuracy))
        if funct == "tan":
            result = calcTan(float(deg), radordeg, accuracy)
    return render_template('index.html', res=result)


if __name__ == '__main__':
    app.run(debug=True)