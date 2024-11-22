from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from main_page import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', TemplateView.as_view(template_name='add_comments.html')),
    path('', include('main_page.urls')),
    path('', include('backet.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
