from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    name = "John Doe 1"
    mobile = "03036666768"
    languages =["Python", "work", "C++", "Go","C#"]
    #current_date = datetime.now().strftime("%Y-%m-%d")
    
    return render_template('B9.html', name=name, mobile=mobile,languages=languages, current_date=str(datetime.now()))

if __name__ == '__main__':
    app.run(debug=True)