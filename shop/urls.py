from django.urls import path, re_path, include
from .views import *
from rest_framework.routers import SimpleRouter

router= SimpleRouter()
router.register(r'costumers', CostumerViewSet)

urlpatterns = [
    path('api/v1/category', CategoryListAPIView.as_view()),
    path('api/v1/category/<int:pk>', CategoryDetailAPIView.as_view()),
    re_path(r'^api/v1/category_products/(?P<pk>\d+)$', CategoryProductsAPIView.as_view()),
    path('api/v1/products', ProductsListAPIView.as_view()),
    path('api/v1/products/<int:pk>', ProductsDetailAPIView.as_view()),
    path('api/v1/', include(router.urls))
]
