from django.db import models
from django.utils import timezone
from catalog.models import ProductModel



class CustomerMessagesModel(models.Model):
    """ Model for storing customer messages. """

    date_created = models.DateTimeField(auto_now=True, verbose_name='Date created',)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'Customer message'
        verbose_name_plural = 'Customer messages'

    def __str__(self):
        return self.name

    

class PriceRequestsModel(models.Model):
    """ Model for storing price requests. """

    date_created = models.DateTimeField(auto_now=True, verbose_name='Date created',)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    product = models.ForeignKey(ProductModel, related_name='request_price', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Price request'
        verbose_name_plural = 'Price requests'

    def __str__(self):
        return self.name



class SubscribersModel(models.Model):
    """ Model for storing subscribers. """

    date_created = models.DateTimeField(auto_now=True, verbose_name='Date created',)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email