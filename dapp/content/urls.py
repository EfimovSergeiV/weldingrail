from django.urls import path
from content.views import SliderView

urlpatterns = [
    path('slides/', SliderView.as_view(), name='slides'),
]