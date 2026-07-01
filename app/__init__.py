from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from app.models.prediction import Prediction
    from app.routes.prediction import prediction_bp

    app.register_blueprint(prediction_bp)

    with app.app_context():
        db.create_all()

    return app