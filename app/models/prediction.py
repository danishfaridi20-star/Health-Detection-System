from app.extensions import db

class Prediction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    symptoms = db.Column(db.Text)
    disease = db.Column(db.String(100))
    confidence = db.Column(db.Float)
    explanation = db.Column(db.Text)
    precautions = db.Column(db.Text)
    