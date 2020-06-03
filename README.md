# Stacked CNN for Document Denoising

This project implements a stacked convolutional neural network to denoise "dirty" documents. Given a document that is "noisy" (wrinkles, shadows, coffee stains, etc), the network reconstructs a clean version of the document without noise, which can then be used more efficiently as input for various OCR applications. 

## Background

### References
* The model architecture used in this repository is inspired by this [article](https://medium.com/illuin/cleaning-up-dirty-scanned-documents-with-deep-learning-2e8e6de6cfa6). 
* The dataset used for model training and inference is the [document denoising dataset on kaggle](https://www.kaggle.com/c/denoising-dirty-documents/overview)

## Getting Started

### Installation
To install required packages locally, navigate to the root directory of this repository after cloning it and run the following in your terminal:
```
pip install -r requirements.txt
```

### Running with Docker
You can also run this repository from within a container using [docker](https://www.docker.com/). The docker commands needed are implemented in the provided `Makefile`. To build the docker image, run the following:
```
make build
```

