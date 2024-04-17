from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import get_language_from_request, get_language_from_path
from catalog.models import CategoryModel, ProductModel, ProductPropertiesModel, ProductAdvantageModel
from catalog.serializers import CategoryModelSerializer, ProductModelSerializer, ProductPropertiesSerializer



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

    qs_properties = ProductPropertiesModel.objects.all()
    qs_advantages = ProductAdvantageModel.objects.all()

    def get(self, request, lang, id):

        product_advantages = []
        product_properties = []

        try:
            queryset = ProductModel.objects.language(lang).get(show=True, id=id)

            product_props_qs = self.qs_properties.language(lang).filter(product=queryset)
            product_adv_qs = self.qs_advantages.language(lang).filter(product=queryset)

            sr_props = ProductPropertiesSerializer(product_props_qs, many=True)
            sr_adv = ProductPropertiesSerializer(product_adv_qs, many=True)

            product_properties = sr_props.data
            product_advantages = sr_adv.data

        except ProductModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelSerializer(queryset, context={'request': request})

        data = serializer.data
        data['product_advantages'] = product_advantages
        data['product_properties'] = product_properties

        return Response(data)