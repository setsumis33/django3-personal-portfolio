from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    # модели для работы с ними в админке
    # не забываем про makemigrations и migrate

    def __str__(self):
        return self.title
    # показывает название в панели админа