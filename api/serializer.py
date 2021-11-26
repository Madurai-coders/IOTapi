from rest_framework import serializers
from api.models import btn

class btnserializer(serializers.ModelSerializer):
    class Meta:
        model = btn
        fields = ['id','is_on']