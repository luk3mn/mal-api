class AnimeScoreDto:
    def __init__(self, **kwargs) -> None:
        self.__cover = kwargs['cover']
        self.__title = kwargs['title']
        self.__score = kwargs['score']
        self.__aired = kwargs['aired']

    def get_anime_score_dto(self):
        return {
            "cover": self.__cover,
            "title": self.__title,
            "score": self.__score,
            "aired": self.__aired
        }
