from django.contrib import admin
from django.urls import path
from .views import CreateCheckoutSessionView, DonationView, CancelView, SuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', DonationView.as_view(), name='donation')
]
