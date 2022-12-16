from rest_framework import generics, permissions, response
from rest_framework.decorators import api_view

from .models import Photo
from .serializers import (DetailPhotoSerializer, ListPhotoSerializer,
                          RegisterUserSerializer, SavePhotoSerializer)
from .utils import kmp


class SavePhotoView(generics.CreateAPIView):

    model = Photo
    serializer_class = SavePhotoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Photo.objects.all()


class ListPhotoView(generics.ListAPIView):

    model = Photo

    def get(self, request, *args, **kwargs):
        if 'latitude' and 'longitude' in kwargs:
            queryset = Photo.objects.filter(longitude__lte=kwargs['longitude']) & \
                       Photo.objects.filter(latitude__lte=kwargs['latitude'])
        elif 'date' in kwargs:
            queryset = Photo.objects.filter(date=kwargs['date'])
        elif 'people' in kwargs:
            queryset = Photo.objects.filter(people__contains=kwargs['people'])
        else:
            queryset = Photo.objects.all()
        serializer = ListPhotoSerializer(queryset, many=True)
        return response.Response(serializer.data)


class DetailPhotoView(generics.RetrieveAPIView):

    model = Photo
    serializer_class = DetailPhotoSerializer

    def get_queryset(self):
        return Photo.objects.all()


class RegisterUserView(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterUserSerializer


@api_view(['POST', 'GET'])
def search_name(request):
    try:
        people = Photo.objects.values_list('people', flat=True)

        if request.method == 'GET':
            name = request.query_params.get('name')
            names = set()
            for persons in people:
                for person in persons.split():
                    if kmp(name, person):
                        names.add(person)
        if request.method == 'POST':
            name = request.data.get('name')
            names = set()
            for persons in people:
                for person in persons.split():
                    if kmp(name, person):
                        names.add(person)
        return response.Response({f'{name}': names})
    except TypeError:
        return response.Response({'Ошибка': 'Нет имени для поиска'})
