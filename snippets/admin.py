from django.contrib import admin
from .models import (
        Language, Snipit, Comment, Annotation)


admin.site.register(Language)
admin.site.register(Snipit)
admin.site.register(Comment)
admin.site.register(Annotation)
