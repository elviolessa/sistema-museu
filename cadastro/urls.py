from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home, cadastrovisitas, cataloga, agendadas

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrovisitas/', cadastrovisitas.as_view(), name='cadastro'),
    path('cataloga/', cataloga.as_view(), name='catalogação'),
    path('cadastrovisitas/form/', views.form, name='form'),
    path('formescola/', views.formescola, name='formescola'),
    path('createescola/', views.createescola, name='createescola'),
    path('formfuncionario/', views.formfuncionario, name='formfuncionario'),
    path('createfuncionario/', views.createfuncionario, name='createfuncionario'),
    path('cadastrovisitas/agendadas/', views.agendadas, name='agendada'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]