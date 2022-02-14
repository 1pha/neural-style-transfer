from django.shortcuts import render
from .apps import TfappConfig


def main(request):

    return render(request, "index.html")


def transfer(request):
    # print(request.)
    return render(request, "index.html")
