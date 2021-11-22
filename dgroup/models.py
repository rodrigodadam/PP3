from dgroup import db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text(1000), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Client: {self.client} | Rating: {self.rating}"