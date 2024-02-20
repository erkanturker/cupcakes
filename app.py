"""Flask app for Cupcakes"""

from flask import Flask,jsonify,request,render_template
from models import connect_db,db,Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']="ekremAsimZehraErkan"

connect_db(app)
app.app_context().push()

@app.route("/")
def show_cupcakes():
    cupcakes = Cupcake.query.all()
    return render_template("index.html",cupcakes=cupcakes)


# *****************************
# RESTFUL TODOS JSON API
# *****************************

@app.route('/api/cupcakes')
def list_cupcakes():
    db_cup_cakes= Cupcake.query.all()
    dict_cup_cakes = [cup_cake.serialize() for cup_cake in db_cup_cakes ]

    return jsonify(cupcakes=dict_cup_cakes)

@app.route("/api/cupcakes/<int:id>")
def show_cup_cake(id):
    db_cupcake = Cupcake.query.get_or_404(id)
    dict_cup_cake = db_cupcake.serialize()

    return jsonify(cupcake=dict_cup_cake)

@app.route("/api/cupcakes",methods=['POST'])
def add_cup_cake():
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image', None)  # Set default value to None if 'image' key is not present

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json=jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)

@app.route("/api/cupcakes/<int:id>",methods=['PATCH'])
def update_cup_cake(id):
    db_cupcake = Cupcake.query.get_or_404(id)

    db_cupcake.flavor = request.json.get('flavor',db_cupcake.flavor)
    db_cupcake.size = request.json.get('size',db_cupcake.size)
    db_cupcake.rating = request.json.get('rating',db_cupcake.rating)
    db_cupcake.image = request.json.get('image',db_cupcake.image)

    db.session.commit()

    return jsonify(cupcake=db_cupcake.serialize())

@app.route("/api/cupcakes/<int:id>",methods=['DELETE'])
def delete_cup_cake(id):
    db_cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(db_cupcake)
    db.session.commit()

    return jsonify(message="deleted")













