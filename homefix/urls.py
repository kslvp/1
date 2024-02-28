
from django.contrib import admin
from django.urls import path, include
from authentication import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
]
