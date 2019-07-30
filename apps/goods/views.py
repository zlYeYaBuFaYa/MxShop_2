from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from .filter import GoodsFilter
# Create your views here.

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100


class GoodsListViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """商品列表"""

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # search_fields = ['name']
    # search_fields = ["name", "goods_brief", "goods.desc"]
    # filterset_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')
    filterset_class = GoodsFilter


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    list:
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer