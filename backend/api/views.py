from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from django.db.models import Q
from rest_framework import status
from .serializers import ProductSerializer
import json

class SearchView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        q = request.GET['q']
        if (q):
            query = Q(title__contains = q) | Q(description__contains = q)
            products = Product.objects.filter(query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
