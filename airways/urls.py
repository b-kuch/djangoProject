from django.urls import path

from .views import *
app_name = 'airways'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('<str:cls>/create/', create, name='Create'),
    path('<str:cls>/read/', read, name='Read'),
    path('<str:cls>/update/<int:id>/', update, name='Update'),
    path('<str:cls>/delete/<int:id>', delete, name='Delete')
]