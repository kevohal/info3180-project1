from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    rooms = db.Column(db.Integer)
    baths = db.Column(db.String(10))
    price = db.Column(db.String(100))
    type = db.Column(db.String(10))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(50))

    def __init__(self, id, title, description, rooms, baths, price, type, location, photo):
        self.id = id
        self.title = title
        self.description = description
        self.rooms = rooms
        self.baths = baths
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)
