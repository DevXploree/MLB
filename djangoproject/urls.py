from django.contrib import admin
from django.urls import path
from .views import home, stats, logout_, update_stats_data, results, savePrediction

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_, name="logout"),
    path("", home, name='home'),
    path("stats/", stats, name='stats'),
    path("save-user-prediction/", savePrediction, name='savePrediction'),
    path("update-stats/", update_stats_data, name='update-stats'),
    path("results/", results, name='results'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
