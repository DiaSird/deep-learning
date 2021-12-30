# Deep Learning used Python template

## Table of Contents

<!-- TOC depthFrom:2 -->

- [Deep Learning used Python template](#deep-learning-used-python-template)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Make usage](#make-usage)

<!-- /TOC -->

## Requirements

- python 3.8 &lt; 3.10
- poetry(package maneger):

If you do not have `poetry` installed, you can install it with the following command.

```shell
pip install poetry
```

if you use Anaconda3

```shell
conda install -c conda-forge poetry
```

More info is [here.](https://raw.githubusercontent.com/python-poetry/poetry/master/install)

## Make usage

| Command          |              Description               |
| :--------------- | :------------------------------------: |
| `make run`       | Run python file(default: `src/run.py`) |
| `make run-simpl` | Run python file(`src/simple_percept.py`) |
| `make run-sigm`  | Run python file(`src/stepsig.py`) |
| `make install`   |    Install dependencies (by poetry)    |
| `make test`      |            Test with pytest            |
| `make lint`      |            Lint with flake8            |
| `make clean`     |       Remove `__pycache__` files       |

If you are using windows, you can install the `make` command [here](http://gnuwin32.sourceforge.net/packages/make.htm).
(Click the `Setup` button at the top.)
