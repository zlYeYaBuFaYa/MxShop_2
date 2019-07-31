# coding=utf-8
from rest_framework.serializers import ModelSerializer

from .models import Goods, GoodsCategory


class CategorySerializer3(ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"
class GoodsSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"
