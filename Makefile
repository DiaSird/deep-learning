default: run

# ------------------------------------------------------------------------------------------------------
# Docker
dk-comp:
		docker-compose -f ./docker/docker-compose.yml up -d --build

# Note that using all your memory:
# https://skeptric.com/vmemm-using-all-ram/
dk-run:
		docker run --name deep-learning-dev -it -v $(pwd):/home/user/code deeplearning:latest

dk-enter:
		docker exec -i -t deep-learning-dev bash

dk-enter-id:
		docker exec -i -t dd956be355f3 bash

# remove all docker container.
dk-cntn-rm:
		docker rm -f $(docker container ls -q)

# ------------------------------------------------------------------------------------------------------

run:
		python3 -m poetry run python ./src/run.py

run-simpl:
		python3 -m poetry run python ./src/simpl_pcept.py

run-neu3:
		python3 -m poetry run python ./src/neural3.py

run-sigm:
		python3 -m poetry run python ./src/stepsig.py

run-mnist:
		# poetry run python ./src/utils/MNIST/set_mnist.py
		python3 -m poetry run python ./src/utils/MNIST/neural_mnist.py

install-dev:
		python3 -m poetry install

install:
		python3 -m poetry install --no-interaction


lint:
    # stop the build if there are Python syntax errors or undefined names
		python3 -m poetry run flake8 ./src ./tests --count --select=E9,F63,F7,F82 --show-source --statistics
    # exit-zero treats all errors as warnings. The width of the GitHub editor is 127 characters.
		python3 -m poetry run flake8 ./src ./tests  --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics

test:
		python3 -m poetry run python -m unittest

clean:
		rm -rf  **/__pycache__ **/**/__pycache__


.PHONY: clean test
