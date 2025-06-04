from django.contrib import admin
from django.urls import path, include
from .views import Main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='home'),
    path('inventory/', include('content.urls')),
]
