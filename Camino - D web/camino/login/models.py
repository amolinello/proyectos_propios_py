from django.db import models

# Create your models here. y se registran en admin
class Users_db(models.Model):
    user = models.CharField(max_length=15)
    passw = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    state = models.CharField(max_length=10)
    last_log = models.DateTimeField(auto_now_add=True)