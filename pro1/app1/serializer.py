from rest_framework import serializers
from . models import *

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:

        model=people

        fields='__all__'