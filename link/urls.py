from django.urls import path, include
from .views import home, create_link, delete_link, delete, update, update_link

urlpatterns = [
    path('', home ,name='home'),    
    path('create_link/', create_link, name='create_link'),
    path('delete_link/<int:pk>/', delete_link, name='delete_link'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update'),
    path('update_link/<int:pk>/', update_link, name='update_link'),
]