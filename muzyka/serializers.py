from rest_framework import serializers
from  .models import Galeria

class MuzykaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields =['slug','nazwa','rok_powstania','opis']
