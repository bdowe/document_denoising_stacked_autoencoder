# Stacked CNN for Document Denoising

This project implements a stacked convolutional neural network to denoise "dirty" documents. Given a document that is "noisy" (wrinkles, shadows, coffee stains, etc), the network reconstructs a clean version of the document without noise, which can then be used more efficiently as input for various OCR applications. 

## Background

### References
* The model architecture used in this repository is inspired by this [article](https://medium.com/illuin/cleaning-up-dirty-scanned-documents-with-deep-learning-2e8e6de6cfa6). 
* The [dataset](https://www.kaggle.com/c/denoising-dirty-documents/overview) used for model training and inference is the document denoising dataset on kaggle.

## Getting Started

### Installation
To install required packages locally, navigate to the root directory of this repository after cloning it and run the following in your terminal:
```
pip install -r requirements.txt
```

### Running with Docker
Alternatively, you can also run this repository from within a [docker](https://www.docker.com/) container. The docker commands needed are implemented in the provided `Makefile`. To build the docker image, run the following:
```
make build
```
To run the container and start a jupyter notebook server locally, run the following command. A link to the notebook server will be provided as output in the command line.

```
make notebook
```

To open a bash shell from within the container after starting it up, run the following command:
```
make bash
```

### Running with Docker (GPU Enabled)
To run as a docker container with GPU training enabled (assuming you have access to a machine with a Nvidia GPU), add `GPU=1` to either of the previous 2 commands for running the docker container. Note: You must have [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed on your local machine, as well as the latest version of [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads). For example, to start the container and run a jupyter notebook server with gpu training enabled, run the following command:
```
make notebook GPU=1
```