from django.db import models

class HomePage(models.Model):
    sentence = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/')
    logo_image = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return "Homepage Settings"