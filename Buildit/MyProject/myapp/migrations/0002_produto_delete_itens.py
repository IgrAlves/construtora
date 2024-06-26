# Generated by Django 5.0.6 on 2024-05-30 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('descript', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('path', models.ImageField(upload_to='imagens/')),
                ('amount', models.IntegerField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Itens',
        ),
    ]
