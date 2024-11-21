from django.contrib import admin
from django.urls import path
from welcome import views
from .views import *

from welcome.views import index, users_api, user_api, items_api, item_api, check, upload_file, questions_and_answers_api

app_name = 'welcome'


urlpatterns = [
    path('', index),
    path('api/users/', users_api),
    path('api/user/<int:id>/', user_api),
     # register page
    path('register/', views.register_view, name='register'),
    # login page
    path('login/', views.login_view, name='login'),
    # logout page
    path('logout/', views.logout_view, name='logout'),
    path("items/", items_api),
    path("item/<int:item_id>/", item_api),
    path('questions/', questions_and_answers_api),
    path("check/", check),
    path('file/', upload_file),
    path(r'^.*', index, name='vue index')
]
