from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Announcement', max_length=350)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Created')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news_page/{self.id}'


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'