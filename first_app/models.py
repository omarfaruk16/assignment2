from django.db import models

class TodoModel(models.Model):
    STATUS_CHOICES = [
        ('incomplete', 'Incomplete'),
    ]
    
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='incomplete')
    
    def __str__(self):
        return self.title

    
class FormModel(models.Model):
    formname = models.CharField(max_length=100)

    def __str__(self):
        return self.formname


    