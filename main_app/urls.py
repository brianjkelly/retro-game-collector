from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.GameList.as_view(), name='index'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('accessorys/', views.AccessoryList.as_view(), name='accessorys_index'),
    path('accessorys/<int:pk>/', views.AccessoryDetail.as_view(), name='accessorys_detail'),
    path('accessorys/create/', views.AccessoryCreate.as_view(), name='accessorys_create'),
    path('accessorys/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessorys_update'),
    path('accessorys/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessorys_delete'),
]