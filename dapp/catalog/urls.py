from django.urls import path
from catalog.views import CategoriesModelView, CategoryModelView, ProductsModelView, ProductModelView

urlpatterns = [
    path('categories/', CategoriesModelView.as_view(), name='categories'),
    path('category/<int:id>/', CategoryModelView.as_view(), name='category'),
    path('category/<slug:url>/', CategoryModelView.as_view(), name='category'),
    path('products/', ProductsModelView.as_view(), name='products'),
    path('products/<slug:url>/', ProductsModelView.as_view(), name='products'),
    path('product/<int:id>/', ProductModelView.as_view(), name='product'),
]