from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class Language(models.Model):
    """ language model

    Multiple versions of languages allowed
    """

    name = models.CharField(max_length=120)
    version = models.CharField(max_length=20)
    base_doc_url = models.URLField()

    class Meta:
        unique_together = ['name', 'version']

    def __str__(self):
        return f'lang: {self.name} ver: {self.version}'


class Snippet(models.Model):
    """ snip class """

    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=120)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    language = models.ManyToManyField(Language, related_name='snippets')

    def __str__(self):
        return self.title


class Fourm(models.Model):
    """ abstract base class

    For comments
    and annotations
    """

    author = models.ForeignKey(User, blank=True, null=False)
    created = models.DateTimeField(blank=True, null=False)
    snippet = models.ForeignKey(Snippet)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            now = datetime.now()
            self.created = now
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author.username} commented on {self.snippet.title}'


class Comment(Fourm):
    """ only for plane text in comments """

    text = models.TextField()


class Annotation(Fourm):
    """ only for annotations on the form of code """

    code = models.TextField()
    line_begin = models.PositiveSmallIntegerField()
    line_end = models.PositiveSmallIntegerField()
