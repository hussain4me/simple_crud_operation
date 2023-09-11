from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(request):
    return Response("You re well, thanks")

def get_person(request):
    pass

def add_person(request):
    pass

def update_person(request):
    pass

def delete_person(request):
    pass
