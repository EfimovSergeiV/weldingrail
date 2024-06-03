from django.contrib import admin
from parler import forms
from django.utils.safestring import mark_safe
from django.forms import TextInput, CharField, ModelForm
from content.models import SliderModel, SubTitleSliderModel
from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline



class SliderForm(forms.TranslatableModelForm):
    title = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))
    url = CharField(widget=TextInput(attrs={'style': 'width: 100%;'}))

    class Meta:
        model = SliderModel
        fields = '__all__'


class SubTitleSliderForm(forms.TranslatableModelForm):
    text = forms.TranslatedField(widget=TextInput(attrs={'style': 'width: 100%;'}))

    class Meta:
        model = SubTitleSliderModel
        fields = '__all__'


class SubTitleSliderInline(TranslatableTabularInline):
    model = SubTitleSliderModel
    form = SubTitleSliderForm
    extra = 0
    fields = ('text',)


class SliderAdmin(TranslatableAdmin):
    
    def activated_image(self, obj):
        return mark_safe('<img style="width: 100vh; background-color: white;" src="/media/%s" alt="Нет изображения" width="100" height="auto" />' % (obj.image))
    activated_image.short_description = 'Image'

    list_display = ('id', 'title', 'activated', 'priority',)
    list_editable = ('activated', 'priority',)
    readonly_fields = ('activated_image',)
    form = SliderForm
    inlines = (SubTitleSliderInline,)
    fieldsets = (
        (None, {'fields': (('priority', 'activated',), ( 'title',), 'url', 'image', 'activated_image')}),
    )


admin.site.register(SliderModel, SliderAdmin)