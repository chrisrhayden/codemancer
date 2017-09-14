from rest_framework import serializers
from .models import Language, Annotation


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name',)


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('author', 'created', 'snippet',
                  'code', 'line_begin', 'line_end')
