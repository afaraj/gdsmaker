from rest_framework import serializers # This is important
from .models import GDS

class GDSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GDS
        fields = ('id', 'title', 'description', 'frozen', 'created_at', 'updated_at')