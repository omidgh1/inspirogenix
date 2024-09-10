from django.db import models

class Resume(models.Model):
    about_me = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    experiences = models.TextField()
    certificates = models.TextField()
    publications = models.TextField()
    picture = models.ImageField(upload_to='pictures/')
    social_media_links = models.TextField()

    def __str__(self):
        return "Resume Information"
