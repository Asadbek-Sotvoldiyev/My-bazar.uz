from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('category/<int:id>', views.category_detail, name='category'),
    path('season/<int:id>', views.season_detail, name='season'),
]