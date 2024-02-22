<a name="mal-api"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/luk3mn/mal-api">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/58/MyAnimeList_-_Full_Text_Logo.jpg" alt="Logo" width="160" height="80">
  </a>

  <h3 align="center">MAL - API</h3>

  <p align="center">
    Back-end web application using Python and Flask to build a Rest API by extracting data from <a href='https://myanimelist.net/'>My Anime List</a> through web scraping.
    <br />
    <a href="https://github.com/luk3mn/mal-api/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
![Home](src/assets/diagram.png)


<p align="justify">
  [...] 

  In this project, it was necessary to split it into three parts, such as: 
  - **ETL Pipeline:** Extraction using web scraping strategy, transformation of these data and load in the MongoDB database;
  - **Database configuration:** configuration to assist a connection from Flask application to MongoDB collections;
  - **Build Rest API:** It was created some endpoints API to consume these data from the database;
</p> 

### Extract and Validation
All the data used in this project belongs to <a href='https://myanimelist.net/'>My Anime List</a> extracted by web scraping method and it was possible by using the library **"Beautiful Soup"**. During this process, it was able to go through several contents and organize them to store in a dictionary to facilitate some validation process before loading in the MongoDB database.


### Load on MongoDB
To be able to create a connection between Flask and MongoDB, it was necessary to use the library **"pymongo"** which facilitated a bunch of features that included connection resources and collection manipulation.


### REST API
The API endpoints were built using the Flask framework from Python and on top of that, it was needed to create a DTO class to limit the quantity of information during endpoint requests.

---
#### Extract new data from the data source

```http
  GET /api/v1/anime/extract
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None`    |  `None`  | **Required**. to extract and load new data |

---
#### List all anime

```http
  GET /api/v1/anime
```

| Parameter     | Type     |     Description      |
| :-------------| :------- | :------------------- |
| `None`        | `None`   | to list all anime    |

---
#### Get by anime name
```http
  GET /api/v1/anime/name/${anime_name}
```

| Parameter     | Type     |     Description      |
| :-------------| :------- | :------------------- |
| `anime_name`  | `string`    | to get anime by name |

---
#### Get anime by genre
```http
  GET /api/v1/anime/genre/${genre_name}
```

| Parameter     | Type     |     Description      |
| :-------------| :------- | :------------------- |
| `genre_name`  | `string`    | to get anime by genre |

---
#### Get anime by rank
```http
  GET /api/v1/anime/rank/${anime_rank}
```

| Parameter     | Type     |     Description      |
| :-------------| :------- | :------------------- |
| `anime_rank`  | `integer`    | to get anime by rank |

---
#### Get anime by score
```http
  GET /api/v1/anime/score/${anime_score}
```

| Parameter      | Type     |     Description      |
| :--------------| :------- | :------------------- |
| `anime_score`  | `integer`    | to get anime by score |



<p align="right">(<a href="#mal-api">back to top</a>)</p>



### Built With

Write here

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Mongo][Mongo]][Mongo-url]

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here are some important topics about this project and how to replay it.

### Prerequisites

* virtualenv
  ```sh
  python3 -m venv .venv
  ```

* Environment Variables
  
  To run this project, you will need to add the following environment variables to your **.env** file

  `HOST`

  `PORT`

  `DB_NAME`

### Installation

_Before starting this application in your local environment, it'll be necessary to proceed with some tasks to reproduce this project._

1. Clone the repo
   ```sh
   git clone https://github.com/luk3mn/mal-api.git
   ```
2. Install packages
   ```sh
   pip freeze -r requirements.txt
   ```

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage / Examples

<!-- ### Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here) -->




<!-- ROADMAP -->
## Roadmap

> Processing
- [x] Extract: get data from the source using web scraping
- [x] Transform: to valid some information before storing it in the database
- [x] Load: store data in MongoDB database

> MongoDB
- [x] Database configuration
- [x] Working on repository class

> API Rest
- [x] GET /api/v1/anime/extract
- [x] GET /api/v1/anime
- [x] GET /api/v1/anime/name/{anime_name}
- [x] GET /api/v1/anime/genre/{genre_name}
- [x] GET /api/v1/anime/rank/{anime_rank}
- [x] GET /api/v1/anime/score/{anime_score}

> Deploy
- [ ] AWS

<p align="right">(<a href="#mal-api">back to top</a>)</p>

<!-- ## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them? -->

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#mal-api">back to top</a>)</p>


<!-- CONTACT -->
## Authors

- username: [@luk3mn](https://www.github.com/luk3mn)

## Feedback

If you have any feedback, please reach out to us at lucasnunes2030@gmail.com

> Project Link: [https://github.com/luk3mn/mal-api](https://github.com/luk3mn/mal-api)

<p align="right">(<a href="#mal-api">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I think it would be interesting to place here some references and other resources that were useful and helped me to work on this project.
* [Web Scraping With Python – Step-By-Step Guide](https://brightdata.com/blog/how-tos/web-scraping-with-python)
* [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
* [StackOverflow](https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection)
* [w3schools: Python MongoDB Find](https://www.w3schools.com/python/python_mongodb_find.asp)
* [How to Use *args and **kwargs in Python](https://www.freecodecamp.org/news/args-and-kwargs-in-python/)
* [Design Patterns for REST-APIs](https://medium.com/@patricksavalle/rest-api-design-as-a-craft-not-an-art-a3fd97ed3ef4)

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/luk3mn/mal-api.svg?style=for-the-badge
[contributors-url]: https://github.com/luk3mn/mal-api/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/luk3mn/mal-api.svg?style=for-the-badge
[issues-url]: https://github.com/luk3mn/mal-api/issues
[forks-shield]: https://img.shields.io/github/forks/luk3mn/mal-api.svg?style=for-the-badge
[forks-url]: https://github.com/luk3mn/mal-api/network/members
[stars-shield]: https://img.shields.io/github/stars/luk3mn/mal-api.svg?style=for-the-badge
[stars-url]: https://github.com/luk3mn/mal-api/stargazers
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/luk3mn/mal-api/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/lucasmaues/
[general-code-screenshot]: assets/general-project.png

<!-- Stack Shields -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffffff
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=ffffff
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Mongo]: https://img.shields.io/badge/Mongodb-green?style=for-the-badge&logo=mongodb&logoColor=ffffff
[Mongo-url]: https://www.mongodb.com/docs/