from rest_framework import serializers
from api.models import btn,turfImages

class Btnserializer(serializers.ModelSerializer):
    class Meta:
        model = btn
        fields = ['id','is_on']


class TurfImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = turfImages
        fields = '__all__' #['turfDetails','generalTurfImages']

    
