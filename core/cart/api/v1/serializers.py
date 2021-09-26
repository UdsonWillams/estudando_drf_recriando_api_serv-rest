from products.models import Products
from cart.models import Carts
from rest_framework import serializers

class ProductsCartSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    quantity = serializers.CharField()
    class Meta:
        model = Products
        fields = [
            "id", 
            "quantity",
        ]


class CreateCartsSerializer(serializers.ModelSerializer):

    products = ProductsCartSerializer()
    class Meta:
        model = Carts
        fields = [
            "id",
            "user", 
            "products",            
        ]

    def validate_products(self, value):
        id = value["id"]
        quantity = value["quantity"]
        product = Products.objects.get(pk=id.id)

        if int(quantity) <= 0:
            raise serializers.ValidationError("valores negativos não podem ser atribuidos")

        if int(quantity) > int(product.quantity):
            raise serializers.ValidationError("Quantidade maior que o estoque do produto")

        return value


    def create(self, validated_data):
        user = validated_data["user"]
        products_id = validated_data["products"]["id"]
        cart_products_quantity = validated_data["products"]["quantity"]
        products = {"id" : products_id, "quantity" : cart_products_quantity}
        carts = Carts.objects.create(user=user, products=products)

        old_quantity = Products.objects.filter(pk=products_id.id)[0].quantity

        new_products_quantity = (int(old_quantity) - int(cart_products_quantity))
        Products.objects.filter(pk=products_id.id).update(quantity=new_products_quantity)
        return carts


class ListCartsSerializer(serializers.Serializer):
    user = serializers.CharField()
    products = serializers.CharField()
    class Meta:
        model = Carts
        fields = [
            "user",
            "products"
        ]
        

class ConcluirCartsSerializer(serializers.Serializer):
    class Meta:
        model = Carts
        fields = [
            "id"
        ]
