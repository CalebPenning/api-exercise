"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'sugarsugarhoneyhoney'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    all_cakes = Cupcake.query.all()
    return render_template('index.html', cakes=all_cakes)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    all_cakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cakes)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    new_cake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cake)
    db.session.commit()
    resp_cake = jsonify(cupcake=new_cake.serialize())
    return (resp_cake, 201)

@app.route('/api/cupcakes/<int:c_id>')
def get_one_cupcake(c_id):
    cake = Cupcake.query.get_or_404(c_id)
    return jsonify(cupcake=cake.serialize())

@app.route('/api/cupcakes/<int:c_id>', methods=['PATCH'])
def update_cupcake(c_id):
    cake = Cupcake.query.get_or_404(c_id)
    
    cake.flavor = request.json.get('flavor', cake.flavor)
    cake.size = request.json.get('size', cake.size)
    cake.rating = request.json.get('rating', cake.rating)
    cake.image = request.json.get('image', cake.image)
    return jsonify(cupcake=cake.serialize())

@app.route('/api/cupcakes/<int:c_id>', methods=['DELETE'])
def delete_cupcake(c_id):
    cake = Cupcake.query.get_or_404(c_id)
    db.session.delete(cake)
    db.session.commit()
    return jsonify(message="Deleted.")