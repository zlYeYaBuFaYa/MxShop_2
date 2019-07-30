"""MxShop_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListViewSet, CategoryViewSet

import xadmin
# from MxShop_2.settings import MEDIA_ROOT

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, basename='goods')
router.register(r'categrorys', CategoryViewSet, basename='categrorys')
# urlpatterns = router.urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'docs/', include_docs_urls(title="线上商城")),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^goods/', goods_list),
    url(r'^', include(router.urls)),
    # url(r'^index/', TemplateView.as_view(template_name='index.html'), name="index"),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^login/$', obtain_jwt_token),
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^alipay/return/', AliPayView.as_view(), name="alipay"),
    # url('', include('social_django.urls', namespace='social'))  # 第三方登录
]
