from django.apps import AppConfig
# import tensorflow_hub as hub


class TfappConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tfapp'
    # model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')

    def transfer(self, content, style):
        stylized_image = self.model(content, style)
        return stylized_image
