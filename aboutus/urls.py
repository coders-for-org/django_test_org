from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='kopu'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('display/', views.display),
    path('emp/', views.emp),
    path('emp-show/', views.emp_show),
    path('emp-edit/<int:id>', views.emp_edit),  
    path('emp-update/<int:id>', views.emp_update),  
    path('emp-delete/<int:id>', views.emp_destroy),
    path('lyrics/', views.lyrics),
    path('lyrics-show/', views.lyrics_show),
    path('lyrics-edit/<int:id>', views.lyrics_edit),
    path('lyrics-update/<int:id>', views.lyrics_update),
    path('lyrics-delete/<int:id>', views.lyrics_destroy),
]