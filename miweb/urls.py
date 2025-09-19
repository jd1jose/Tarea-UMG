from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', include('home.urls')),
    path('informacion/', include('informacion.urls')),
    path('principal/', include('principal.urls')),
    path("revista/", include("revista.urls")),
]
