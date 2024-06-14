from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from customers.serializers import CustomerMessagesSerializer, PriceRequestsSerializer, SubscribersSerializer
from customers.models import CustomerMessagesModel, PriceRequestsModel, SubscribersModel



class CustomerMessagesView(APIView):
    """ View for customer messages. """

    def post(self, request):
        """ Post method for customer messages. """

        serializer = CustomerMessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PriceRequestsView(APIView):
    """ View for price requests. """

    def post(self, request):
        """ Post method for price requests. """

        serializer = PriceRequestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubscribersView(APIView):
    """ View for subscribers. """

    def post(self, request):
        """ Post method for subscribers. """

        serializer = SubscribersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
