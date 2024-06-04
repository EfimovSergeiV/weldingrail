from django.urls import path
from catalog.views import CategoriesView, SubCategoriesView, CategoryModelView, ProductsModelView, ProductModelView

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('subcategories/', SubCategoriesView.as_view(), name='subcategories'),
    path('category/<int:id>/', CategoryModelView.as_view(), name='category'),
    path('category/<slug:url>/', CategoryModelView.as_view(), name='category'),
    path('products/', ProductsModelView.as_view(), name='products'),
    path('products/<slug:url>/', ProductsModelView.as_view(), name='products'),
    path('product/<int:id>/', ProductModelView.as_view(), name='product'),
]