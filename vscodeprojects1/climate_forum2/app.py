from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    file = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'


# Simulated database
posts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        file = request.form["file"]
        posts.append({'name': name, 'message': message})
        return redirect(url_for('forum'))
    return render_template('forum.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)