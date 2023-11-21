from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index' ),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
]
