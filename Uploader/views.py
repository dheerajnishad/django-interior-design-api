from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ProductDetails.models import Product
from Uploader.models import CategorySelector, BannerImages, OfferImages, BrandSelector
from .serializer import ProductImageUploadSerializer, CategorySelectorSerializer, OfferImageSerializer, \
    BannerImageSerializer, BrandSelectorSerializer


class ProjectImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = ProductImageUploadSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


