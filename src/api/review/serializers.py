from rest_framework import serializers
from region.models import Region
from review.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id', 'product', 'user', 'rating'
        ]
