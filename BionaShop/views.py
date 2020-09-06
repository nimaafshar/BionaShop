from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """

    :param request:
    :return: rendering template of home from template folder
    """
    return render(request, "shop/index.html")


def about(request):
    """

    :param request:
    :return: rendering template of about us from template folder
    """
    return render(request, "shop/about.html")


def frequently_asked_questions(request):
    """

        :param request:
        :return: rendering template of FQQ from template folder
        """
    return render(request,"shop/about.html")

