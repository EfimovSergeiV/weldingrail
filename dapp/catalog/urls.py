from django.urls import path
from catalog.views import CategoryModelView, ProductModelView

urlpatterns = [
    path('categories/', CategoryModelView.as_view(), name='categories'),
    path('products/', ProductModelView.as_view(), name='products'),
]