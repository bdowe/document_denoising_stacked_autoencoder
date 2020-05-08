help:
	@cat Makefile

IMAGE_NAME=tensorflow
IMAGE_TAG=document-denoising-stacked-autoencoder
DATA?=$(shell dirname `pwd`)
GPU?=0
DOCKER_FILE=Dockerfile
DOCKER=GPU=$(GPU) nvidia-docker
BACKEND=tensorflow
PYTHON_VERSION?=3.6
CUDA_VERSION?=9.0
CUDNN_VERSION?=7
SRC?=$(shell dirname `pwd`)

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

bash: build
	xhost + && $(DOCKER) run -it -ti --net=host --ipc=host -v $(SRC):/src/workspace -v $(DATA):/data -e DISPLAY=$(DISPLAY) -v /tmp/.X11-unix:/tmp/.X11-unix --env="QT_X11_NO_MITSHM=1" --env KERAS_BACKEND=$(BACKEND) $(IMAGE_NAME):$(IMAGE_TAG) bash

notebook: build
	$(DOCKER) run --gpus all -it -v $(SRC):/src/workspace -v $(DATA):/data --net=host --env KERAS_BACKEND=$(BACKEND) $(IMAGE_NAME):$(IMAGE_TAG)