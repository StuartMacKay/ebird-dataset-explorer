# eBird Dataset Explorer

eBird Dataset Explorer is a Django-based web site for browsing observations
from the eBird Basic Dataset v1.16.

## Overview

The Cornell Laboratory of Ornithology in Ithaca, New York runs the eBird database
which collects observations of birds from all over the world, and publishes them
on (eBird.org)[https://ebird.org]. The data is also available via the
[eBird Basic Dataset](https://science.ebird.org/en/use-ebird-data/download-ebird-data-products)
which is intended for for analysis and modelling.

This project contains Django-based web site for browsing observations from the
eBird Basic Data. This project uses the [ebird-dataset-data](https://git.sr.ht/~smackay/ebird-dataset-data)
which allows you to load the CSV based files published by eBird and load them
into a database.

## Getting Started

To get started, you will need to [sign up](https://secure.birds.cornell.edu/identity/account/create) for an eBird account,
then [request access](https://ebird.org/data/download), which usually takes 7 days to be reviewed and approved.

Next, get a copy of the repository:

```shell
git clone https://git.sr.ht/~smackay/ebird-dataset-explorer
cd ebird-dataset-explorer
```

Create the virtual environment:

```shell
uv venv
```

Activate it:

```shell
source .venv/bin/activate
```

Install the requirements:

```shell
uv sync
```

Create a copy of the .env.example file and set the URL to access the database:

    cp .env.example .env

For example:

```shell
DATABASE_URL=postgres://dataset:passwordd@localhost:5432/dataset
```

The site is developed and tested with PostgreSQL.

Run the database migrations:

    python manage.py migrate

Create an admin user:

    python manage.py createsuperuser

There is a copy of the sample file from the eBird Basic Dataset in the
/data/datasets/ directory. Use the load_dataset management command to
load it into the database:

```shell
python manage.py load_dataset data/datasets/ebd.csv
```

It's time to start the server:

    python manage.py runserver

Finally, visit the home page to view the observations:

    http://localhost:8000/

## Project Information

* Issues: https://todo.sr.ht/~smackay/ebird-dataset-explorer
* Repository: https://git.sr.ht/~smackay/ebird-dataset-explorer
* Announcements: https://lists.sr.ht/~smackay/ebirders-announce
* Discussions: https://lists.sr.ht/~smackay/ebirders-discuss
* Development: https://lists.sr.ht/~smackay/ebirders-develop

The repository is also mirrored on Github:

* Repository: https://github.com/StuartMacKay/ebird-dataset-explorer

# License

eBird Dataset Browser is released under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
