from django.contrib import admin
from .models import (
        Language, Snippet, Comment, Annotation)


admin.site.register(Language)
admin.site.register(Snippet)
admin.site.register(Comment)
admin.site.register(Annotation)
