import requests
from bs4 import BeautifulSoup
from src.models.database.connection import DBConnectionHandler
from src.models.repository.anime_repository import AnimeRepository

class Processing:
    """ ETL Processing """
    def __init__(self) -> None:
        self.anime_rank: list = []

    def extract_anime_rank(self) -> object:
        """ To extract data from source using web scraping strategy """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        # Connect to the target URL
        page = requests.get('https://myanimelist.net/topanime.php', headers=headers, timeout=3)

        # Init beautiful soup
        soup = BeautifulSoup(page.text, 'html.parser')

        ranking_list = soup.find_all('tr', class_='ranking-list')
        count: int = 0
        for ranking in ranking_list:

            link_details = str(ranking.find('a', class_='hoverinfo_trigger fl-l ml12 mr8')['href'])
            access_details = requests.get(link_details, headers=headers, timeout=10)
            soup_details = BeautifulSoup(access_details.text, 'html.parser')
            leftside = soup_details.find('div', class_='leftside')
            for detail in leftside.find_all('div', class_='spaceit_pad'):
                cover = ranking.find('img')['data-srcset'].split(',')[1].split(' ')[1]
                anime_detail = detail.text.replace('\n','').split(':')

                if anime_detail[0] == "Synonyms":
                    synonyms = anime_detail[1].strip()

                if anime_detail[0] == "Japanese":
                    japanese = anime_detail[1].strip()

                if anime_detail[0] == "English":
                    english = anime_detail[1].strip()

                if anime_detail[0] == "Type":
                    type_ = anime_detail[1].strip()

                if anime_detail[0] == "Episodes":
                    episodes = int(anime_detail[1]) if anime_detail[1].strip() != "Unknown" else anime_detail[1].strip()

                if anime_detail[0] == "Status":
                    status = anime_detail[1].strip()

                if anime_detail[0] == "Aired":
                    aired = anime_detail[1].strip()

                if anime_detail[0] == "Producers":
                    producers = [x.strip() for x in anime_detail[1].split(',')] # remove empty spaces

                if anime_detail[0] == "Studios":
                    studios = [x.strip() for x in anime_detail[1].split(',')] # remove empty spaces

                if anime_detail[0] == "Source":
                    source = anime_detail[1].strip()

                if anime_detail[0] == "Genres":
                    genres = [x.strip()[:-int(len(x.strip())/2)] for x in anime_detail[1].split(',')] # remove empty spaces and duplicate words

                if anime_detail[0] == "Demographic":
                    demographic = anime_detail[1].strip()[:-int(len(anime_detail[1].strip())/2)] # remove duplicate words

                if anime_detail[0] == "Duration":
                    duration = anime_detail[1].strip()

                if anime_detail[0] == "Rating":
                    rating = anime_detail[1].strip()

                if anime_detail[0] == "Score":
                    score = float(anime_detail[1].split(' ')[0][:-1])

                if anime_detail[0] == "Ranked":
                    ranked = int(anime_detail[1].split(' ')[2].split("#")[1][:-2])

                if anime_detail[0] == "Popularity":
                    popularity = int(anime_detail[1].split("#")[1])

                if anime_detail[0] == "Members":
                    members = anime_detail[1].replace(',','.')

                if anime_detail[0] == "Favorites":
                    favorites = float(anime_detail[1].replace(',','.'))

            anime_detail = {
                "cover": cover,
                "titles": {
                    "synonyms": synonyms,
                    "japanese": japanese,
                    "english": english,
                },
                "information": {
                    "type": type_,
                    "episodes": episodes,
                    "status": status,
                    "aired": aired,
                    "producers": producers,
                    "studios": studios,
                    "source": source,
                    "genres": genres,
                    "demographic": demographic,
                    "duration": duration,
                    "rating": rating
                },
                "statistics": {
                    "score": score,
                    "ranked": ranked,
                    "popularity": popularity,
                    "members": members,
                    "favorites": favorites
                }
            }
            self.anime_rank.append(anime_detail)
            count += 1
            print(count)
            synonyms, demographic, english = ['', '', ''] # reset verables

        return self.anime_rank

    def load_anime_rank(self):
        db_handler = DBConnectionHandler()
        db_connection = db_handler.connect_database()

        anime_repository = AnimeRepository("anime_rank", db_connection)

        anime_repository.drop_all()
        for anime in self.anime_rank:
            anime_repository.insert_document(anime)
