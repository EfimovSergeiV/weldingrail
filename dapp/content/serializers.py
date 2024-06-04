from rest_framework import serializers
from content.models import SliderModel, SubTitleSliderModel
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField, TranslatedField


class SubTitleSliderModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubTitleSliderModel)

    class Meta:
        model = SubTitleSliderModel
        fields = ['id', 'translations']


class SliderModelSerializer(TranslatableModelSerializer):
    # https://github.com/django-parler/django-parler-rest/blob/master/testproj/serializers.py


    sub_title = SubTitleSliderModelSerializer(many=True)

    class Meta:
        model = SliderModel
        fields = ('id', 'title', 'url', 'image', 'sub_title',)