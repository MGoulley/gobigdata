from django.urls import re_path, path
from django.contrib.auth.decorators import login_required

from . import views
from .views import *


urlpatterns = [
    path("", views.index, name="home"),
]
