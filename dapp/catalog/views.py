from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import get_language_from_request, get_language_from_path
from catalog.models import CategoryModel, ProductModel, ProductPropertiesModel, ProductAdvantageModel
from catalog.serializers import CategoryModelSerializer, ProductModelSerializer, ProductPropertiesSerializer



class CategoriesModelView(APIView):
    """ Category model view """

    def get(self, request, lang):
        queryset = CategoryModel.objects.filter(level=0).language(lang).filter(activated=True)

        response_data = []

        for category_qs in queryset:
            category_children_qs = category_qs.get_children().language(lang).filter(activated=True)

            category = CategoryModelSerializer(category_qs, context={'request': request}).data    
            category_children = CategoryModelSerializer(category_children_qs, many=True, context={'request': request}).data

            category['children'] = category_children if category_children else None
            response_data.append(category)
        
        return Response(response_data)



class ProductsModelView(APIView):
    """ All products model view """

    qs_properties = ProductPropertiesModel.objects.all()
    qs_advantages = ProductAdvantageModel.objects.all()

    def get(self, request, lang):
        response_data = []

        queryset = ProductModel.objects.language(lang).filter(activated=True)
        serializer = ProductModelSerializer(queryset, many=True, context={'request': request})

        for data in serializer.data:
            product_props_qs = self.qs_properties.language(lang).filter(product=data['id'])
            product_adv_qs = self.qs_advantages.language(lang).filter(product=data['id'])

            sr_props = ProductPropertiesSerializer(product_props_qs, many=True)
            sr_adv = ProductPropertiesSerializer(product_adv_qs, many=True)

            data['product_properties'] = sr_props.data
            data['product_advantages'] = sr_adv.data

            response_data.append(data)

        

        return Response(response_data)
    

class ProductModelView(APIView):
    """ Select product model view """

    qs_properties = ProductPropertiesModel.objects.all()
    qs_advantages = ProductAdvantageModel.objects.all()

    def get(self, request, lang, id):

        product_advantages = []
        product_properties = []

        try:
            queryset = ProductModel.objects.language(lang).get(activated=True, id=id)

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