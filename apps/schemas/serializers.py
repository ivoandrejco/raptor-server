from datetime import date
from rest_framework import serializers
from .models import Schema


class SchemasSerializer(serializers.ModelSerializer):
    id          = serializers.ReadOnlyField()
    created_on  = serializers.ReadOnlyField()
    updated_on  = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['created_on'] = date.today()
        validated_data['updated_on'] = date.today()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)

    def partial_update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)

    class Meta:
        model = Schema
        fields = ['id','kind','title','json','ordering','updated_on','created_on']


