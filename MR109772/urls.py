from django.conf.urls import include, url
from django.contrib import admin
from store import views as store
from data import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'MR109772.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.note, name='note'),
    url(r'^shoes', views.shoe, name='shoe'),
    url(r'^api/', include(router.urls)),
    #url(r'store/', store.store, name='store'),
    #url(r'store/', data.store, name='store'),
    #url(r'data/', data.data, name='data'),
    #url(r'page/', data.page, name='page'),
    #url(r'myname/', data.myname, name='myname'),
    url(r'books/', views.books, name='books'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework'))

]
