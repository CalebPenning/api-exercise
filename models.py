"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Instance of our cupcake class."""
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
    flavor = db.Column(db.String, nullable=False)
    
    size = db.Column(db.String, nullable=False)
    
    rating = db.Column(db.Float, nullable=False, default=0.0)
    
    image = db.Column(db.String, nullable=False, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
        
    def __repr__(self):
        return f"<Cupcake id={self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>"