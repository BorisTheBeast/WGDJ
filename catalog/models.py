from django.db import models
from django.urls import reverse


class Gold(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    promo = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gold-detail', args=[str(self.id)])


class GoldImage(models.Model):
    gold = models.ForeignKey(
        Gold,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField(upload_to='gold')


class Premium(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    promo = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('premium-detail', args=[str(self.id)])


class PremiumImage(models.Model):
    premium = models.ForeignKey(
        Premium,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField(upload_to='premium')


class TankType(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a tank type", null=True)

    def __str__(self):
        return self.name


class TankNation(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a tank nation", null=True)

    def __str__(self):
        return self.name


class Tank(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    promo = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    priority = models.BooleanField(default=False)
    type = models.ManyToManyField(TankType, help_text="Select a type for this tank")
    nation = models.ManyToManyField(TankNation, help_text="Select a nation for this tank")
    tier = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tank-detail', args=[str(self.id)])


class TankImage(models.Model):
    tank = models.ForeignKey(
        Tank,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField(upload_to='tanks')
