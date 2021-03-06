from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    #auto_now_add=True - set this attribute to current date and time
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    
    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

        def __str__(self):
            return self.text