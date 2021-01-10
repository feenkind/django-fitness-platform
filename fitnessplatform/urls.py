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
from apps.users.views import user_profile
from apps.trainers.views import *

urlpatterns = [
                  path('', start_view),
                  path('admin/', admin.site.urls),
                  path('user/', include('allauth.urls')),
                  path('user/', user_profile, name='user_profile'),
                  path('trainerlist/', get_trainer_list, name='trainer_list'),
                  path('trainer/<int:id>/', get_trainer_profile,
                       name='trainer_profile'),
                  path('trainer/', get_trainer_profile,
                       name='trainer_profile'),
                  path('trainer/edit', edit_trainer_profile,
                       name='trainer_profile_edit'),
                  path(
                      'trainer/upload', upload_trainer_profile,
                      name='trainer_profile_upload'
                  ),
                  path('trainer/locations', edit_trainer_locations,
                       name='trainer_profile_locations'),
                  path('trainer/locations/<int:id>', edit_trainer_locations,
                       name='trainer_profile_locations'),
                  path('trainer/locations/<create>', edit_trainer_locations,
                       name='trainer_profile_locations'),
                  path('trainer/locations/delete/<int:id>/', delete_location,
                       name='location_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
