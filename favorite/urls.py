from django.urls import path

from . import views

app_name = 'favorite'
urlpatterns = [
    path('favorites/', views.favorites, name='favorites'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('del_favorite/', views.del_favorite, name='del_favorite'),
]