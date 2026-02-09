"""
URL configuration for core project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    path("api/users/", include("users.urls")),
    path("api/users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/tasks/', include('tasks.urls')),
]
