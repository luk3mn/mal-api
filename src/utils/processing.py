import requests
from bs4 import BeautifulSoup

class Processing:
    """ ETL Processing """
    def __init__(self) -> None:
        pass

    def extract(self):
        """ To extract data from source using web scraping strategy """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        # Connect to the target URL
        page = requests.get('https://myanimelist.net/topanime.php', headers=headers, timeout=3)

        # Init beautiful soup
        soup = BeautifulSoup(page.text, 'html.parser')

        anime_rank: list = []
        ranking_list = soup.find_all('tr', class_='ranking-list')
        count: int = 0
        for ranking in ranking_list:

            link_details = str(ranking.find('a', class_='hoverinfo_trigger fl-l ml12 mr8')['href'])
            access_details = requests.get(link_details, headers=headers, timeout=10)
            soup_details = BeautifulSoup(access_details.text, 'html.parser')
            leftside = soup_details.find('div', class_='leftside')

            for detail in leftside.find_all('div', class_='spaceit_pad'):
                anime_detail = detail.text.replace('\n','').split(':')

                if anime_detail[0] == "Synonyms":
                    synonyms = anime_detail[1]

                if anime_detail[0] == "Japanese":
                    japanese = anime_detail[1]

                if anime_detail[0] == "English":
                    english = anime_detail[1]

                if anime_detail[0] == "Type":
                    type_ = anime_detail[1]

                if anime_detail[0] == "Episodes":
                    episodes = anime_detail[1]

                if anime_detail[0] == "Status":
                    status = anime_detail[1]

                if anime_detail[0] == "Aired":
                    aired = anime_detail[1]

                if anime_detail[0] == "Producers":
                    producers = anime_detail[1].split(',')

                if anime_detail[0] == "Studios":
                    studios = anime_detail[1].split(",")

                if anime_detail[0] == "Source":
                    source = anime_detail[1]

                if anime_detail[0] == "Genres":
                    genres = anime_detail[1].split(",")

                if anime_detail[0] == "Demographic":
                    demographic = anime_detail[1]

                if anime_detail[0] == "Duration":
                    duration = anime_detail[1]

                if anime_detail[0] == "Rating":
                    rating = anime_detail[1]

                if anime_detail[0] == "Score":
                    score = anime_detail[1].split(' ')[0][:-1]

                if anime_detail[0] == "Ranked":
                    ranked = anime_detail[1].split(' ')[2].split("#")[1][:-2]

                if anime_detail[0] == "Popularity":
                    popularity = anime_detail[1]

                if anime_detail[0] == "Members":
                    members = anime_detail[1]

                if anime_detail[0] == "Favorites":
                    favorites = anime_detail[1]

            anime_detail = {
                "titles": {
                    "Synonyms": synonyms,
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
            anime_rank.append(anime_detail)
            count += 1
            print(count)
            synonyms, demographic, english = ['', '', ''] # reset verables

        return anime_rank
