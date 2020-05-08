import numpy as np
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

    