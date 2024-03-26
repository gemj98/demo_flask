from flask import Flask, render_template, request

app = Flask('__name__')

# @app.route('/<val>')
# def home(val):
#     return render_template('index.html')

@app.route('/<val>')
def home(val):
    return render_template('index.html', val=val)

@app.route('/new')
def new_route():
    return render_template('index.html')

@app.route('/acc_var/<val>')
def read_val(val):
    return 'The value is %s' %val

@app.route('/calculate', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1',type=float)
        num2 = request.form.get('num2',type=float)
        result = num1 + num2
    return render_template('calculate.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)