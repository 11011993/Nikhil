# Generated by Django 4.2.6 on 2023-10-14 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenseshareapp', '0002_participantowe'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantowe',
            name='first_installment_receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_installment_receivers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participantowe',
            name='second_installment_receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_installment_receivers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participantowe',
            name='third_installment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participantowe',
            name='third_installment_receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_installment_receivers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participantowe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
