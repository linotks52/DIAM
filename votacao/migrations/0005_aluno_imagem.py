# Generated by Django 4.1.7 on 2023-04-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0004_aluno_votosmax'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='imagem',
            field=models.CharField(default='default-user-image.png', max_length=100),
        ),
    ]