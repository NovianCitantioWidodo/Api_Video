from app import app, db
from app.model.user import User

class Video(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    # owner = db.Column(db.BigInteger, db.ForeignKey(User.id))
    

    def __repr__(self):
        return f'<Video {self.name}>'