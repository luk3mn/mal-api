from flask import Blueprint, jsonify
from src.utils.processing import Processing
from src.models.repository.anime_repository import AnimeRepository
from src.main.dto.anime_rank_dto import AnimeRankDto

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

@anime_routes_bp.route('/api/anime')
def anime():
    """ GET /api/anime """
    anime_repository = AnimeRepository("anime_rank")
    response = anime_repository.find_documents()

    anime_rank_dto_list = []
    for r in response:
        anime_rank_dto = AnimeRankDto(
            title=r['titles']['english'],
            genres=r['information']['genres'],
            cover=r['cover'],
            status="Currently Airing",
            score=r['information']['status'],
            episodes=r['information']['episodes']
        )
        anime_rank_dto_list.append(anime_rank_dto.get_anime_dto())

    if not anime_rank_dto_list:
        return jsonify({"Message": "There's no any data into database]"}), 400
    else:
        # print(anime_rank_dto_list)
        return jsonify(anime_rank_dto_list), 201
