from rest_framework import serializers
from country.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',
                  'alpha2',
                  'alpha3',
                  'numeric')