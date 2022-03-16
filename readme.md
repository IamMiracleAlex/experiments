## Basic Requirements
The basic requirements needed to run this application
- `python 3.8.8` or above
- `Docker` (optional)

## To Run (Docker)
To run this application with docker, please use the following instructions
- `start Docker`, version `3.8` or highter is recommended
- copy `.env.local.sample` to `.env` 
- `docker-compose -f docker-compose.local.yml up --build`
- Go to `localhost:8000` to access the site

## To Run
This application can be run without docker, to do so, please see instructions below:
- Create and activate a virtual environment
- copy `.env.local.sample` to `.env` and update it to have `USE_DOCKER=No`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Go to `localhost:8000` to access the site

## Run Tests
Tests are written using `django.tests.Testcase`, we run all tests as follows:
`python manage.py test`

## Test Coverage
To run the tests, check your test coverage, and generate an HTML coverage report:
-  `coverage erase`
-  `coverage run --source='.' manage.py test `
-  `coverage report` (to view reports on the terminal)
-  `coverage html` and open `htmlcov/index.html` to view reports on the browser


## In Production
To run in production environment, please note the following:
- copy `.env.prod.sample` to `.env` and update it to have `USE_AWS=Yes`
- `docker-compose -f docker-compose.yml up --build`
- Go to `0.0.0.0:80` to access the site