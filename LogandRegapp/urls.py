from django.urls import path
from . import views

urlpatterns = [
    path('',views.Regin.as_view()),
    path('reg/',views.Registerview.as_view()),

]