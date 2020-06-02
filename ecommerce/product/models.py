from django.db import models
from django.utils.text import slugify

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length=50)
    catagory = models.ForeignKey(
        'Catagory', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=300)
    price = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Catagory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name
