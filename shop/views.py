from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.settings import api_settings
from .serializers import CategorySerializer,CategoryProductsSerializer, ProductSerializer
from .models import Product, Category

class ProductsListAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
class ProductsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
#I can use default classes DRF and write class with 2 string, 
#but in this task i want make my own class based 
#on parent class APIView 
class CategoryListAPIView(APIView):
    queryset = Category.objects.all()
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = CategorySerializer
    
    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator= None
            else:
                self._paginator= self.pagination_class()
        return self._paginator
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    #def get(self, request, **kwargs,):
        #return Response({'name': CategorySerializer(Category.objects.all(), many=True).data})
#    def post(self, request):
 #       serializer= CategorySerializer(data=request.data)
  #      serializer.is_valid(raise_exception= True)
   #     serializer.save()
    #    return Response({'name': serializer.data })

class CategoryDetailAPIView(APIView):
    def get(self, request, **kwargs):
        pk= kwargs.get('pk')
        if not pk:
            return Response({'error': 'method GET not allowed'})
        try:
            objects=Category.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})
        return Response({'name': CategorySerializer(Category.objects.get(pk=pk)).data })
    def put(self, request, *args, **kwargs):
        pk= kwargs.get('pk')
        if not pk:
            return Response({'error': 'method PUT not allowed'})
        try:
            instance = Category.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})
        serializer = CategorySerializer(data= request.data, instance= instance)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response({'category':serializer.data})
    def delete(self, request, *args, **kwargs):
        pk= kwargs.get('pk')
        if not pk:
            return Response({'error': 'method Delete is not allowed'})
        try:
            remv= Category.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exist'})
        Category.objects.get(pk=pk).delete()
        return Response({'category': 'deleted category ' + str(pk)})
class CategoryProductsAPIView(APIView):
    def get(self, request, pk):
        pkey= Category.objects.get(pk=pk)
        products= pkey.category_products.all().values()
        return Response({'title': CategoryProductsSerializer(products, many= True).data })
    
