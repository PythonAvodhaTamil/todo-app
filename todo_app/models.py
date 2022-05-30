from django.db import models

# Create your models here.
class ToDolist(models.Model):
    text=models.TextField()
    
    def __str__(self):
        return f"{self.text}"