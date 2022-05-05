from django.contrib import admin
from django.urls import path, include

from petclub.views import HelloWorld

from petclub.views import (
    HelloWorld,
    PetListAPIView,
)


urlpatterns = [
    path('hi', HelloWorld.as_view(), name="helloworld"),
    path('api-auth/', include('rest_framework.urls')),
    path('pets/', PetListAPIView.as_view(), name="all-pets"),
]


