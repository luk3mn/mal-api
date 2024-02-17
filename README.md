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
    <!-- <img src="https://pipedream.com/s.v0/app_mqeh75/logo/orig" alt="Logo" width="80" height="80"> -->
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
  - **ETL Pipeline:** ...;
  - **Database configuration:** ...;
  - **Build Rest API:** ...;
</p> 

### Processing

> Extract

> Transform

> Load



<p align="right">(<a href="#mal-api">back to top</a>)</p>



### Built With

Write here

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Mongo][Mongo]][Mongo-url]
<!-- * [![Pandas][Pandas]][Pandas-url] -->

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here are some important topics about this project and how to replay it.

### Prerequisites

* virtualenv
  ```sh
  python3 -m venv .venv
  ```

### Installation

_Before starting this application in your local environment, it'll be necessary to proceed with some tasks to reproduce this project._

1. Get API Access [https://developer.spotify.com](https://developer.spotify.com/documentation/web-api)
2. Clone the repo
   ```sh
   git clone https://github.com/luk3mn/mal-api.git
   ```
3. Install packages
   ```sh
   pip freeze -r requirements.txt
   ```

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


<!-- ROADMAP -->
## Roadmap

> Processing
- [x] Extract: get data from source using web scrapping
- [x] Transform: to valid some information before storing in database
- [x] Load: store data into mongodb database

> MongoDB
- [x] Database configuration
- [x] Working on repository class

> API Rest
- [x] GET /api/anime
- [ ] GET /api/anime/name/{anime_name}
- [x] GET /api/anime/genre/{genre_name}
- [ ] GET /api/anime/rating/{anime_rank}
- [ ] GET /api/anime/score/{anime_score}

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#mal-api">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Lucas Renan - lucasnunes2030@gmail.com

Project Link: [https://github.com/luk3mn/mal-api](https://github.com/luk3mn/mal-api)

<p align="right">(<a href="#mal-api">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I think it would be interesting to place here some references and other resources that were really useful and helped me to work on this project.
* [Web Scraping With Python – Step-By-Step Guide](https://brightdata.com/blog/how-tos/web-scraping-with-python)
* [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
* [StackOverflow](https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection)
* [w3schools: Python MongoDB Find](https://www.w3schools.com/python/python_mongodb_find.asp)
* [How to Use *args and **kwargs in Python](https://www.freecodecamp.org/news/args-and-kwargs-in-python/)

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
<!-- [Pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=ffffff
[Pandas-url]: https://pandas.pydata.org/ -->