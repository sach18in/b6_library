from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    # is_active = models.CharField(max_length=1, default="Y")

    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"

class company(models.Model):
    pass

class book_auther(models.Model):
    pass
