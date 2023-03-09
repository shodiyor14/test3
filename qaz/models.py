from django.db import models


class Clothes(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField()
    images = models.ImageField(upload_to='Clothes')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'clothes'
        verbose_name_plural = 'clothes'

