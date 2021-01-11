from extensions import db

movie_catalog = []

def get_id():
    if (movie_catalog):
        return len(movie_catalog) + 1
    else:
        return 1


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image =   db.Column(db.String(300))
    alt =  db.Column(db.String(200))
    rating =  db.Column(db.Float)
    url = db.Column(db.String(100))
    genre_id =  db.Column(db.Integer)
    price_for_rent = db.Column(db.Float) 
    price_for_buy =  db.Column(db.Float) 
    count_rent = db.Column(db.Integer)
    count_buy = db.Column(db.Integer)
    num_reviews =  db.Column(db.Integer)
    is_available  = db.Column(db.Boolean(), default=False)
   
        
