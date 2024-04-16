from django.db import models
from django_resized import ResizedImageField
from parler.models import TranslatableModel, TranslatedFields
from django_ckeditor_5.fields import CKEditor5Field


class CategoryModel(TranslatableModel):
    """ Product categories """

    show = models.BooleanField(verbose_name="show", default=False)
    priority = models.IntegerField(verbose_name="Priority", default=50)

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Name", max_length=300),
        description = CKEditor5Field(verbose_name="Description",null=True, blank=True, config_name='extends')
    )

    class Meta:
        ordering = ['-priority',]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    

class ProductModel(TranslatableModel):
    """ Product model """

    show = models.BooleanField(verbose_name="Activated", default=False)
    priority = models.IntegerField(verbose_name="Priority", default=50)
    category = models.ForeignKey(CategoryModel, verbose_name="Category", on_delete=models.CASCADE, related_name="product_category")

    image = ResizedImageField(
        size = [320, 320],
        crop = ['middle', 'center'],
        upload_to='img/prods/320x320/',
        default='img/prods/320x320/default.webp',
        quality=100,
        verbose_name='',
        force_format='WEBP',
    )

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Name", max_length=300),
        description = CKEditor5Field(verbose_name="Description", config_name='extends') #default
    )

    class Meta:
        ordering = ['category','-priority',]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)