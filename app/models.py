from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(verbose_name='Basliq',max_length=200)
    photo = models.ImageField(verbose_name='Sekil', upload_to='media/')
    tarix = models.DateField(verbose_name='tarix',auto_created=True)
    metn = models.TextField(verbose_name='metn',max_length=500)
