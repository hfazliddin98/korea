from django.db import models

class Links(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    link = models.CharField(max_length=500)

    def __str__ (self):
        return self.link