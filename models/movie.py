movie_catalog = []

def get_id():
    if (movie_catalog):
        return len(movie_catalog)
    else:
        return 1


class Movie:

    def __init__(self, name , image, alt, genre_id, url, price_for_rent, price_for_buy, count_rent, count_buy, rating, num_reviews):
        self.id = get_id()
        self.name = name
        self.image = image
        self.alt = alt
        self.rating = rating
        self.url = url
        self.genre_id = genre_id
        self.price_for_rent = price_for_rent 
        self.price_for_buy =  price_for_buy 
        self.count_rent = count_rent
        self.count_buy = count_buy
        self.num_reviews =  num_reviews

    @property
    def data(self):
        return {
           

       'name' :self.name ,
       'image' : self.image ,
       'alt' : self.alt ,
       'rating' : self.rating ,
       'url' : self.url ,
       'genre_id' : self.genre_id ,
       'price_for_rent' : self.price_for_rent , 
       'price_for_buy' : self.price_for_buy , 
       'count_rent' : self.count_rent , 
       'count_buy' : self.count_buy , 
       'num_reviews' : self.num_reviews 
        }