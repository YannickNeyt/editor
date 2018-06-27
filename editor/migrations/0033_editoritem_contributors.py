# Generated by Django 2.0.5 on 2018-06-26 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0032_auto_20180626_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('profile_url', models.URLField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='editor.EditorItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('item', 'user')},
        ),
    ]