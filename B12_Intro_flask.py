from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('B12_jinja.html',name="Nouman",age=28)
@app.route('/home')
def home1():
    return render_template('B12_jinja.html',age=22)

if __name__ == '__main__':
    app.run(debug=True)
