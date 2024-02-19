from flask import Flask
from flask_cors import CORS
from src.main.routes.anime_routes import anime_routes_bp

app = Flask(__name__)

app.register_blueprint(anime_routes_bp)
CORS(app)
