from dgroup import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"#{self.id} - Client: {self.client} | Rating: {self.rating}"
