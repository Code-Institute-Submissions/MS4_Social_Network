from django.urls import path

from .views import DonationView

urlpatterns = [
    path('donation/', DonationView.as_view(), name='donation'),
]
