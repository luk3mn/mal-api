from flask import Blueprint, jsonify
from src.utils.processing import Processing
from src.models.repository.anime_repository import AnimeRepository
from src.main.dto.anime_rank_dto import AnimeRankDto
from src.main.dto.anime_score_dto import AnimeScoreDto

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
def get_anime() -> jsonify:
    """ GET /api/anime """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    anime_rank_dto_list = []
    for anime in anime_response:
        anime_rank_dto = AnimeRankDto(
            title=anime['titles']['english'],
            genres=anime['information']['genres'],
            cover=anime['cover'],
            status=anime['information']['status'],
            score=anime['statistics']['score'],
            episodes=anime['information']['episodes']
        )
        anime_rank_dto_list.append(anime_rank_dto.get_anime_dto())

    if not anime_rank_dto_list:
        return jsonify({"message": "There's no any data into database]"}), 404
    else:
        return jsonify(anime_rank_dto_list), 201

@anime_routes_bp.route('/api/anime/genre/<string:genre_name>', methods=["GET"])
def get_by_genre(genre_name: str) -> jsonify:
    """ GET /api/anime/genre/{genre_name} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_genre = []
    for anime in anime_response:
        genres = anime['information']['genres']
        if genre_name in [x.lower() for x in genres]:

            anime_rank_dto = AnimeRankDto(
                title=anime['titles']['english'],
                genres=anime['information']['genres'],
                cover=anime['cover'],
                status=anime['information']['status'],
                score=anime['statistics']['score'],
                episodes=anime['information']['episodes']
            )
            filtered_by_genre.append(anime_rank_dto.get_anime_dto())

    if not filtered_by_genre:
        return jsonify({"message":f"Genre '{genre_name}' does not exists"}), 404
    else:
        return jsonify({"message":f"Results to anime by '{genre_name}' genre"}, filtered_by_genre)

@anime_routes_bp.route('/api/anime/score/<anime_score>', methods=["GET"])
def get_by_score(anime_score: int) -> jsonify:
    """ GET /api/anime/score/{anime_score} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_score = []
    for anime in anime_response:
        if int(anime_score) == round(anime['statistics']['score']):
            anime_score_dto = AnimeScoreDto(
                cover=anime['cover'],
                title=anime['titles']['english'],
                score=anime['statistics']['score'],
                aired=anime['information']['aired']
            )

            filtered_by_score.append(anime_score_dto.get_anime_score_dto())

    if not filtered_by_score:
        return jsonify({"message":f"Score '{anime_score}' does not exists"}), 404
    return jsonify(filtered_by_score)
