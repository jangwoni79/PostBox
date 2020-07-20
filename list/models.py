from django.db import models

class Letter(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, upload_to='list/%Y/%m/%d/')

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.contents}'