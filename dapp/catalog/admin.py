from django.contrib import admin
from django.forms import TextInput
from django.utils.safestring import mark_safe
from django_ckeditor_5.widgets import CKEditor5Widget
from parler import forms
from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline

from catalog.models import CategoryModel, ProductModel



class CategoryAdminForm(forms.TranslatableModelForm):

    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    description = forms.TranslatedField(widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"},))

    class Meta:
        model = CategoryModel
        fields = '__all__'


class CategoryAdmin(TranslatableAdmin):

    form = CategoryAdminForm
    list_display = ('id', 'name', 'priority','show',)
    list_display_links = ('id', 'name')
    list_editable = ('priority','show',)
    fieldsets = (
        (None, {'fields': (('priority','show',), ('name',), ('description',))}),
    )


class ProductAdminForm(forms.TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    description = forms.TranslatedField(widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"},))

    class Meta:
        model = ProductModel
        fields = '__all__'

class ProductAdmin(TranslatableAdmin):
    def xs_image(self, obj):
        print(obj.image)
        return mark_safe('<img style="background-color: white; padding: 15px; border-radius: 5px;" src="/media/%s" alt="Нет изображения" width="50" height="auto" />' % (obj.image))
    xs_image.short_description = 'Image'

    def show_image(self, obj):
        print(obj.image)
        return mark_safe('<img style="margin-right:-10vh; background-color: white; padding: 4px; border-radius: 5px;" src="/media/%s" alt="Нет изображения" width="100" height="auto" />' % (obj.image))
    show_image.short_description = 'Image'

    form = ProductAdminForm

    list_display = ('id', 'xs_image', 'name', 'priority', 'show',)
    list_display_links = ('id', 'xs_image', 'name')
    list_editable = ('priority', 'show',)
    list_filter = ('category',)
    search_fields = ('id', 'category', 'name',)
    readonly_fields = ('show_image',)
    fieldsets = (
        (None, {'fields': (('priority', 'category', 'show',), ('show_image', 'image',), ('name',), ('description',),)}),
    )



admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)