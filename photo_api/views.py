from rest_framework import generics, permissions, response

from .models import Photo
from .serializers import (DetailPhotoSerializer, ListPhotoSerializer,
                          SavePhotoSerializer)


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
