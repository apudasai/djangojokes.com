from django.urls import path

from .views import HomePageView, AboutUsView

app_name = 'app_djangojokes'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'homepage'),
    path('about-us/', AboutUsView.as_view(), name = 'about-us'),
]