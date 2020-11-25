# ✉️ 🐍 Telegraph 🐍 ✉️

An open-source Python chatting engine written with FastAPI and Tortoise ORM in order to use as much `asyncio` as possible! 🐍

## Technologies

- `Python 3.9`;
- `Asyncio`;
- `FastAPI`;
- `Tortoise ORM`;
- `Pydantic`;
- `Aerich` (migrations);
- `Pytest`

## Running locally

```bash
# start the database
docker-compose up -d db

# run locally
pipenv run start:local
```

## Running locally: debugging

If local debugging is desired, run the following command with your IDE/Text editor debugger:

```bash
# start the database
docker-compose up -d db

# run all migrations
pipenv run migrate

# start the python process which will be debugged by your IDE's debugger API
python main.py
```

## Running Remotely: docker

The easiest way to run:

```bash
docker-compose up app
```

In order to debug, use a docker remote interpreter (Pycharm) or create a `process picker (attach to process)` with your text editor such as `VSCode`.

## Migrations

This project uses `aerich` which is standard migration tool which goes along with `Tortoise ORM`.

To create the very first migration, make sure `src/migrations/models` **does not exist**. The `models` folder (aerich app named `models`) cannot exist or it won't run the first migration:

```bash
pipenv run migrate:init
```

To run migrations:

```bash
pipenv run migrate
```

The following commands automatically run migrations first:

```bash
pipenv run start:local  # ./scripts/start-local.sh
pipenv run start:docker  # ./scripts/start-docker.sh
```

## Testing: locally

Just run:

```bash
pipenv run start:tests
```

Which will start a pytest debugging section.

## Testing: remotely

Just run:

```bash
docker-compose up tests
```
