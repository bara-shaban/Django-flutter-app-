from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.email