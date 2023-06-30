from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='users/',blank=True,null=True)
    data_of_birth=models.DateField(blank=True,null=True)
    verbose_name = "Profile"
    verbose_name_plural = "Profiles"

    def __str__(self):
        return  f"{self.user.username} profili"
