import re

from rest_framework import serializers

from .models import Photo


class SavePhotoSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not re.match(r'([12][09][0-9][0-9])\-(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01])',
                        data['date'].strftime('%Y-%m-%d')):
            raise serializers.ValidationError({'Дата': 'Неправильный формат даты!'})
        if not re.search(r'^[\-\+]?(0(\.\d{1,10})?|([1-9](\d)?)(\.\d{1,10})?|1[0-7]\d{1}(\.\d{1,10})?|180\.0{1,10})$',
                         str(data['longitude'])):
            raise serializers.ValidationError({'Долгота': 'Неправильный формат долготы!'})
        if not re.match(r'^[\-\+]?((0|([1-8]\d?))(\.\d{1,10})?|90(\.0{1,10})?)$', str(data['latitude'])):
            raise serializers.ValidationError({'Широта': 'Неправильный формат широты!'})
        return data

    class Meta:
        model = Photo
        fields = ['image', 'latitude', 'longitude', 'description', 'date', 'people', ]


class ListPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['image', ]


class DetailPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['image', 'latitude', 'longitude', 'description', 'date', 'people', ]
