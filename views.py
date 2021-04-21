from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('HELLO ZURI BOARD THIS IS MY FIRST APP AND IT IS ALSO MY PROJECT THE USERNAME TO THE ADMIN IS zuriboard, PASSWORD;zuriboard123 AND EMAIL; ezeobisunny51@gmail.com. THANKS')

