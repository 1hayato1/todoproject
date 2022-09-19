from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('todo/', views.ListtodoView.as_view(), name='list-todo'),
    path('todo/create/', views.CreatetodoView.as_view(), name='create-todo'),
    path('todo/<int:pk>/delete/', views.DeletetodoView.as_view(), name='delete-todo'),
    path('todo/<int:pk>/update/', views.UpdatetodoView.as_view(), name='update-todo'),
]