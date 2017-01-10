from django.contrib.auth.models import User, Group
from data.models import Book
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        permission_classes = [IsAuthenticatedOrReadOnly]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('author', 'title')