from django.db import models


class Type(models.Model):
    name_type = models.CharField(max_length=60, verbose_name='Название')

    def __str__(self):
        return str(self.name_type)

    class Meta:
        verbose_name_plural = 'Вид'


class Animals(models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Вид'
    )
    name = models.CharField \
        (max_length=60, verbose_name='Название', unique=True)

    def __str__(self):
        return f'{str(self.name), str(self.type)}'

    class Meta:
        verbose_name_plural = 'Животные'
