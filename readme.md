# Basic Requirements
- `python 3.8.8` or above
- `Docker` (optional)

# To Run (Docker)
- Start Docker
- `docker-compose -f docker-compose-local.yml up --build`
- Go to `localhost:8000` to access the site

# To Run
- Clone this repository
- Create and activate a virtual environment
- `pip install -r requirements_dev.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Go to `localhost:8000` to access the site

# Run Tests
`python manage.py test`

# Test Coverage
-  `coverage erase`
-  `coverage run --source='.' manage.py test `
-  `coverage report` (to view reports on the terminal)
-  `coverage html` and open `htmlcov/index.html` to view reports on the browser
