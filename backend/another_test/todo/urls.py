from django.urls import include
from django.conf.urls import url
from .views import TodoViewSet

urlpatterns = [
    url(r'^todo/$', TodoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]