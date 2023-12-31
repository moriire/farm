from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from users.views import IndexView

urlpatterns = [
    path("unicorn/", include('django_unicorn.urls')),
    path('auth/', include('users.urls')),
    path('farmers/', include('farmers.urls')),
    path('carts/', include('buyers.urls')),
    path('posts/', include('forum.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('services/', TemplateView.as_view(template_name="services.html"), name='services'),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)