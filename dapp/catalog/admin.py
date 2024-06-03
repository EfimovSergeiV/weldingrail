from django.contrib import admin
from django.forms import TextInput, CharField
from django.utils.safestring import mark_safe
from django_ckeditor_5.widgets import CKEditor5Widget
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from mptt.forms import MPTTAdminForm, TreeNodeChoiceField, TreeNodeMultipleChoiceField
from parler import forms
from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline

from catalog.models import CategoryModel, ProductModel, ProductAdvantageModel, ProductPropertiesModel



class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    url = CharField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    description = forms.TranslatedField(widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"},))

    class Meta:
        model = CategoryModel
        fields = '__all__'


class CategoryAdmin(TranslatableAdmin, DraggableMPTTAdmin):
    form = CategoryAdminForm

    list_display = ('tree_actions', 'indented_title', 'activated',)
    list_editable = ('activated',)
    fieldsets = (
        (None, {'fields': (('section', 'parent', 'activated'),'name', 'url','description',)}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'url': ('name',)}



class ProductAdminForm(forms.TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    category = TreeNodeChoiceField(queryset=CategoryModel.objects.all(), label= 'Категория')
    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    keywords = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    description = forms.TranslatedField(widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"},))

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductAdvantageForm(forms.TranslatableModelForm):
    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))

    class Meta:
        model = ProductAdvantageModel
        fields = '__all__'


class ProductAdvantageInline(TranslatableTabularInline):
    model = ProductAdvantageModel
    form = ProductAdvantageForm
    extra = 0
    fields = ('name', 'priority',)


class ProductProductPropertiesForm(forms.TranslatableModelForm):
    name = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    value = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))

    class Meta:
        model = ProductPropertiesModel
        fields = '__all__'


class ProductPropertiesInline(TranslatableTabularInline):
    model = ProductPropertiesModel
    form = ProductProductPropertiesForm
    extra = 0
    fields = ('name', 'value', 'priority',)


class ProductAdmin(TranslatableAdmin):
    def xs_image(self, obj):
        return mark_safe('<img style="background-color: white; padding: 15px; border-radius: 5px;" src="/media/%s" alt="Нет изображения" width="50" height="auto" />' % (obj.image))
    xs_image.short_description = 'Image'

    def activated_image(self, obj):
        return mark_safe('<img style="margin-right:-10vh; background-color: white; padding: 4px; border-radius: 5px;" src="/media/%s" alt="Нет изображения" width="100" height="auto" />' % (obj.image))
    activated_image.short_description = 'Image'

    # prepopulated_fields = {'keywords': ('name',)}


    form = ProductAdminForm

    list_display = ('id', 'xs_image', 'name', 'priority', 'activated',)
    list_display_links = ('id', 'xs_image', 'name')
    list_editable = ('priority', 'activated',)
    list_filter = ('category',)
    search_fields = ('id', 'category', 'name',)
    readonly_fields = ('activated_image',)
    inlines = (ProductAdvantageInline, ProductPropertiesInline)
    fieldsets = (
        (None, {'fields': (('priority', 'category', 'activated',), ('activated_image', 'image',), 'name', 'keywords', ('description',),)}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        
        return {'keywords': ('name',)}




admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)