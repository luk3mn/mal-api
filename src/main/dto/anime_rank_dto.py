class AnimeRankDto:
    def __init__(self, **kwargs) -> None:
        self.__cover = kwargs['cover']
        self.__title = kwargs['title']
        self.__genres = kwargs['genres']
        self.__episodes = kwargs['episodes']
        self.__status = kwargs['status']
        self.__score = kwargs['score']

    def get_anime_dto(self):
        return [
            {
                "cover": self.__cover,
                "title": self.__title,
                "genres": self.__genres,
                "episodes": self.__episodes,
                "status": self.__status,
                "score": self.__score
            }
        ]
