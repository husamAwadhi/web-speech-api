env ?= dev
export

setup-env:
ifeq (,$(wildcard ./frontend/.env))
	cp frontend/.env.$(env) frontend/.env
endif
up: setup-env
	docker compose -f docker/$(env).yml up --build -d
down:
	docker compose -f docker/$(env).yml down
test:
	docker compose -f docker/$(env).yml run --rm --no-deps python \
		bash -c "cd /home/app/web && python -m pytest --cov-report term-missing --cov=webspeech tests/"
lint:
	docker compose -f docker/$(env).yml run --rm --no-deps python \
		bash -c "cd /home/app/web && flake8 --config=.flake8"
