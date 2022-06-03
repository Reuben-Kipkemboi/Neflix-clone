# Netflix Clone

#### By Reuben Kipkemboi

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#installation-requirements)
+ [Technology Used](#technologies-used)
+ [License](#license)
+ [Authors Info](#authors-info)

## Description
A clone the popular Movie streaming website Netflix. You are challenged to use  The movie database API  to display all the movies available.In future include the use of Youtube API to show movie trailers.


[Go Back to the top](#netflix-clone)


## User Stories

User Can :-

* As a user I would like to view the different movies and Tv shows that are available
* As a user I would like to search for my favorite Tv show and movie.
* As a user I would like to view a description Of the movie and its current rating.
* As a user I would like to save the movie to my Playlist to view whenever i liked.
* As a user I would like to watch a trailer for a movie or a Tv Show.
* As a user I should be able to create a profile on the web app.
* As a user I should be able to select categories that Interest me and get movie recommendations according to those categories.

[Go Back to the top](#netflix-clone)

## Installation Requirements

### Prerequisites

- Django
- Python
- Heroku
- postgres

## Instructions

To get the project .......  
  
##### Clone Repository:  
 ```bash 
https://github.com/Reuben-Kipkemboi/Neflix-clone.git 
```
##### Install and activate Virtual Environment virtual  
 ```bash 
cd netflix && python3 -m venv virtual && source virtual/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  
 ```bash 
python manage.py makemigrations news 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py runserver 
 or
 ./manage.py runserver
```
##### Test Application  
 ```bash 
 python manage.py test app
```
Open the application on your browser `127.0.0.1:8000`.  

[Go Back to the top](#netflix-clone)


## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE)

## Live Site

#### https://netflix-flix.herokuapp.com/

## Known bugs

* User login
* Application breaks at some point due to invalid response from the API


## Author's Info

* :email: [Reuben Kipkemboi](https://gmail.com)  

<p align = "center">
    &copy; 2022 @Reuben Kipkemboi.
</p>
