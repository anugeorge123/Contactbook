from django.db import models

class Contactbook(models.Model):
	name=models.CharField(max_length=100)
	number=models.CharField(max_length=100)


class Meta:
	db_table = "contactbook"
