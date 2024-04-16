from django.db import models
from django_resized import ResizedImageField
from parler.models import TranslatableModel, TranslatedFields
from django_ckeditor_5.fields import CKEditor5Field


class CategoryModel(TranslatableModel):
    """ Product categories """

    show = models.BooleanField(verbose_name="show", default=False)
    priority = models.IntegerField(verbose_name="Priority", default=50)
    url = models.SlugField(verbose_name="URL", max_length=300, unique=False)

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
        size = [320, 240],
        crop = ['middle', 'center'],
        upload_to='img/prods/320x320/',
        default='img/prods/320x320/default.webp',
        quality=100,
        verbose_name='',
        force_format='WEBP',
    )

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Name", max_length=300),
        keywords = models.CharField(verbose_name="Keywords", max_length=300, null=True, blank=True),
        description = CKEditor5Field(verbose_name="Description", config_name='extends') #default
    )

    class Meta:
        ordering = ['category','-priority',]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    

# class ProductImagesModel(models.Model):
#     """ Product images model """

#     product = models.ForeignKey(ProductModel, verbose_name="Product", on_delete=models.CASCADE, related_name="product_images")
#     priority = models.IntegerField(verbose_name="Priority", default=50)
#     image = ResizedImageField(
#         size = [320, 240],
#         crop = ['middle', 'center'],
#         upload_to='img/prods/320x320/',
#         default='img/prods/320x320/default.webp',
#         quality=100,
#         verbose_name='',
#         force_format='WEBP',
#     )

#     class Meta:
#     ordering = ['-priority',]
#         verbose_name = "Product image"
#         verbose_name_plural = "Product images"

#     def __str__(self):
#         return self.product.safe_translation_getter('name', any_language=True)


class ProductAdvantageModel(TranslatableModel):
    """ Product advantages model """

    product = models.ForeignKey(ProductModel, verbose_name="Product", on_delete=models.CASCADE, related_name="product_advantages")
    priority = models.IntegerField(verbose_name="Priority", default=100)
    
    translations = TranslatedFields(
        name = models.CharField(verbose_name="Name", max_length=600, null=True, blank=True),
    )

    class Meta:
        ordering = ['-priority',]
        verbose_name = "Product advantage"
        verbose_name_plural = "Product advantages"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    

class ProductPropertiesModel(TranslatableModel):
    """ Product properties model """

    product = models.ForeignKey(ProductModel, verbose_name="Product", on_delete=models.CASCADE, related_name="product_properties")
    priority = models.IntegerField(verbose_name="Priority", default=100)
    
    translations = TranslatedFields(
        name = models.CharField(verbose_name="Name", max_length=300, null=True, blank=True),
        value = models.CharField(verbose_name="Value", max_length=300, null=True, blank=True),
    )

    class Meta:
        ordering = ['-priority',]
        verbose_name = "Product property"
        verbose_name_plural = "Product properties"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    
