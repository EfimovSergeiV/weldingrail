from content.models import SliderModel, SubTitleSliderModel
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField, TranslatedField


class SubTitleSlider(TranslatableModelSerializer):
    """ Не переключается язык """
    
    class Meta:
        model = SubTitleSliderModel
        fields = ('id', 'text',)


class SliderModelSerializer(TranslatableModelSerializer):
    # sub_title = TranslatedField() # https://github.com/django-parler/django-parler-rest/blob/master/testproj/serializers.py

    class Meta:
        model = SliderModel
        fields = ('id', 'title', 'url', 'image', 'sub_title',)