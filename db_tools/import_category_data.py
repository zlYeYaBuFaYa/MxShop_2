# coding=utf-8

import os
import sys


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

import_data = row_data

for data_1 in import_data:
    obj_1 = GoodsCategory()
    obj_1.name = data_1["name"]
    obj_1.code = data_1["code"]
    obj_1.category_type = 1
    obj_1.save()

    for data_2 in data_1["sub_categorys"]:
        obj_2 = GoodsCategory()
        obj_2.name = data_2["name"]
        obj_2.code = data_2["code"]
        obj_2.category_type = 2
        obj_2.parent_category = obj_1
        obj_2.save()

        for data_3 in data_2["sub_categorys"]:
            obj_3 = GoodsCategory()
            obj_3.name = data_2["name"]
            obj_3.code = data_2["code"]
            obj_3.category_type = 3
            obj_3.parent_category = obj_2
            obj_3.save()