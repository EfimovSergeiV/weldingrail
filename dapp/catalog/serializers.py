from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from catalog.models import CategoryModel, ProductModel



class CategoryModelSerializer(TranslatableModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'description',)


class ProductModelSerializer(TranslatableModelSerializer):

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'description', 'image',)