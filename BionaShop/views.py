from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """

    :param request:
    :return: rendering template of home from template folder
    """
    return HttpResponse("home page")


def about(request):
    """

    :param request:
    :return: rendering template of about us from template folder
    """
    return HttpResponse("about page")
