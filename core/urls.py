from django.urls import path

# =============== Renderizar HTML diretamente ======================
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"))
]