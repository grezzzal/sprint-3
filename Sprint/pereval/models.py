from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=12)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

STATUS_CHOICES = [
    ("new", "новый"),
    ("pending", "на рассмотрении"),
    ("accepted", "принят"),
    ("rejected", "отклонен"),
]

class PerevalAdded(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    date_added = models.DateTimeField('Дата создания', auto_now_add=True)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=255)
    level_summer = models.CharField(max_length=255)
    level_autumn = models.CharField(max_length=255)
    level_spring = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')


class Coords(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.latitude} : {self.longitude} : {self.height}'


class PerevalImages(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.image_name}'

