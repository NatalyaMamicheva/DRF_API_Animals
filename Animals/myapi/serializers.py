from rest_framework import serializers

from .models import Animals, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

    def create(self, validated_data):
        return Type.objects.create(**validated_data)


class AnimalsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="type.name_type", read_only=True)
    class Meta:
        model = Animals
        fields = ['name', 'type']

    def create(self, validated_data):
        return Animals.objects.create(**validated_data)
