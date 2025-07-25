from rest_framework import serializers
from main.models import Product, Contractor, StorageItem, Document, DocumentItem, Operation, Category, \
    ProductModification


class ProductModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModification
        fields = ['description']


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
    modifications = ProductModificationSerializer(many=True)

    class Meta:
        model = Product
        fields = ['category', 'id', 'title', 'price', 'to_remove', 'modifications', 'dt_created', 'dt_updated']

    def create(self, validated_data):
        modifications_data = validated_data.pop('modifications', [])
        product = Product.objects.create(**validated_data)
        for modification_data in modifications_data:
            ProductModification.objects.create(product=product, **modification_data)
        return product

    def update(self, instance, validated_data):
        modifications_data = validated_data.pop('modifications', [])
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.to_remove = validated_data.get('to_remove', instance.to_remove)
        instance.save()

        # Обновление модификаций
        for modification_data in modifications_data:
            modification_id = modification_data.get('id', None)
            if modification_id:  # Если ID модификации указан, обновляем ее
                modification = ProductModification.objects.get(id=modification_id, product=instance)
                modification.description = modification_data.get('description', modification.description)
                modification.save()
            else:  # Если ID не указан, создаем новую модификацию
                ProductModification.objects.create(product=instance, **modification_data)

        return instance


