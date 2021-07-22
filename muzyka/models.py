from django.db import models
from django.urls import reverse
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('story_by_category', args=[self.slug])


class Galeria(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="categories_cat")
    zespol = models.CharField(max_length=60,default='')
    nazwa = models.CharField(max_length=60)
    opis = models.TextField(default='')
    rok_powstania = models.DateField(null=False, blank=False)
    zdjecie = models.ImageField(upload_to="media", blank=True)
    slug = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('-nazwa',)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
       return reverse('paginacja', args=[self.slug])

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


class OcenaAlbumu(models.Model):
    objects = None
    ocena = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Galeria, on_delete=models.CASCADE, null=True)

class Znajomi(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='main_user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='friend')
