from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .people.views import generate_image
from django.views.generic import TemplateView
from .products import views
from  .appointment import views as appt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-image/', generate_image, name="generate-image"),
    path('appointments', appt_views.AppointmentsView.as_view(), name="appointments")
    path('products', views.view_products, name="products"),
    path('', TemplateView.as_view(template_name="index.html"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)