
# Nasa Exoplanet Query

## Objective
Allown informations about exoplanets to be searched easily  and beautifully.

## Screenshots
![landpage](https://user-images.githubusercontent.com/15112609/122652816-4068e000-d117-11eb-97a9-e97cdc639bdb.png)

![Screenshot from 2021-06-26 14-34-51](https://user-images.githubusercontent.com/15112609/123521262-f1c5c380-d68b-11eb-8dc9-a29db5c06ffe.png)

## How to use

Clone the repository.
```
git clone https://github.com/elicaciocdefarias/nasa-exoplanet-query.git
```

Access the project folder, 
```
cd nasa-exoplanet-query/
```

Open settings.yaml file and change the value of the variables BASE_DIR and NAME.
> Notes:
> The value of **parent_dir** must be the full path to the folder 
> where the project was cloned.
```
BASE_DIR: /<parent_dir>/nasa-exoplanet-query
DATABASES:
    default:
      ENGINE: django.db.backends.sqlite3
      NAME: /<parent_dir>/nasa-exoplanet-query/db.sqlite3
```

In the root project, create a file called .secrets.yaml and add bellow code.
> Notes:
> don't forget to change the value of the variable.
```
---
development:
  SECRET_KEY: <your-secret-key>
```

Install the dependencies
```
poetry install
```

Run the migratrions.
```
poetry run python manage.py migrate
```

Run the  tests.
```
poetry run pytest -vv
```

Build static files
```
cd search/static/search/bootstrap-5.0.2 & npm install & npm run dist
```

Load the information into the database.
```
poetry run python manage.py migrate
```

Start the application in development mode
```
poetry run python manage.py run server
```

Have fun!!!