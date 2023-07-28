from django.urls import path
from profiles import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
]
