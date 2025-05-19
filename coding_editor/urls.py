from django.urls import path, include

urlpatterns = [
    path('editor/', include('editor.urls')),
]