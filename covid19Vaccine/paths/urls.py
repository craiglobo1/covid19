from django.urls import path
from . import views

urlpatterns = [
    path('',views.path,name='paths-path' ),
]