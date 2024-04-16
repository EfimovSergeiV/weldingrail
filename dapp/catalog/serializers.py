from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from catalog.models import CategoryModel, ProductModel, ProductAdvantageModel, ProductPropertiesModel



class CategoryModelSerializer(TranslatableModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'url', 'description',)


class ProductAdvantageSerializer(TranslatableModelSerializer):
    
        class Meta:
            model = ProductAdvantageModel
            fields = ('id', 'name',)

class ProductPropertiesSerializer(TranslatableModelSerializer):
    
        class Meta:
            model = ProductPropertiesModel
            fields = ('id', 'name', 'value')


class ProductModelSerializer(TranslatableModelSerializer):

    # ERR не переключают перевод
    product_advantages = ProductAdvantageSerializer(many=True)
    product_properties = ProductPropertiesSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'category', 'name', 'keywords', 'image', 'description', 'product_advantages', 'product_properties',)