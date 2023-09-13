from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import UserProfileSerilier
from rest_framework import status


 
@api_view(['GET','POST'])
def add_person(request):
    queryset = Person.objects.all().order_by('-id')
    if request.method == 'GET':
        serializer = UserProfileSerilier(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserProfileSerilier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = UserProfileSerilier(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def update_delete_person(request, pk):

    person = get_object_or_404(Person,id=pk)
    if request.method == 'GET':
        serializer = UserProfileSerilier(person)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserProfileSerilier(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

