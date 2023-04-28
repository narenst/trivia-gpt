# Trivia GPT

This is a prototype full stack application designed to demonstrate the best practices. As a demo, this app serves trivia questions created by ChatGPT with increasing difficulty.

## Code organization

### backend 

The backend is a python flask application. The code is organized into:

- models
- controllers
- services
- tests

### Frontend

This is a react application that renders the trivia questions.

### Local Dev

This has the docker-compose file required to setup `postgres` and `redis` needed to develop and test the application.

### Deploy

This is the terraform configuration for deploying the application into a `staging` and `production` env.

## Datastore

The app uses `postgres` to store the user and quiz models. TODO: Cache ChatGPT response using `Redis`.

## Configuration

The app is configured using [Dynaconf](https://www.dynaconf.com/flask/). The default settings are present in `backend/settings.toml`. These configuration params will be overridden using environment variables in staging and production.

## Testing

Tests can be run with `pytest`. TODO: Add coverage report.