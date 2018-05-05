#!/usr/bin/python
# -*- coding:utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class JdProducts(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jd_products'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    default_good_count = models.CharField(max_length=255, blank=True, null=True)
    poor_comment_count = models.CharField(max_length=255, blank=True, null=True)
    good_comment_count = models.CharField(max_length=255, blank=True, null=True)
    good_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    general_comment_count = models.CharField(max_length=255, blank=True, null=True)
    poor_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    general_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    p_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductBasemakeup(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_basemakeup'


class ProductComment(models.Model):
    product_id = models.IntegerField()
    comment_id = models.CharField(primary_key=True, max_length=255)
    comment_uid = models.CharField(max_length=255, blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)
    creation_time = models.CharField(max_length=255, blank=True, null=True)
    after_comment_content = models.CharField(max_length=255)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_comment'


class ProductEye(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_eye'


class ProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_lipstick'


class ProductOtherPerfume(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_other_perfume'


class ProductPerfume(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    my_category = models.CharField(max_length=60, blank=True, null=True)
    platform = models.CharField(max_length=60, blank=True, null=True)
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    finish_get_data = models.IntegerField(blank=True, null=True)
    store = models.CharField(max_length=60, blank=True, null=True)
    clean_weight = models.CharField(max_length=60, blank=True, null=True)
    package = models.CharField(max_length=60, blank=True, null=True)
    fragrance = models.CharField(max_length=60, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    fragrance_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_perfume'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    account = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class VipProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    v_sku_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vip_product_lipstick'
