from django.db import models
from django_resized import ResizedImageField
from parler.models import TranslatableModel, TranslatedFields


class SliderModel(TranslatableModel):
    """ Slider model """

    activated = models.BooleanField(verbose_name="Activated", default=True)
    priority = models.IntegerField(verbose_name="Priority", default=100)
    url = models.JSONField(verbose_name="URL", null=True, blank=True)

    translations = TranslatedFields(
        title = models.CharField(verbose_name="Title", max_length=300)
    )

    image = ResizedImageField(
        size=[1220, 380],
        crop = ['middle', 'center'],
        upload_to='img/slides/1220x380/',
        default='img/slides/1220x380/default.webp',
        quality=100,
        verbose_name='',
        force_format='WEBP',
    )

    class Meta:
        ordering = ['-priority',]
        verbose_name = "Top slide"
        verbose_name_plural = "Top slides"

        def __str__(self):
            return self.model.safe_translation_getter('title', any_language=True)




class SubTitleSliderModel(TranslatableModel):
    """ Subtitle slider model """

    slide = models.ForeignKey(SliderModel, verbose_name="Slide", on_delete=models.CASCADE, related_name="sub_title")
    
    translations = TranslatedFields(
        text = models.CharField(verbose_name="Text", max_length=100)
    )

    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Text"

        def __str__(self):
            return self.text