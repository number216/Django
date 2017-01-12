from django.shortcuts import render
from data.models import Book, Shoe, Note, Size

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, BookSerializer

from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['test@test.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
            #return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')

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

def shoe(request):
    context = {
        'ShoeCount' : Shoe.objects.count,
        'shoes' : Shoe.objects.all()}
    return render(request, 'shoe.html', context)

def pickedShoe(request, id):
    context = {
        'shoe' : Shoe.objects.get(pk = id),
        'sizes' : Size.objects.all().filter(shoeID = id)}
    return render(request, 'pickedShoe.html', context)

def note(request):
    context = {
        'NoteCount' : Note.objects.count,
        'notes' : Note.objects.all().order_by('-publish_date')}
    return render(request, 'note.html', context)

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