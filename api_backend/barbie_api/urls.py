from django.urls import path
from barbie_api import views

urlpatterns = [
    path('index_barbies', views.index, name='index_barbies'),
    path('barbies_rest/', views.barbies_rest, name='barbies_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('add_barbie/', views.add_barbie_view, name='add_barbie'),
    path('new_barbie/', views.NewBarbieView.as_view(), name='new_barbie'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]