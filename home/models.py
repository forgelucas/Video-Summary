from django.db import models

# Create your models here.
class Video(models.Model):
    titulo = models.CharField(max_length=100)
    video = models.FileField(upload_to='video/')
    transcricao = models.TextField(null=True, blank=True)
    resumo = models.TextField()

    def __str__(self):
        self.titulo
