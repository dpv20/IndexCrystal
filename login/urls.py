# login/urls.py

from django.urls import path
from . import views
from .views import root_page
from .views import upload_profile_picture

urlpatterns = [
    path('', views.root_page, name='root'),
    path('root/', root_page, name='root_page'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
]
