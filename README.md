# Web Speech API

Using the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) which provides two distinct areas of functionality — speech recognition, and speech synthesis (also known as text to speech, or tts) — which open up interesting new possibilities for accessibility, and control mechanisms.

## Tech Stack

- Python 3.12 ([Flask v3](https://flask.palletsprojects.com/en/3.0.x/) - API)
- Vue 3 ([Vite](https://vitejs.dev/) - Frontend)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/): local development

## Development

### Setup

In project root directory,

```sh
make up
```

### Access

- backend: http://localhost:80
- frontend: http://localhost:8000

## Tests

Run Backend tests,

```sh
make test
```
