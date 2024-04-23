from django.urls import path
from catalog.views import CategoriesModelView, ProductsModelView, ProductModelView

urlpatterns = [
    path('categories/', CategoriesModelView.as_view(), name='categories'),
    path('products/', ProductsModelView.as_view(), name='products'),
    path('product/<int:id>/', ProductModelView.as_view(), name='product'),
]