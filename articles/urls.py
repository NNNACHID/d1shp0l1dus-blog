from django.urls import path
from articles.views import *

app_name = "articles"

urlpatterns = [
    path("", article_list, name="index"),
]