from flask import Flask, request, jsonify

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers_new_python():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = Calculator.add(a, b)
    return jsonify({"result": result})

@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = Calculator.subtract(a, b)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
