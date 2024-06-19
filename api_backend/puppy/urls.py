from django.urls import path
from puppy import views

urlpatterns = [
    path('index_puppies', views.index, name='index_puppies'),
    path('puppies_rest/', views.puppies_rest, name='puppies_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    # path('add_puppy/', views.add_puppy_view, name='add_puppy'),
    path('new_puppy/', views.NewPuppyView.as_view(), name='new_puppy'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]