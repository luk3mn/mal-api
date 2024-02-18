class AnimeRankDto:
    def __init__(self, **kwargs) -> None:
        self.__cover = kwargs['cover']
        self.__title = kwargs['title']
        self.__rank = kwargs['rank']
        self.__aired = kwargs['aired']
        self.__popularity = kwargs['popularity']
        self.__studios = kwargs['studios']
        self.__duration = kwargs['duration']
        self.__source = kwargs['source']
        self.__episodes = kwargs['episodes']
        self.__status = kwargs['status']
        self.__members = kwargs['members']

    def get_anime_rank_dto(self) -> dict:
        return {
            "cover": self.__cover,
            "title": self.__title,
            "rank": self.__rank,
            "aired": self.__aired,
            "popularity": self.__popularity,
            "studios": self.__studios,
            "duration": self.__duration,
            "source": self.__source,
            "episodes": self.__episodes,
            "status": self.__status,
            "members": self.__members,
        }
