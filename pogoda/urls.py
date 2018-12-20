from django.urls import path
from . import views
app_name = 'pogoda'
urlpatterns = [
    path('', views.index, name="index"),
]