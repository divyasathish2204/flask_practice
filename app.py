from flask import Flask,request,render_template
obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "WELCOME TO THE FLASK"

@obj.route('/calculate',methods = ['GET'])
def math_operator():
    operation = request.json['operation']
    number1 = request.form['number1']
    number2 = request.form['number2']
    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    else:
        result=number1-number2
    return result
        

if __name__ == '__main__':
    obj.run(debug=True)


