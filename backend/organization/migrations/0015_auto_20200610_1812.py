# Generated by Django 2.2.11 on 2020-06-10 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0014_auto_20200528_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectparents',
            options={'verbose_name_plural': 'Project Parents'},
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='organization_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='projectparents',
            name='parent_organization',
            field=models.ForeignKey(blank=True, help_text='Points to organization', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_parent_org', to='organization.Organization', verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='projectparents',
            name='project',
            field=models.ForeignKey(help_text="Points to organizations's project", on_delete=django.db.models.deletion.CASCADE, related_name='project_parent', to='organization.Project', verbose_name='Project'),
        ),
        migrations.AlterUniqueTogether(
            name='projectparents',
            unique_together=set(),
        ),
    ]
