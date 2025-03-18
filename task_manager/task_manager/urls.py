from django.contrib import admin
from django.urls import path, include
from tasks.views import user_login 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', user_login, name='login'),
    path('tasks/', include('tasks.urls')), 
]
