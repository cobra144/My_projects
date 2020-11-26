from django.db import models
from django.urls import reverse
from exiffield.fields import ExifField
from exiffield.getters import exifgetter

class Category(models.Model):
    objects = None
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('story_by_category', args=[self.slug])


class Galeria(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    nazwa = models.CharField(max_length=32)
    opis = models.TextField(default='')
    rok_powstania = models.DateField(null=False, blank=False)
    zdjecie = models.ImageField(upload_to="media", blank=True)
    slug = models.AutoField(primary_key=True)
    camera = models.CharField(
        editable=False,
        max_length=100,
    )
    Xres = models.CharField(
        editable=False,
        max_length=100,
    )
    Yres = models.CharField(
        editable=False,
        max_length=100,
    )
    exif = ExifField(
        source='zdjecie',
        denormalized_fields={
            'camera': exifgetter('Model'),
            'Xres': exifgetter('ExifImageWidth'),
            'Yres': exifgetter('ExifImageHeight'),
        },
    )
    class Meta:
        ordering=('-nazwa',)
    def __str__(self):
        return self.nazwa
    def get_absolute_url(self):
       return reverse('story_detail',args=[self.slug,])



class UploadedImage(models.Model):
    objects = None
    image = models.ImageField(upload_to="media", blank=True)
    camera = models.CharField(
        editable=False,
        max_length=100,
    )
    exif = ExifField(
        source='image',
        denormalized_fields={
            'camera': exifgetter('Model'),
        },
    )

