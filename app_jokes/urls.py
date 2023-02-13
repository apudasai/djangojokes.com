from django.urls import path
from .views import JokeListView

app_name = 'app_jokes'
urlpatterns = [
    path('jokes/', JokeListView.as_view(), name = 'list'),
]