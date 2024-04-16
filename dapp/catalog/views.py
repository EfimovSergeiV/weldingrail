from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import get_language_from_request, get_language_from_path
from catalog.models import CategoryModel, ProductModel
from catalog.serializers import CategoryModelSerializer, ProductModelSerializer



class CategoryModelView(APIView):
    """ Category model view """

    def get(self, request, lang):
        queryset = CategoryModel.objects.language(lang).filter(show=True)
        serializer = CategoryModelSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    

class ProductsModelView(APIView):
    """ Products model view """

    def get(self, request, lang):
        queryset = ProductModel.objects.language(lang).filter(show=True)
        serializer = ProductModelSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    

class ProductModelView(APIView):
    """ Product model view """

    def get(self, request, lang, id):
        try:
            queryset = ProductModel.objects.language(lang).get(show=True, id=id)
        except ProductModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelSerializer(queryset, context={'request': request})
        return Response(serializer.data)