FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

MAINTAINER Richard Chen <richard.chen.1989@gmail.com>

RUN apt-get -y update && apt-get install -y --no-install-recommends \
        wget \
        nginx \
        ca-certificates \
        libsm6 \
        libxext6 \
        libxrender-dev \
        bzip2 \
        g++ \
        git \
        graphviz \
        libgl1-mesa-glx \
        libhdf5-dev \
        openmpi-bin \
        tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Install all of the packages
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install Pillow
RUN pip install opencv-python
RUN pip install jupyter
RUN pip install -U pip setuptools
RUN pip install --upgrade scikit-image
RUN pip install imutils
RUN pip install matplotlib
RUN pip install pytesseract
RUN rm -rf /root/.cache

# Env Variables
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

WORKDIR /data

EXPOSE 8888

CMD jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root

