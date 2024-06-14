from django.contrib import admin
from customers.models import CustomerMessagesModel, SubscribersModel, PriceRequestsModel


class CustomerMessagesAdmin(admin.ModelAdmin):

    def time_created(self, obj):
        return obj.date_created.strftime('%H:%M:%S %Y-%m-%d')

    list_display = ('name', 'email', 'company', 'country', 'time_created')
    search_fields = ('name', 'email', 'company', 'country', 'message')
    list_filter = ('date_created',)
    readonly_fields = ('time_created',)

    fieldsets = (
        (None, {'fields': (('name', 'email',), ('company', 'country',), 'message')}),
    )



class PriceRequestsAdmin(admin.ModelAdmin):

    def time_created(self, obj):
        return obj.date_created.strftime('%H:%M:%S %Y-%m-%d')

    list_display = ('name', 'email', 'company', 'country', 'product', 'time_created')
    search_fields = ('name', 'email', 'company', 'country', 'product')
    list_filter = ('date_created',)
    readonly_fields = ('time_created',)

    fieldsets = (
        (None, {'fields': (('name', 'email',), ('company', 'country',), 'product')}),
    )



class SubscribersAdmin(admin.ModelAdmin):

    def time_created(self, obj):
        return obj.date_created.strftime('%H:%M:%S %Y-%m-%d')
    
    list_display = ('email', 'time_created')
    search_fields = ('email',)
    list_filter = ('date_created',)
    readonly_fields = ('time_created',)



admin.site.register(CustomerMessagesModel, CustomerMessagesAdmin)
admin.site.register(PriceRequestsModel, PriceRequestsAdmin)
admin.site.register(SubscribersModel, SubscribersAdmin)
