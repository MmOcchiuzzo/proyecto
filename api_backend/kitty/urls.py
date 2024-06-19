from django.urls import path
from kitty import views

urlpatterns = [
    path('index_kitties', views.index, name='index_kitties'),
    path('kitties_rest/', views.kitties_rest, name='kitties_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    # path('add_kitty/', views.add_kitty_view, name='add_kitty'),
    path('new_kitty/', views.NewKittyView.as_view(), name='new_kitty'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]