from django.contrib import admin
from customers.models import CustomerMessagesModel, SubscribersModel, PriceRequestsModel


class CustomerMessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'country', 'date_created')
    search_fields = ('name', 'email', 'company', 'country', 'message')
    list_filter = ('date_created',)

    fieldsets = (
        (None, {'fields': (('name', 'email',), ('company', 'country',), 'message')}),
    )



class PriceRequestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'country', 'product', 'date_created')
    search_fields = ('name', 'email', 'company', 'country', 'product')
    list_filter = ('date_created',)

    fieldsets = (
        (None, {'fields': (('name', 'email',), ('company', 'country',), 'product')}),
    )



class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created')
    search_fields = ('email',)
    list_filter = ('date_created',)



admin.site.register(CustomerMessagesModel, CustomerMessagesAdmin)
admin.site.register(PriceRequestsModel, PriceRequestsAdmin)
admin.site.register(SubscribersModel, SubscribersAdmin)
