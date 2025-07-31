from rest_framework import serializers
from main.models import Product, Contractor, StorageItem, Document, DocumentItem, Operation, Category


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['username', 'operation', 'dt_created']


class StorageItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['product_title'] = instance.product.title
        result['product_price'] = instance.product.price
        result['product_category_name'] = instance.product.category.name if instance.product.category else None
        return result

    class Meta:
        model = StorageItem
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['contractor_title'] = instance.contractor.title
        return result

    class Meta:
        model = Document
        fields = '__all__'


class DocumentItemSerializer(serializers.ModelSerializer):
    modifications = serializers.StringRelatedField(many=True)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['product_title'] = instance.product.title
        result['product_price'] = instance.product.price
        result['product_category_name'] = instance.product.category.name if instance.product.category else None
        result['modifications'] = [mod.description for mod in instance.product.modifications.all()]
        return result

    class Meta:
        model = DocumentItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Включаем все поля (id, name)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'dt_created', 'dt_updated', 'to_remove', 'category', 'modifications']  # Добавьте modifications

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.modifications = validated_data.get('modifications', instance.modifications)  # Обновите modifications
        instance.save()
        return instance
