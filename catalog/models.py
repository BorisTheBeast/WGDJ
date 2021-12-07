from django.db import models
from django.urls import reverse


class Gold(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class GoldImage(models.Model):
    gold = models.ForeignKey(
        Gold,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField(upload_to='gold')