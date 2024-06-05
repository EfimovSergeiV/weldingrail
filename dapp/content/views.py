from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import get_language_from_request, get_language_from_path
from content.models import SliderModel, SubTitleSliderModel
from content.serializers import SliderModelSerializer


class SliderView(APIView):

    def get(self, request, lang):
        queryset = SliderModel.objects.language(lang).filter(activated=True)
        slide = SliderModelSerializer(queryset, many=True, context={'request': request})

        lang = lang if lang != 'zh' else 'zh-hans'
        clear_data = []

        for data in slide.data:
            clear_data.append({
                'id': data['id'],
                'title': data['title'],
                'image': data['image'],
                'url': data['url'],
                'sub_title': [ sub_title['translations'][lang]['text'] for sub_title in data['sub_title'] ],
            })
        
        return Response(clear_data)