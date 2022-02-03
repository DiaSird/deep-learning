FROM python:3.8.10

# hadolint ignore=DL3008,DL3059,DL3015
RUN apt-get update && \
    apt-get install -y curl git make sudo && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# hadolint ignore=DL3008
RUN adduser --disabled-password --gecos '' user && \
    echo 'user ALL=(root) NOPASSWD:ALL' >/etc/sudoers.d/user
USER user
WORKDIR /home/user/code

# hadolint ignore=DL3013,DL3008
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade setuptools

ADD http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz ./MNIST-datasets
ADD http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz ./MNIST-datasets
ADD http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz ./MNIST-datasets
ADD http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz  ./MNIST-datasets


SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -