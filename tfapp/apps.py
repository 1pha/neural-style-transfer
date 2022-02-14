from django.apps import AppConfig
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import PIL.Image


def image2tensor(img):
    max_dim = 512
    img = tf.keras.utils.img_to_array(img)
    img = tf.convert_to_tensor(img, dtype=tf.float32) / 255.0

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


def tensor2image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)


class TfappConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tfapp'
    model = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1")
