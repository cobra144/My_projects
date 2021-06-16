from django.db import models
from django.urls import reverse
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1,related_name="categories_cat")
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
    Fnum = models.CharField(
        editable=False,
        max_length=100,
    )
    ogniskowa = models.CharField(
        editable=False,
        max_length=100,
    )
    ekspozycja = models.CharField(
        editable=False,
        max_length=100,
    )
    firma = models.CharField(
        editable=False,
        max_length=100,
    )
    data = models.CharField(
        editable=False,
        max_length=100,
    )
    iso = models.CharField(
        editable=False,
        max_length=100,
    )

    exif = ExifField(
        source='zdjecie',
        denormalized_fields={
            'camera': exifgetter('Model'),
            'Xres': exifgetter('ExifImageWidth'),
            'Yres': exifgetter('ExifImageHeight'),
            'Fnum': exifgetter('FNumber'),
            'ogniskowa': exifgetter('FocalLength'),
            'ekspozycja': exifgetter('ExposureTime'),
            'firma': exifgetter('Manufacturer'),
            'data': exifgetter('DateTimeOriginal'),
            'iso': exifgetter('ISO'),



        },
    )
    class Meta:
        ordering=('-nazwa',)

    def __str__(self):
        return self.nazwa

    def ciag(self):
        return str(self.data).replace(':', '-')



    def get_absolute_url(self):
       return reverse('story_detail',args=[self.slug,])

    def is_valid(self):
        pass



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


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo_user = models.ImageField(upload_to="media", blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class UlubionyAlbum(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    albumy = models.ForeignKey(Galeria, on_delete=models.CASCADE, null=True)
