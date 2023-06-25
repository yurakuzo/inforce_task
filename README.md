# Inforce Task

Clone repository to your local machine

`git clone https://github.com/yurakuzo/inforce_task.git`

Get into clonned directory

`cd inforce_task`

Create `.env` file based on `.env.sample`

Build docker containers

`docker-compose up --build`

Open `localhost:<your_app_port>` in browser. (I will use 8000 as example)

## App routes:
 - http://localhost:8000/api-auth/ - basic **DRF** urls
    - http://localhost:8000/api-auth/login
    - http://localhost:8000/api-auth/logout
 - http://localhost:8000/restaurant-api/ - all routes related to menus and restaurants
    - http://localhost:8000/restaurant-api/menus - GET, POST, PUT, DELETE
    - http://localhost:8000/restaurant-api/menus/today - GET
    - http://localhost:8000/restaurant-api/menus/most_voted - GET
    - http://localhost:8000/restaurant-api/restaurants - GET, POST, PUT, DELETE
 - http://localhost:8000/auth/ - JWT and Employees, Votes endpoints
    - http://localhost:8000/auth/votes - GET, POST, PUT, DELETE
    - http://localhost:8000/auth/employees - GET, POST, PUT, DELETE
    - http://localhost:8000/auth/login/
    - http://localhost:8000/auth/logout/
    - http://localhost:8000/auth/register/

To run tests just exec it with docker

`docker-compose exec app pytest`

Also you can try using flake8:

Get into app container `docker-compose exec app sh`

Run:
- `flake8 ./auth_app/`
- `flake8 ./main_app/`
- `flake8 ./restourant_vote/`

PS. There are definitely problems with permissions, tests but I'm ready and really motivated to improve my skills : )
    