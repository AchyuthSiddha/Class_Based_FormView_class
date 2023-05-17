from django.db import models


from django.core import validators
# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    sid=models.IntegerField(primary_key=True,validators=[validators.MaxLengthValidator(9999)])
    semail=models.EmailField()
    saddress=models.TextField(max_length=100)

    def __str__(self):
        return str(self.sid)

