from django.db import models

class Menu(models.Model):
    DAYS_CHOICE = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
    )

    title = models.CharField(max_length=35, unique=True)
    day = models.CharField(choices=DAYS_CHOICE)
    price = models.IntegerField()
    description = models.TextField(blank=True) # We can also make it ManyToMany field to another Ingredient model-class
    ...

    def __str__(self) -> str:
        return f"Menu<{self.title}|{self.day}>"
    

class Restaurant(models.Model):
    title = models.CharField(max_length=35, unique=True)
    menus = models.ManyToManyField(Menu)
    ...

    def __str__(self) -> str:
        return f"Restaurant<{self.title}>"
