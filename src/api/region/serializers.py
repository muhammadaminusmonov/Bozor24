from rest_framework import serializers
from region.models import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id', 'name', 'parent_region', 'add_region_at'
        ]
