from django.shortcuts import render
from data.models import Book

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, BookSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def page(request):
    return render(request, 'page.html')

def data(request):
    context = {
        'BookCount' : Book.objects.count,
        'books' : Book.objects.all()}
    return render(request, 'data.html', context)

def myname(request):
    context = {
        'imie' : 'Mateusz',
        'nazwisko' : 'Rutkowski',
        'indeks' : '109772'
    }
    return render(request, 'myname.html', context)

def store(request):
    return  render(request, 'index.html')

def books(request):
    context = {
        'BookCount' : Book.objects.count,
        'books' : Book.objects.all()}
    return render(request, 'books.html', context)