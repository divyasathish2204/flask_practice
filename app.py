from flask import Flask,request
obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "WELCOME TO THE FLASK"

@obj.route('/calculate',methods = ['GET'])
def math_operator():
    operation = request.json['operation']
    number1 = request.json['number1']
    number2 = request.json['number2']
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return "The operation is {} and the result is {}".format(operation,result)
        

if __name__ == '__main__':
    obj.run(debug=True)


