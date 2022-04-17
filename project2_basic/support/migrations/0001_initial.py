# Generated by Django 4.0.4 on 2022-04-17 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True, verbose_name='질문')),
                ('category', models.CharField(choices=[('일반', '일반'), ('계정', '계정'), ('기타', '기타')], max_length=10, verbose_name='카테고리')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='답변')),
                ('create_date', models.DateTimeField(verbose_name='생성일시')),
                ('final_modify_date', models.DateTimeField(verbose_name='최종 수정일시')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
