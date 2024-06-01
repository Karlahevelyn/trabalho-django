from django.db import models

class Roupa(models.Model):
    id_roupas=models.AutoField(primary_key=True)
    tipo=models.TextField(max_length=255)
    cor=models.TextField(max_length=255)