from django.apps import AppConfig
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import PIL.Image


def image2tensor(image):

    np_image = tf.keras.utils.img_to_array(image)
    tf_image = tf.convert_to_tensor(np_image, dtype=tf.float32)

    shape = tf.cast(tf_image.shape[:-1], tf.float32)
    max_dim = 512
    long_dim = max(shape)
    scale = max_dim / long_dim
    new_shape = tf.cast(shape * scale, tf.int32)

    resized_image = tf.image.resize(tf_image, new_shape) / 255.
    expanded_image = resized_image[tf.newaxis, :]
    return expanded_image


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
    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')
