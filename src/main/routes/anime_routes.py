from flask import Blueprint, jsonify
from src.utils.processing import Processing
from src.models.repository.anime_repository import AnimeRepository
from src.main.dto.anime_dto import AnimeDto
from src.main.dto.anime_score_dto import AnimeScoreDto
from src.main.dto.anime_rank_dto import AnimeRankDto

anime_routes_bp = Blueprint('anime_routes', __name__)

@anime_routes_bp.route('/', methods=["GET"])
def index():
    return "Home application"

@anime_routes_bp.route('/api/v1/anime/extract', methods=["GET"])
def populate_db():
    """ GET /api/v1/anime/extract """
    try:
        processing = Processing()
        processing.extract_anime_rank()
        processing.load_anime_rank()

        return jsonify({"message": "All of your data has been populate into database successfuly!"})
    except Exception:
        return jsonify({"message": "Something went wrong!"}), 500

@anime_routes_bp.route('/api/v1/anime')
def get_anime() -> jsonify:
    """ GET /api/v1/anime """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    anime_rank_dto_list = []
    for anime in anime_response:
        anime_dto = AnimeDto(
            title=anime['titles']['japanese'],
            genres=anime['information']['genres'],
            cover=anime['cover'],
            status=anime['information']['status'],
            score=anime['statistics']['score'],
            episodes=anime['information']['episodes']
        )
        anime_rank_dto_list.append(anime_dto.get_anime_dto())

    if not anime_rank_dto_list:
        return jsonify({"message": "There's no any data into database]"}), 404
    else:
        return jsonify(anime_rank_dto_list)

@anime_routes_bp.route('/api/v1/anime/genre/<string:genre_name>', methods=["GET"])
def get_by_genre(genre_name: str) -> jsonify:
    """ GET /api/v1/anime/genre/{genre_name} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_genre = []
    for anime in anime_response:
        genres = anime['information']['genres']
        if genre_name in [x.lower() for x in genres]:

            anime_dto = AnimeDto(
                title=anime['titles']['japanese'],
                genres=anime['information']['genres'],
                cover=anime['cover'],
                status=anime['information']['status'],
                score=anime['statistics']['score'],
                episodes=anime['information']['episodes']
            )
            filtered_by_genre.append(anime_dto.get_anime_dto())

    if not filtered_by_genre:
        return jsonify({"message":f"Genre '{genre_name}' does not exists"}), 404
    else:
        return jsonify({"message":f"Results to anime by '{genre_name}' genre"}, filtered_by_genre)

@anime_routes_bp.route('/api/v1/anime/score/<anime_score>', methods=["GET"])
def get_by_score(anime_score: int) -> jsonify:
    """ GET /api/v1/anime/score/{anime_score} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_score = []
    for anime in anime_response:
        if int(anime_score) == round(anime['statistics']['score']):
            anime_score_dto = AnimeScoreDto(
                cover=anime['cover'],
                title=anime['titles']['japanese'],
                score=anime['statistics']['score'],
                aired=anime['information']['aired']
            )

            filtered_by_score.append(anime_score_dto.get_anime_score_dto())

    if not filtered_by_score:
        return jsonify({"message":f"Score '{anime_score}' does not exists"}), 404
    return jsonify(filtered_by_score)

@anime_routes_bp.route('/api/v1/anime/rank/<anime_rank>', methods=["GET"])
def get_by_rank(anime_rank: int) -> jsonify:
    """ GET /api/v1/anime/rank/{anime_rank} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_rank = []
    for anime in anime_response:
        if int(anime_rank) == anime['statistics']['ranked']:
            anime_rank_dto = AnimeRankDto(
                cover=anime['cover'],
                title=anime['titles']['japanese'],
                popularity=anime['statistics']['popularity'],
                rank=anime['statistics']['ranked'],
                aired=anime['information']['aired'],
                source=anime['information']['source'],
                episodes=anime['information']['episodes'],
                duration=anime['information']['duration'],
                status=anime['information']['status'],
                studios=anime['information']['studios'],
                members=anime['statistics']['members'],
            )
            filtered_by_rank.append(anime_rank_dto.get_anime_rank_dto())

    if not filtered_by_rank:
        return jsonify({"message":f"The rank '{anime_rank}' does not exists"}), 404
    return jsonify(filtered_by_rank)

@anime_routes_bp.route('/api/v1/anime/name/<anime_name>', methods=["GET"])
def get_by_name(anime_name: int) -> jsonify:
    """ GET /api/v1/anime/name/{anime_name} """
    anime_repository = AnimeRepository("anime_rank")
    anime_response = anime_repository.find_documents()

    filtered_by_name = []
    for anime in anime_response:
        if anime_name in anime['titles']['japanese'].lower() or anime_name in anime['titles']['english'].lower():
            filtered_by_name.append(anime)

    if not filtered_by_name:
        return jsonify({"message":f"There's no an anime by name '{anime_name}' in this list"}), 404
    else:
        return jsonify({"message":f"Results to anime by name '{anime_name}'"}, filtered_by_name)
