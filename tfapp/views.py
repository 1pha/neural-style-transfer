from django.shortcuts import render
# from .apps import TfappConfig
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
    # print(request.)

    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    source_image = image_converter(body['source_image'])
    style_image = image_converter(body['style_image'])

    print(source_image, style_image)
    


    #여기서 새로운 이미지 생성
    #일단 임시로 source
    gan_image = source_image


    #다시 base64로
    buffered = BytesIO()
    gan_image.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    data = {
        "new_image": "data:image/jpeg;base64,"+img_str
    }


    return JsonResponse(data)
    

def image_converter(image):
    image = image.split(",")[1]
    image = base64.b64decode(image)
    image = io.BytesIO(image)
    image = Image.open(image)
    return image

