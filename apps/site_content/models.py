from django.db import models
from ckeditor.fields import RichTextField


class ContentItem(models.Model):
    slug = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    content = RichTextField(config_name='full')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('page-detail', args=[self.slug])

    def __str__(self):
        return self.slug
