# coding=utf-8
from django.db.models import Q
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Goods

class GoodsFilter(filters.FilterSet):
    """  商品的过滤类  """
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr="gte", help_text="最低价格")
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr="lte",  help_text="最高价格")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains", help_text="名字")
    top_category = filters.NumberFilter(method="top_category_filter", help_text='上级类型')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category=value) | Q(
            category__parent_category__parent_category=value))

    class Meta:
        model = Goods
        fields = ['category', 'name', 'min_price', 'max_price']
