from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
]

handler404 = "cadastro.views.handler404"
handler500 = "cadastro.views.handler500"
