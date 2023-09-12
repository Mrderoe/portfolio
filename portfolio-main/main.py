from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.ddb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ddb = SQLAlchemy(app)

class Comment(ddb.Model):
    id = ddb.Column(ddb.Integer, primary_key=True, autoincrement=True)
    login = ddb.Column(ddb.Text, nullable=False)
    text = ddb.Column(ddb.Text, nullable=False)

# Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')

# Динамичные скиллы
@app.route('/', methods=['POST','Flesh'])
def process_form():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        button_python = request.form.get('button_python')

        comment = Comment(login=email, text=text)  # Исправлено на text
        ddb.session.add(comment)
        ddb.session.commit()

    return render_template('index.html', button_python=button_python)

if __name__ == "__main__":
    app.run(debug=True)
