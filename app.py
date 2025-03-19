from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    myName=''
    myMobile=''
    myEmail=''
    message=''
    if request.method == 'POST':
        myName = request.form['name']
        myMobile = request.form['mobile']   
        myEmail = request.form['email']
        message = 'Form submited successfully'
    return render_template('index.html', name=myName, mobile=myMobile, email=myEmail, message=message)

@app.route('/save')
def save():
    saveM='checking save'
    name='john doe'
    name1='acc'
    return render_template('index.html' , save=saveM, name=name,name1=name1)
if __name__ == '__main__':
    app.run(debug=True)
