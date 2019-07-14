# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import \
    make_password
from django.db import migrations, models


def add_user_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model(
        'auth', 'Permission')
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('user', 'User')
    Laughter_user = User.objects.create(
        email='isaacamunenwa@gmail.com',
        password=make_password('laughter@2000'),
        is_active=True,
        is_staff=True,
        is_superuser=True)
    Laughter_profile = Profile.objects.create(
        user=Laughter_user,
        name='Laughter',
        slug='laughter',
        about='The author of this site!')
    # Django Girls is a real and very cool
    # organization but they are not affiliated
    # with this book and the email above is *not*
    # a real one.  Use of their name is for
    # illustrative purposes only.
    David_user = User.objects.create(
        email='florenceamunenwa@gmail.com',
        password=make_password('laughter@2000'),
        is_active=True,
        is_staff=True,
        is_superuser=False)
    David_profile = Profile.objects.create(
        user=David_user,
        name='David Amunenwa',
        slug='davidamunenwa',
        about=(
            'Django Girls is a non-profit '
            'organization that empowers and '
            'helps women to organize free, '
            'one-day programming workshops by '
            'providing tools, resources and '
            'support. It was born in Berlin and '
            'started by two Polish girls: Ola '
            'Sitarska and Ola Sendecka.'))
    contributors = Group.objects.create(
        name='contributors')
    David_user.groups.add(contributors)
    permissions = [
        'add_post',
        'change_post',
    ]
    for perm in permissions:
        contributors.permissions.add(
            Permission.objects.get(
                codename=perm,
                content_type__app_label='blog'))


def remove_user_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('user', 'User')
    Profile.objects.get(slug='laughter').delete()
    Profile.objects.get(
        slug='davidamunenwa').delete()
    User.objects.get(
        email='isaacamunenwa@gmail.com').delete()
    User.objects.get(
        email='florenceamunenwa@gmail.com').delete()
    Group.objects.get(
        name='contributors').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_permissions'),
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.RunPython(
            add_user_data,
            remove_user_data)
    ]