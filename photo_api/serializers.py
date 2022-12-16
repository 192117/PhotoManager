import re

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import Photo, User


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


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"Пароль": "Пароли не совпадают!"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
