from django.shortcuts import render
from .apps import TfappConfig, image2tensor, tensor2image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from PIL import Image
import base64
import io
from io import BytesIO


def main(request):

    return render(request, "index.html")


@csrf_exempt
def transfer(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content_image = image_converter(body['content_image'])
    style_image = image_converter(body['style_image'])

    content_tensor = image2tensor(content_image)
    style_tensor = image2tensor(style_image)

    gan_tensor = TfappConfig.model(content_tensor, style_tensor)[0]
    gan_image = tensor2image(gan_tensor)

    buffered = BytesIO()
    gan_image.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    data = {
        "new_image": "data:image/jpeg;base64," + img_str
    }
    return JsonResponse(data)
    

def image_converter(image):
    image = image.split(",")[1]
    image = base64.b64decode(image)
    image = io.BytesIO(image)
    image = Image.open(image)
    return image

