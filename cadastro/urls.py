from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home, cadastrovisitas, catalogacao, agendadas

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('cadastrovisitas/', cadastrovisitas.as_view(), name='cadastro'),
    path('catalogacao/', catalogacao.as_view(), name='catalogacao'),
    path('catalogacao/formpeca/', views.formpeca, name='formpeca'),
    path('catalogacao/catalogadas/', views.catalogadas, name='catalogadas'),
    path('cadastrovisitas/form/', views.form, name='form'),
    path('formescola/', views.formescola, name='formescola'),
    path('createescola/', views.createescola, name='createescola'),
    path('createpeca/', views.createpeca, name='createpeca'),
    path('formfuncionario/', views.formfuncionario, name='formfuncionario'),
    path('createfuncionario/', views.createfuncionario, name='createfuncionario'),
    path('cadastrovisitas/agendadas/', views.agendadas, name='agendada'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view, name='view'),
    path('viewpeca/<int:pk>/', views.viewpeca, name='viewpeca'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('editpeca/<int:pk>/', views.editpeca, name='editpeca'),
    path('update/<int:pk>/', views.update, name='update'),
    path('updatepeca/<int:pk>/', views.updatepeca, name='updatepeca'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('deletepeca/<int:pk>/', views.deletepeca, name='deletepeca'),
]