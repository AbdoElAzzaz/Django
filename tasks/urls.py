from django.urls import path

from . import views

urlpatterns = [
    path('', views.tasks_index, name='tasks_index'),
    path('logout/', views.logout, name='logout'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('done/<int:id>/',views.done,name="done"),
]