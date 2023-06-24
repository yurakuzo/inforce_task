from django.db import models
from django.contrib.auth.models import AbstractUser
from main_app.models import Menu


class Employee(AbstractUser):
    full_name = models.CharField(max_length=100)
    ...

    def __str__(self):
        return f"Employee<{self.full_name}>"


class Vote(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    chosen_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote<{self.user}|{self.chosen_menu}>"
