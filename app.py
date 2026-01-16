from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (Update with your DB details)
# Format: 'mysql+pymysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_SETTING'] = 'mysql+pymysql://admin:your_password@localhost/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    new_product = Product(name=name, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Change host to '0.0.0.0' to make it accessible via Public IP
    app.run(host='0.0.0.0', port=5000, debug=True)
