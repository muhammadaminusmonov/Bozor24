from rest_framework.serializers import ModelSerializer
from payment.models import Transaction

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['buyer']