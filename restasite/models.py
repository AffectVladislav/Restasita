from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)

    TYPE = [
        ('CHS', 'Горячие и холодные закуски'),
        ('SLD', 'Салаты'),
        ('SPS', 'Супы'),
        ('SDS', 'Гарниры'),
        ('HOT', 'Горячее'),
        ('SUS', 'Соусы'),
        ('DST', 'Десерты'),
        ('AHL', 'Алкоголь'),
    ]

    type = models.CharField(choices=TYPE, max_length=3, default='HOT', verbose_name='Тип')
