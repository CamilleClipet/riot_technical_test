# Riot technical test

## Description

My submission for the [Riot technical test](https://github.com/tryriot/take-home).

## Prerequisites

Install [uv](https://docs.astral.sh/uv/#projects) with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Project setup

Clone this repo:

```bash
$ git@github.com:CamilleClipet/riot_technical_test.git
```

## Run the development server

```bash
# development mode
$ $ uv run -- flask run -p 3000

# watch mode
$ uv run -- flask run -p 3000 --debug --reload
```

## Test endpoints

You can test the endpoints in the terminal with [HTTPie](https://httpie.io/), an open-source API testing client.
At the root of the project, run:

```bash
$ http http://127.0.0.1:3000/encrypt
```

This should return the following:

```bash
HTTP/1.1 200 OK
Connection: close
Content-Length: 17
Content-Type: text/html; charset=utf-8
Date: Tue, 18 Mar 2025 17:05:31 GMT
Server: Werkzeug/3.1.3 Python/3.13.2

to be implemented
```

You can also use an API testing platform of your choice ([Postman](https://www.postman.com/downloads/), [Insomnia](https://insomnia.rest/)...)

## Run tests

```bash
# run unit tests
$ uv run -- pytest
```
