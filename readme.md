## Basic Requirements
- `python 3.8.8` or above
- `Docker` (optional)

## To Run (Docker)
- Start Docker
- copy `.env.local.sample` to `.env` 
- `docker-compose -f docker-compose.local.yml up --build`
- Go to `localhost:8000` to access the site

## To Run
- Create and activate a virtual environment
- copy `.env.local.sample` to `.env` and update it to have `USE_DOCKER=No`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Go to `localhost:8000` to access the site

## Run Tests
`python manage.py test`

## Test Coverage
-  `coverage erase`
-  `coverage run --source='.' manage.py test `
-  `coverage report` (to view reports on the terminal)
-  `coverage html` and open `htmlcov/index.html` to view reports on the browser


## In Production
- copy `.env.prod.sample` to `.env` and update it to have `USE_AWS=Yes`
- `docker-compose -f docker-compose.yml up --build`
- Go to `0.0.0.0:80` to access the site