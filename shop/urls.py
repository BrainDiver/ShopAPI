from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('api/v1/category', CategoryListAPIView.as_view()),
    path('api/v1/category/<int:pk>', CategoryDetailAPIView.as_view()),
    re_path(r'^api/v1/category_products/(?P<pk>\d+)$', CategoryProductsAPIView.as_view()),
    path('api/v1/products', ProductsListAPIView.as_view()),
    path('api/v1/products/<int:pk>', ProductsDetailAPIView.as_view())
]
