# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.management import \
    create_permissions
from django.db import migrations, models


def generate_permissions(apps, schema_editor):
    blog = apps.get_model(
        'auth', 'Post')
    Permission = apps.get_model(
        'auth', 'Permission')
    content_type = apps.get_model("contenttypes", "ContentType")
    post = content_tpe.objects.get_for_model(blog)
    try:
        Permission.objects.get(
            codename='add_post',
            name='can add post',
            content_type=post)
    except Permission.DoesNotExist:
        models_module = getattr(
            apps, 'models_module', None)
        if models_module is None:
            apps.models_module = True
            create_permissions(apps, verbosity=0)
            apps.models_module = None
        else:
            raise


def reverse_code(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('auth',
         '0006_require_contenttypes_0002'),
        ('post',
         '0004_add_view_future_post_permission'),
        ('contenttypes', '__latest__'),
    ]

    operations = [
        migrations.RunPython(
            generate_permissions,
            reverse_code,
        )
    ]