# Stacked CNN for Document Denoising

This project implements a stacked convolutional neural network to denoise "dirty" documents. Given a document that is "noisy" (wrinkles, shadows, coffee stains, etc), the network reconstructs a clean version of the document without noise, which can then be used more efficiently as input for various OCR applications. 

## Background

### References
* The model architecture used in this repository is inspired by this [article](https://medium.com/illuin/cleaning-up-dirty-scanned-documents-with-deep-learning-2e8e6de6cfa6). 
* The dataset used for model training and inference is the [document denoising dataset on kaggle](https://www.kaggle.com/c/denoising-dirty-documents/overview)
