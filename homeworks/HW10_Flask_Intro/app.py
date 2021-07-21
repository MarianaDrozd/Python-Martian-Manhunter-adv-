from flask import Flask, render_template

app = Flask(__name__)

ACTIONS = {'sum': '+', 'dif': '-', 'mult': '*', 'div': '/'}


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return '''Hey, it\'s a Flask calculator!  \
           Please enter "/calc/"in the address bar,  \
           then enter the action and "/". \
           ***HINT!***\
            Use:  \
           "div" for division, \
           "sum" for addition, \
           "dif" for subtraction, \
           "mult" for multiplication. \
           Then enter the first number like "x=1" and the second number like "y=2" separated by a "," sign. 
           Thank you! :)'''


@app.route('/calc/')
def hello_calc():
    return 'Good! Now enter the action and numbers!'


@app.route('/calc/<string:action>')
def hello_calc_(action):
    return f'Good job! You entered an action {action}! Now enter the numbers!'


@app.route('/calc/<string:action>/x=<int:x>,y=<int:y>', methods=['GET', 'POST'])
def calc(action, x, y):
    act = ACTIONS.get(action)
    if act:
        try:
            return render_template('calc.html', x=x, y=y, action=str(act), result=eval(f'{x} {act} {y}'))
        except ZeroDivisionError:
            return render_template('zerodivisionerror.html')
    return render_template('incorrect_action.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
