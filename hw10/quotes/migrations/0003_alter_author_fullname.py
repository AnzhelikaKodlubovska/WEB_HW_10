
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0002_alter_tag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="fullname",
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
