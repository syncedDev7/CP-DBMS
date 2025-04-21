from django.urls import path
from . import views

urlpatterns = [
    path('', views.Train_list, name='train_list'),
    path('train/book/<int:train_id>/', views.Booked_Train_ticket, name='book_ticket'),
    path('register/', views.register,name = 'register')
]