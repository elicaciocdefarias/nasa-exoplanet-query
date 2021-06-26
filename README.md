
# Nasa Exoplanet Query

## Objective
Allown informations about exoplanets to be searched easily  and beautifully.

## Screenshots
![landpage](https://user-images.githubusercontent.com/15112609/122652816-4068e000-d117-11eb-97a9-e97cdc639bdb.png)

![Screenshot from 2021-06-26 14-34-51](https://user-images.githubusercontent.com/15112609/123521262-f1c5c380-d68b-11eb-8dc9-a29db5c06ffe.png)

## How to use

Clone the projeto.
```
git clone https://github.com/elicaciocdefarias/nasa-exoplanet-query.git
```

Access project, 
```
cd nasa-exoplanet-query
```

open settings.yaml file and change value of the variables BASE_DIR and NAME.
see that *parent_dir have be full path where your project to be localized.
```
BASE_DIR: /<parent_dir>/nasa-exoplanet-query
DATABASES:
    default:
      ENGINE: django.db.backends.sqlite3
      NAME: /<parent_dir>/nasa-exoplanet-query/db.sqlite3
```

In the root project create .secrets.yaml and add bellow code.

```
---
development:
  SECRET_KEY: <your-secret-key>
```

Install dependencies
```
poetry install
```

Running migratrions
```
poetry run python manage.py migrate
```

Running tests
```
poetry run pytest -vv
```

Populate database
```
poetry run python manage.py migrate
```

Start app at development mode
```
poetry run python manage.py run server
```