"""fitnessplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from apps.pages.views import start_view
from apps.users.views import *
from apps.trainers.views import *

urlpatterns = [
    path('', start_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', user_profile, name='user_profile'),
    path('trainerlist/', get_trainer_list, name='trainer_list'),
    path('trainer/<int:id>/', get_trainer_profile, name='trainer_profile'),
    path('trainer/', get_trainer_profile, name='trainer_profile'),
    path('trainer/edit', edit_trainer_profile, name='trainer_profile_edit'),
    path(
        'trainer/upload/<int:id>/', delete_upload, name='delete_upload'
    ),
    path(
        'trainer/upload', upload_trainer_profile, name='trainer_profile_upload'
    ),
    path(
        'trainer/locations',
        edit_trainer_locations,
        name='trainer_profile_locations',
    ),
    path(
        'trainer/locations/<int:id>',
        edit_trainer_locations,
        name='trainer_profile_locations',
    ),
    path(
        'trainer/locations/<str:action>',
        edit_trainer_locations,
        name='trainer_profile_locations',
    ),
    path(
        'trainer/locations/delete/<int:id>/',
        delete_location,
        name='location_delete',
    ),
    path(
        'trainer/favorite/<int:id>',
        mark_favorite,
        name='mark_favorite',
    ),
    path(
        'accounts/favorites',
        get_user_favorites,
        name='user_favorites',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
