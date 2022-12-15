from datetime import datetime

from django.urls import path, register_converter

from .views import DetailPhotoView, ListPhotoView, SavePhotoView


class DateConverter:

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return value


register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('save_photo/', SavePhotoView.as_view()),
    path('detail_photo/<int:pk>/', DetailPhotoView.as_view()),
    path('show/', ListPhotoView.as_view()),
    path('show/<yyyy:date>/', ListPhotoView.as_view()),
    path('show/<str:people>/', ListPhotoView.as_view()),
    path('show/<str:latitude>/<str:longitude>/', ListPhotoView.as_view()),
]
