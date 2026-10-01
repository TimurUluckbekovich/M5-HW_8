from rest_framework import serializers
from .models import Service, Order


class ServiceSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    final_price = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'description', 'category',
            'base_price', 'discount', 'final_price',
            'is_active', 'author', 'created_at'
        ]

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Название услуги должно содержать минимум 5 символов.")
        return value

    def validate_discount(self, value):
        if not (0 <= value <= 90):
            raise serializers.ValidationError("Скидка должна быть в диапазоне от 0 до 90%.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'service', 'client_name', 'phone', 'comment', 'created_at']