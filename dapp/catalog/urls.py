from django.urls import path
from catalog.views import CategoryModelView, ProductsModelView, ProductModelView

urlpatterns = [
    path('categories/', CategoryModelView.as_view(), name='categories'),
    path('products/', ProductsModelView.as_view(), name='products'),
    path('product/<int:id>/', ProductModelView.as_view(), name='product'),
]