from rest_framework import serializers

from accounts.models import User

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password  = serializers.CharField()
    is_staff  = serializers.BooleanField()
    class Meta:        
        fields = [
        "username",
        "email",
        "password",
        "is_staff",
    ]
    model = User

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class ListUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    is_staff  = serializers.BooleanField()
    class Meta:
        fields = [
            "id"
            "username",
            "email",
            "is_staff",
        ]
        model = User
        lookup_field = "id"

class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password  = serializers.CharField()
    class Meta:
        fields = [
            "username",
            "email",
            "password",
        ]
        model = User

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
