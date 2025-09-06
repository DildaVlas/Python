from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    age = models.IntegerField()
    bio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'trainers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = 'subscription_plans'

    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    subscription = models.ForeignKey(SubscriptionPlan, null=True, blank=True, on_delete=models.SET_NULL, db_column='subscription_id')
    trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete=models.SET_NULL, db_column='trainer_id')

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    visited_at = models.DateTimeField()

    class Meta:
        db_table = 'visits'

    def __str__(self):
        return f"{self.client} - {self.visited_at}"
