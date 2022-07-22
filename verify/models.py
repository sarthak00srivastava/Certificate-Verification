from django.db import models

# Create your models here.

class Certificates(models.Model):
    c_num = models.CharField(max_length=20)
    c_name = models.CharField(max_length=50)
    c_title = models.CharField(max_length=50)
    c_mode = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def _str_(self):
        return '{}'.format(self.c_num)