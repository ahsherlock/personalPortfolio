from django.db import models

class Project (models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) #blank allows for field to be optional

    def __str__(self):
        return self.title