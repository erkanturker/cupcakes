"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    __tablename__="cupcakes"

    id= db.Column(db.Integer, primary_key= True)
    flavor = db.Column(db.Text, nullable =False)
    size  = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text,nullable=False,default="https://tinyurl.com/demo-cupcake" )

    def __repr__(self):
        return f"<Cupcake(id={self.id}, flavor={self.flavor}, size={self.size}, rating={self.rating}, image={self.image})>"
    
    def serialize(cup_cake):
         """Serialize a Cupcake SQLAlchemy obj to dictionary."""

         return {
             "id":cup_cake.id,
             "flavor":cup_cake.flavor,
             "size":cup_cake.size,
             "rating":cup_cake.rating,
             "image":cup_cake.image
         }



