from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


@app.route('/test')
def somthing():
    l = [1,2,3,4,5]
    articles = ['Учебники ','Как установить питон ', 'УпП%;П;%' ]
    return render_template('test.html' , lst = l)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == "__main__":
    app.run(debug=True)
