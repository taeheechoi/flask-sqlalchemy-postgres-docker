import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Contacts(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    