from django.urls import path
from bank import views

app_name='bank'
urlpatterns=[
    path('',views.index),
    path('login/',views.login, name='login')
]