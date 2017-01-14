from django.conf.urls import include, url
from django.contrib import admin
from data import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.note, name='note'),
    url(r'^shoes', views.shoe, name='shoe'),
    url(r'^shoe/(?P<id>[0-9]+)$', views.pickedShoe, name='pickedShoe'),
    url(r'^cart', views.get_cart, name='cart'),
    url(r'^products/buy/(?P<product_id>[0-9]+)/(?P<quantity>[0-9]+)$', views.add_to_cart, name = 'add_to_cart'),
    url(r'^products/remove/(?P<product_name>[^/]+)/(?P<selectedSize>[^/]+)$',
        views.remove_from_cart, name = 'remove_from_cart'),
    url(r'^pay', views.pay, name='pay'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^pleaseLogIn', views.pleaseLogIn, name='pleaseLogIn'),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)