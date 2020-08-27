from django.urls import path
from . import views

app_name = "cv"

urlpatterns = [
    path('', views.display_cv, name='display_cv'),
]