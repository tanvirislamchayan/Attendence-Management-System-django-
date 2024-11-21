"""
URL configuration for AMS project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('t/', include('teachers.urls')),
    path('d/', include('departments.urls')),
    path('p/', include('probidhans.urls')),
    # path('s/', include('seassons.urls')),
    # path('sem/', include('semesters.urls')),
    # path('g/', include('groups.urls')),
    # path('sub/', include('subjects.urls')),
    # path('std/', include('students.urls')),
    # path('atd/', include('attendances.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
