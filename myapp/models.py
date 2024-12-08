from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    usertype=models.CharField(max_length=250)

class expert(models.Model):
    expertname=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    post=models.CharField(max_length=250)
    pin=models.CharField(max_length=250)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class trainer(models.Model):
    trainername=models.CharField(max_length=250)
    traineremail=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    post=models.CharField(max_length=250)
    pin=models.CharField(max_length=250)
    LOGIN=models.ForeignKey(login, default=1,on_delete=models.CASCADE)

class event(models.Model):
    eventname=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    date=models.CharField(max_length=250)

class batch(models.Model):
    batchname=models.CharField(max_length=250)

class user(models.Model):
    username=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    post=models.CharField(max_length=250)
    pin=models.CharField(max_length=250)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class allocated_user(models.Model):
    USER=models.ForeignKey(user, default=1,on_delete=models.CASCADE)
    BATCH=models.ForeignKey(batch, default=1,on_delete=models.CASCADE)

class trainer_allocation(models.Model):
    BATCH=models.ForeignKey(batch, default=1,on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer, default=1, on_delete=models.CASCADE)

class fee(models.Model):
    fee=models.CharField(max_length=250)

class pay_payment_alert(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    notification=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    month=models.CharField(max_length=250,default=1)
    year=models.CharField(max_length=250,default=1)

class chat_with_trainer_user(models.Model):
    chat=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    TRAINER = models.ForeignKey(trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)

class health_tips(models.Model):
    tip=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    EXPERT = models.ForeignKey(expert, default=1, on_delete=models.CASCADE)

class video(models.Model):
    EXPERT = models.ForeignKey(expert, default=1, on_delete=models.CASCADE)
    video=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    date=models.CharField(max_length=250)

class attendance(models.Model):
    date=models.CharField(max_length=250)
    attendances=models.CharField(max_length=250)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer, default=1, on_delete=models.CASCADE)

class chat_expert_user(models.Model):
    chat=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    EXPERT = models.ForeignKey(expert, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)

class health_details(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(trainer, default=1, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

class payment(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    FEE = models.ForeignKey(fee, default=1, on_delete=models.CASCADE)
    date = models.DateField()
    month = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    payment_status = models.CharField(max_length=250)
