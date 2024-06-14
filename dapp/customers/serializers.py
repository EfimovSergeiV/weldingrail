from rest_framework.serializers import ModelSerializer
from customers.models import CustomerMessagesModel, PriceRequestsModel, SubscribersModel
# from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField, TranslatedField



class CustomerMessagesSerializer(ModelSerializer):

    class Meta:
        model = CustomerMessagesModel
        fields = '__all__'



class PriceRequestsSerializer(ModelSerializer):
    
    class Meta:
        model = PriceRequestsModel
        fields = '__all__'



class SubscribersSerializer(ModelSerializer):

    class Meta:
        model = CustomerMessagesModel
        fields = ('id', 'email', 'date_created',)