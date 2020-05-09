import numpy as np
import cv2
from tensorflow.keras.preprocessing import image

class ImageLoader():
    @staticmethod
    def load_image(path, img_w, img_h):
        image_list = np.zeros((len(path), img_w, img_h, 1))
        for i, fig in enumerate(path):
            img = image.load_img(fig, color_mode='grayscale', target_size=(img_w, img_h))
            x = image.img_to_array(img).astype('float32')
            x = x / 255.0
            image_list[i] = x

        return image_list

    @staticmethod
    def load_image_blur(path, img_w, img_h):
        image_list = np.zeros((len(path), img_w, img_h, 1))
        for i, fig in enumerate(path):
            img = image.load_img(fig, color_mode='grayscale', target_size=(img_w, img_h))
            x = image.img_to_array(img).astype('float32')
            x = x / 255.0
            x = cv2.medianBlur(x, 3)
            x = np.expand_dims(x, axis=-1)
            image_list[i] = x

        return image_list

    @staticmethod
    def load_image_canny_dilate_erode(path, img_w, img_h):
        image_list = np.zeros((len(path), img_w, img_h, 1))
        for i, fig in enumerate(path):
            img = cv2.imread(fig)
            edges = cv2.Canny(img,100,200)
            kernel = np.ones((5,5), np.uint8) # Taking a matrix of size 5 as the kernel 
            img_dilation = cv2.dilate(edges, kernel, iterations=1) 
            img_erosion = cv2.erode(img_dilation, kernel, iterations=1) 
            x = image.img_to_array(img_erosion).astype('float32')
            x = x / 255.0
            x = cv2.resize(x, (img_w, img_h))
            x = np.expand_dims(x, axis=-1)
            image_list[i] = x

        return image_list
    
    @staticmethod
    def load_image_threshold(path, img_w, img_h, threshold='adaptive_gaussian'):
        image_list = np.zeros((len(path), img_w, img_h, 1))
        for i, fig in enumerate(path):
            img = cv2.imread(fig)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if threshold == 'binary':
                ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            elif threshold == 'adaptive_mean':
                th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,65,2)
            else:
                th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,105,2)
            x = image.img_to_array(th).astype('float32')
            x = x / 255.0
            x = cv2.resize(x, (img_w, img_h))
            x = np.expand_dims(x, axis=-1)
            image_list[i] = x

        return image_list
    