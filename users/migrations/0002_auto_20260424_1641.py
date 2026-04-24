from django.db import migrations

def create_schema(apps, schema_editor):
    schema_editor.execute("CREATE SCHEMA IF NOT EXISTS twitter_clone;")

def drop_schema(apps, schema_editor):
    schema_editor.execute("DROP SCHEMA IF EXISTS twitter_clone CASCADE;")

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_schema, reverse_code=drop_schema),
    ]