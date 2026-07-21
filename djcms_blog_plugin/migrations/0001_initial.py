from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleBlogEntriesPlugin',
            fields=[
                ('label', models.CharField(blank=True, help_text='Overrides the display name in the structure mode.', max_length=255, verbose_name='Label')),
                ('custom_blog_title', models.CharField(blank=True, help_text='Overrides the display name in the widget.', max_length=255, verbose_name='Custom Title')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
