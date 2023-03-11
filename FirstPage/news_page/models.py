from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Created')

    def __str__(self):
        return self.title
