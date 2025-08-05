# Tell Python how to Convert your Python DB Model Data into JSON Values (String)

from rest_framework import serializers
from .models import TVShowActorsModel

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShowActorsModel
        fields = '__all__'