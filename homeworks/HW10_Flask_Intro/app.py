from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, it\'s a Flask calculator! ' \
           'Please enter "/calc/"in the address bar, ' \
           'then enter the first number, second number and the action, separated by a "/" sign. ' \
           'Use: ' \
           '"div" for division, ' \
           '"sum" for addition, ' \
           '"dif" for subtraction, ' \
           '"mult" for multiplication.' \
           'Thank you! :)'


@app.route('/calc/')
def hello_calc():
    return "Good! Now enter numbers and action!"


@app.route('/calc/<int:x>/<int:y>/')
def hello_calc_(x, y):
    return f"Good job! You entered {x} and {y}! Now enter an action!"


@app.route('/calc/<int:x>/<int:y>/<string:action>')
def calc(x, y, action):
    if action == 'div':
        if y == 0:
            return render_template('calc.html', y=y)
        return render_template('calc.html', x=x, y=y, action='/', result=x/y)
    elif action == 'sum':
        return render_template('calc.html', x=x, y=y, action='+', result=x+y)
    elif action == 'dif':
        return render_template('calc.html', x=x, y=y, action='-', result=x-y)
    elif action == 'mult':
        return render_template('calc.html', x=x, y=y, action='*', result=x*y)
    else:
        return "Wrong action! :("


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
