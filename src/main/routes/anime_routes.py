from flask import Blueprint, jsonify
from src.utils.processing import Processing

anime_routes_bp = Blueprint('anime_routes', __name__)

@anime_routes_bp.route('/', methods=["GET"])
def index():
    return "Home application"

@anime_routes_bp.route('/populate', methods=["GET"])
def populate_db():
    try:
        processing = Processing()

        processing.extract_anime_rank()
        processing.load_anime_rank()

        return jsonify({"message": "All of your data has been populate into database successfuly!"})
    except Exception:
        return jsonify({"message": "Something went wrong!"}), 500
