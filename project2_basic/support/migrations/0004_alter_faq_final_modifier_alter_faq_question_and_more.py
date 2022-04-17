# Generated by Django 4.0.4 on 2022-04-17 09:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_faq_final_modifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='final_modifier',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=10, null=True, verbose_name='최종수정자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(blank=True, default='', verbose_name='질문'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]