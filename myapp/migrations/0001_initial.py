# Generated by Django 2.0.9 on 2024-06-12 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allocated_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=250)),
                ('attendances', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='chat_expert_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='chat_with_trainer_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('post', models.CharField(max_length=250)),
                ('pin', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='health_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='health_tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('EXPERT', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.expert')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('usertype', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='pay_payment_alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('payment_status', models.CharField(max_length=250)),
                ('FEE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.fee')),
            ],
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainername', models.CharField(max_length=250)),
                ('traineremail', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('post', models.CharField(max_length=250)),
                ('pin', models.CharField(max_length=250)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='trainer_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BATCH', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.batch')),
                ('TRAINER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('post', models.CharField(max_length=250)),
                ('pin', models.CharField(max_length=250)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('EXPERT', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.expert')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='pay_payment_alert',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='health_details',
            name='TRAINER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer'),
        ),
        migrations.AddField(
            model_name='health_details',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='expert',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
        migrations.AddField(
            model_name='chat_with_trainer_user',
            name='TRAINER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer'),
        ),
        migrations.AddField(
            model_name='chat_with_trainer_user',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='chat_expert_user',
            name='EXPERT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.expert'),
        ),
        migrations.AddField(
            model_name='chat_expert_user',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='TRAINER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='allocated_user',
            name='BATCH',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.batch'),
        ),
        migrations.AddField(
            model_name='allocated_user',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
