from flask import Flask, render_template

app = Flask (__name__)


@app.route('/')
def check():
    name="john"
    mobile="03010000000"
    pizza= ["mypizza","pizza","supreme"]

    return render_template('myHtml.html',name=name,mobile=mobile,pizza=pizza)


if __name__ == '__main__':
    app.run(debug=True)        