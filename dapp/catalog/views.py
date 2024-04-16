from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.translation import get_language_from_request, get_language_from_path
from catalog.models import CategoryModel, ProductModel
from catalog.serializers import CategoryModelSerializer, ProductModelSerializer



class CategoryModelView(APIView):
    """ Category model view """

    def get(self, request):
        """ Get method """
        lang_request = get_language_from_request(request)
        lang_path = get_language_from_path(request.path)
        print(lang_request)
        print(lang_path)

        queryset = CategoryModel.objects.language(lang_request).filter(show=True)

        serializer = CategoryModelSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    

class ProductModelView(APIView):
    """ Product model view """

    def get(self, request):
        """ Get method """

        lang_request = get_language_from_request(request)
        lang_path = get_language_from_path(request.path)

        queryset = ProductModel.objects.language(lang_request).filter(show=True)
        serializer = ProductModelSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)