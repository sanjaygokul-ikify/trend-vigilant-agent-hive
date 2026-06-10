build: export RUSTFLAGS = -Ctarget-cpu=native
build:
	rust build --release
	python setup.py build_ext --inplace
	docker-compose up -d

lint:
	rust clippy
	pylint --rcfile=.pylintrc
	docker images prune

ci: build lint test
docker:
	docker build -t vigilant-agent-hive .

dist: export RUSTFLAGS =
dist:
	rust build --target wasm32-unknown-unknown

format:
	rust fmt
	poetry run black .

