from django.urls import path
from customers.views import CustomerMessagesView, PriceRequestsView, SubscribersView



urlpatterns = [
    path('messages/', CustomerMessagesView.as_view(), name='messages'),
    path('request-price/', PriceRequestsView.as_view(), name='request_price'),
    path('subscribe/', SubscribersView.as_view(), name='subscribe'),
]