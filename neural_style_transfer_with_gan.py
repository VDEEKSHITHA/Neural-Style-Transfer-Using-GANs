# -*- coding: utf-8 -*-
"""Neural Style Transfer with GAN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15sLvtD8im1qXKXCeL95otDx4exGKeHo8
"""

# IMPORT THE LIBRARIES
import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

# PREPROCESS THE IMAGE
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

# LOAD THE CONTENT & STYLE IMAGES
content_image = load_image('frida.jpeg')
style_image = load_image('monet.jpeg')

# VISUALIZATION OF IMAGES
plt.imshow(np.squeeze(style_image))
plt.show()
plt.imshow(np.squeeze(content_image))
plt.show()

# MERGE THE CONTENT & STYLE IMAGES
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
plt.imshow(np.squeeze(stylized_image))
plt.show()
cv2.imwrite('generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))