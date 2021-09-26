from rest_framework import serializers

from accounts.models import User

from products.models import Products
from products.api.v1.validate import (
    is_valid_user_admin,
    is_valid_product_name
)

class CreateProductsSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_staff=True))
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Products
        fields = [
            "id"
            "user",
            "name",
            "price",
            "description",
            "quantity",
        ]


    #com a adição do filter talvez esse metodo de validação
    #não seria necessario
    def validate_user(self, value):
        if is_valid_user_admin(value):
            return value
        else:
            raise serializers.ValidationError("usuario não é administrador")

    def validate_name(self, value):
        if is_valid_product_name(value):
            return value
        else:
            raise serializers.ValidationError("Esse nome de produto já está sendo utilizado")

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com preço negativo")
        else:
            return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com quantidade negativa")
        else:
            return value    

    def create(self, validated_data):
        products = Products.objects.create(**validated_data)
        print(validated_data)
        return products

    
class ListProductsSerializers(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Products
        fields = [
            "name",
            "price",
            "description",
            "quantity",
        ]

class UpdateProductsSerializers(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Products
        fields = [
            "name",
            "price",
            "description",
            "quantity",
        ]

    def validate_name(self, value):
        if is_valid_product_name(value):
            return value
        else:
            raise serializers.ValidationError("Esse nome de produto já está sendo utilizado")

    def validate_name(self, value):
        if is_valid_product_name(value):
            return value
        else:
            raise serializers.ValidationError("Esse nome de produto já está sendo utilizado")            

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com preço negativo")
        else:
            return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com quantidade negativa")
        else:
            return value 

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class DeleteProductsSerializer(serializers.Serializer):
    class Meta:
        model = Products
        fields = [
            "id"
        ]
