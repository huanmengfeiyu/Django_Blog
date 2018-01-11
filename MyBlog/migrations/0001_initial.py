# Generated by Django 2.0.1 on 2018-01-09 08:43

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumQuestions',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('QuestionTitle', models.CharField(max_length=50)),
                ('Content', models.TextField()),
                ('Pub_Date', models.DateTimeField(auto_now_add=True)),
                ('Opt_Date', models.DateTimeField(auto_now=True)),
                ('IsSolve', models.IntegerField()),
                ('IsClose', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ForumReplys',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Content', models.TextField()),
                ('Pub_Date', models.DateTimeField(auto_now_add=True)),
                ('Opt_Date', models.DateTimeField(auto_now=True)),
                ('QuestionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question',
                                                 to='MyBlog.ForumQuestions')),
            ],
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('UserID', models.CharField(max_length=32)),
                ('Token', models.CharField(max_length=32)),
                ('PassWord', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=40)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(choices=[('M', 'Man'), ('F', 'Woman'), ('S', 'Secrecy')], default='S', max_length=1)),
                ('Card', models.CharField(max_length=18)),
                ('BirthDay', models.DateField()),
                ('Adress', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Pub_Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='forumquestions',
            name='AuthorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User',
                                    to='MyBlog.SysUser'),
        ),
        migrations.AddField(
            model_name='forumquestions',
            name='TagID',
            field=models.ManyToManyField(to='MyBlog.Tags'),
        ),
    ]