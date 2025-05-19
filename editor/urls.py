from django.urls import path
from . import views

urlpatterns = [
    path('execute/', views.run_code, name='run_code'),
]