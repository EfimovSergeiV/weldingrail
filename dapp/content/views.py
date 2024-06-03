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
        
        return Response(slide.data)