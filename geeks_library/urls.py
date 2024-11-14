from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from main_page import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('', include('main_page.urls')),
    path('about_me/', views.about_me_response),
    path('about_cars/', views.about_my_cars_response),
    path('system_time/', views.system_time),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
